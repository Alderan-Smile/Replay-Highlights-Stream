import os
import configparser
import keyboard
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from moviepy.editor import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

config = configparser.ConfigParser()
config.read('config.ini')

video_folder = config['Paths']['video_folder']
temp_folder = config['Paths']['temp_folder']

playlist = []
played_videos = []


class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory and event.src_path.endswith('.mp4'):
            if event.src_path.startswith(temp_folder):
                return

            if event.src_path not in playlist:
                playlist.append(event.src_path)

            if len(playlist) == 1:
                keyboard.press_and_release('page up')


def play_video(file_path):
    video = VideoFileClip(file_path)
    video.preview()
    played_videos.append(file_path)
    playlist.remove(file_path)
    keyboard.press_and_release('page down')


def start_monitoring():
    event_handler = FileEventHandler()
    observer = Observer()
    observer.schedule(event_handler, video_folder, recursive=True)
    observer.start()

    try:
        while True:
            if len(playlist) > 0:
                file_path = playlist[0]
                if file_path not in played_videos:
                    play_video(file_path)
            else:
                time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()


if __name__ == '__main__':
    start_monitoring()
