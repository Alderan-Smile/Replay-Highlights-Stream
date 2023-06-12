import os
import time
import cv2
import configparser
import keyboard
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Clase para manejar los eventos de Watchdog
class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        # Verificar si el archivo creado es un archivo MP4
        if event.is_directory:
            return
        if not event.src_path.lower().endswith(".mp4"):
            return

        # Ignorar la carpeta específica
        if "temp-capture" in event.src_path:
            return

        # Agregar el archivo a la lista de reproducción
        playlist.append(event.src_path)

# Clase para reproducir los videos
class VideoPlayer:
    def __init__(self):
        self.current_video = None

    def play_videos(self):
        while True:
            # Verificar si la lista de reproducción está vacía
            if len(playlist) == 0:
                # Simular presionar la tecla "page down" una vez
                keyboard.press_and_release("page down")
                time.sleep(0.1)
                continue

            # Obtener el siguiente video de la lista de reproducción
            video_path = playlist.pop(0)

            # Reproducir el video
            self.play_video(video_path)

    def play_video(self, video_path):
        # Simular presionar la tecla "page up" una vez
        keyboard.press_and_release("page up")
        time.sleep(0.1)

        # Leer el video usando cv2
        video = cv2.VideoCapture(video_path)

        # Obtener la velocidad de fotogramas (fps) del video
        fps = video.get(cv2.CAP_PROP_FPS)

        # Reproducir el video fotograma por fotograma
        while True:
            ret, frame = video.read()
            if not ret:
                break

            # Mostrar el fotograma en una ventana
            cv2.imshow("Video Player", frame)

            # Esperar según la velocidad de fotogramas del video
            time.sleep(1 / fps)

            # Detectar si se presiona la tecla ESC para salir del programa
            if cv2.waitKey(1) == 27:
                break

        # Cerrar la ventana de reproducción y liberar los recursos
        cv2.destroyAllWindows()
        video.release()

        # Eliminar el video de la lista de reproducción si se reprodujo completamente
        if video_path == self.current_video:
            self.current_video = None

# Función para cargar la configuración desde el archivo config.ini
def load_config():
    config = configparser.ConfigParser()
    config.read("config.ini")
    return config

# Obtener la configuración
config = load_config()

# Obtener la ruta de la carpeta a monitorear
folder_path = config.get("General", "Folder")

# Obtener la lista de carpetas a ignorar
ignore_folders = config.get("General", "IgnoreFolders").split(",")

# Crear la lista de reproducción
playlist = []

# Crear un observador de Watchdog
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_path, recursive=True)
observer.start()

# Crear un reproductor de videos
player = VideoPlayer()

# Iniciar la reproducción de videos
player.play_videos()

# Mantener el proyecto en ejecución hasta que el usuario lo requiera
while True:
    # Detectar si se presiona la tecla ESC para salir del programa
    if cv2.waitKey(1) == 27:
        observer.stop()
        break

# Detener el observador de Watchdog
observer.join()
