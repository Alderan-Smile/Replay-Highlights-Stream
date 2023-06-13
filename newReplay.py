import configparser
import os
import time
import keyboard
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from moviepy.editor import VideoFileClip
import pyglet
from pydub import AudioSegment
from pydub.playback import play as play_audio
from logger import log

try:
    # Lee la configuración desde el archivo externo config.ini
    config = configparser.ConfigParser()
    config.read('config.ini')
    try:
        video_folder = config['DEFAULT']['video_folder']
    except KeyError:
        log("La clave 'video_folder' no está definida en el archivo config.ini.")
        exit(1)

    # Rutas de carpetas
    watch_folder = config.get('Paths', 'WatchFolder')
    ignore_folder = config.get('Paths', 'IgnoreFolder')

    # Lista de reproducción
    playlist = []
    played_videos = set()

    # Clase de manipulador de eventos para detectar cambios en la carpeta
    class FileCreatedEventHandler(FileSystemEventHandler):
        def on_created(self, event):
            if not event.is_directory and event.src_path.endswith('.mp4'):
                video_path = event.src_path
                try:
                    if video_path not in playlist and not video_path.startswith(ignore_folder):
                        playlist.append(video_path)
                except Exception as e:
                    log(f"Error processing video: {video_path}")
                    log(e)

    # Función para reproducir los videos en la lista de reproducción
    def play_videos():
        while True:
            if len(playlist) == 0:
                time.sleep(1)
                continue

            video_filename = playlist.pop(0)
            video_path = os.path.join(video_folder, video_filename)
            if video_path not in played_videos:
                try:
                    log(f'Reproduciendo: {video_path}')

                    # Simula la tecla "page up" antes de iniciar la reproducción
                    keyboard.press('page up')
                    keyboard.release('page up')

                    # Extrae el audio del video utilizando pydub
                    video = VideoFileClip(video_path)
                    audio = video.audio
                    audio_path = 'temp_audio.wav'
                    audio.write_audiofile(audio_path, codec='pcm_s16le')

                    # Reproduce el audio con pyglet
                    audio_player = pyglet.media.Player()
                    audio = pyglet.media.load(audio_path)
                    audio_player.queue(audio)
                    audio_player.play()

                    # Registra el evento de finalización de reproducción del audio
                    @audio_player.event
                    def on_player_eos():
                        audio_player.delete()
                        os.remove(audio_path)

                    # Muestra el video sin audio utilizando MoviePy
                    video.preview(fullscreen=False, audio=False)
                    video.close()

                    played_videos.add(video_path)
                    log(f'Terminado: {video_path}')

                    # Simula la tecla "page down" después de reproducir el último video
                    if len(playlist) == 0:
                        log(f'Lista terminada Terminada')
                        time.sleep(2)
                        keyboard.press('page down')
                        keyboard.release('page down')

                    # Elimina el video de la lista de reproducción
                    if video_path in played_videos:
                        played_videos.remove(video_path)
                except Exception as e:
                    if len(playlist) == 0:
                        log(f'Lista terminada Terminada con excepciones')
                        time.sleep(2)
                        keyboard.press('page down')
                        keyboard.release('page down')
                    log("Error al reproducir el video:", video_path)
                    log("Error:", str(e))


    # Configura el observador para detectar cambios en la carpeta
    event_handler = FileCreatedEventHandler()
    observer = Observer()
    observer.schedule(event_handler, watch_folder, recursive=True)
    observer.start()

    # Inicia la reproducción de videos
    try:
        play_videos()
    except Exception as e:
        log(f"Excepción al reproducir videos: {str(e)}")

    # Detiene el observador cuando se cierra la ventana
    keyboard.wait('esc')
    observer.stop()
    observer.join()
except Exception as e:
    log(f"Excepción no controlada: {str(e)}")