import os
import cv2
import time
import keyboard
import json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class VideoHandler(FileSystemEventHandler):
    def __init__(self, folder_path, ignored_folders):
        super().__init__()
        self.folder_path = folder_path
        self.ignored_folders = ignored_folders
        self.playlist = []
        self.is_playing = False
        self.played_videos = set()

    def on_created(self, event):
        if not event.is_directory and event.src_path.endswith(".mp4"):
            file_path = event.src_path
            if not self.is_ignored(file_path) and file_path not in self.played_videos:
                self.add_to_playlist(file_path)
                self.play_videos()

    def is_ignored(self, file_path):
        for ignored_folder in self.ignored_folders:
            if ignored_folder in file_path:
                return True
        return False

    def add_to_playlist(self, file_path):
        self.playlist.append(file_path)

    def play_videos(self):
        if not self.is_playing:
            self.is_playing = True
            while self.playlist:
                video_path = self.playlist.pop(0)
                self.played_videos.add(video_path)
                self.play_video(video_path)
            self.is_playing = False
            ##keyboard.press_and_release("page down")  # Presionar "page down" al finalizar la lista

    def play_video(self, video_path):
        keyboard.press_and_release("page up")  # Presionar "page up" antes de reproducir cada video
        cap = cv2.VideoCapture(video_path)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            cv2.imshow('Video Player', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):  # Presionar 'q' para detener la reproducción
                break
            time.sleep(0.033)  # Retraso de aproximadamente 1/30 segundos (30 fps)
        cap.release()


if __name__ == "__main__":
    with open("config.json") as config_file:
        config = json.load(config_file)

    folder_path = config["folder_path"]
    ignored_folders = config["ignored_folders"]

    event_handler = VideoHandler(folder_path, ignored_folders)
    observer = Observer()
    observer.schedule(event_handler, folder_path, recursive=True)
    observer.start()

    try:
        while True:
            if not event_handler.is_playing and len(event_handler.playlist) == 0:
                break
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

    ##keyboard.press_and_release("page down")  # Presionar "page down" al terminar la lista de reproducción

cv2.destroyAllWindows()
