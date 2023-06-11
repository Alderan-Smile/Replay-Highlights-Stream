import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import keyboard
from moviepy.editor import VideoFileClip

class FileEventHandler(FileSystemEventHandler):
    def __init__(self):
        self.processed_files = set()
        self.total_duration = 0

    def on_created(self, event):
        if event.is_directory or not event.src_path.endswith('.mp4'):
            return

        # Obtener el nombre de la carpeta contenedora
        parent_folder = os.path.dirname(event.src_path)
        if 'temp-capture' in parent_folder:
            return

        # Verificar si el archivo ya ha sido procesado
        if event.src_path in self.processed_files:
            return

        # Agregar el archivo a la lista de archivos procesados
        self.processed_files.add(event.src_path)

        # Verificar la duración del video
        duration = get_video_duration(event.src_path)
        if duration is not None:
            self.total_duration += duration
            # Simular pulsaciones de teclas
            keyboard.press_and_release('page up')
            #print("Duracion replay",self.total_duration)
            time.sleep(self.total_duration)
            #print("Termina duracion")
            keyboard.press_and_release('page down')
            self.total_duration = 0

def get_video_duration(file_path):
    try:
        clip = VideoFileClip(file_path)
        duration = clip.duration
        clip.close()
        return duration
    except Exception as e:
        print(f"Error al obtener la duración del video: {str(e)}")
        return None

def main():
    path = 'C:\\xampp\\htdocs\\outplayed\\Outplayed'

    event_handler = FileEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()
