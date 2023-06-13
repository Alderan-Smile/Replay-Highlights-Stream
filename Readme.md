# OutPlayed Replay Stream

Este proyecto es una herramienta para reproducir automáticamente archivos de video en una carpeta específica.

## Requisitos

- Python 3.6 o superior
- Paquetes de Python: `configparser`, `subprocess`, `time`, `keyboard`, `watchdog`, `moviepy`, `pyglet`, `pydub`, `logger`, `cv2`, `requests`

## Instalación

1. Clona este repositorio en tu máquina local.
2. Instala los paquetes de Python requeridos ejecutando el siguiente comando en tu terminal:

pip install configparser subprocess time keyboard watchdog moviepy pyglet pydub opencv-python-headless requests


## Configuración

Antes de ejecutar el programa, asegúrate de configurar los siguientes parámetros en el archivo `config.ini`:

```ini
[Paths]
WatchFolder = C:\Users\Admn\Videos\Overwolf\Outplayed
IgnoreFolder = C:\Users\Admn\Videos\Overwolf\Outplayed\temp-capture

[DEFAULT]
video_folder = C:\Users\Admn\Videos\Overwolf\Outplayed

[Framerate]
# Opciones de tasa de cuadros por segundo:
# - original_player: Tasa de cuadros por segundo original del reproductor
# - original_video: Tasa de cuadros por segundo original del video
# - 15: Tasa de cuadros por segundo de 15
# - 30: Tasa de cuadros por segundo de 30
# - 45: Tasa de cuadros por segundo de 45
# - 60: Tasa de cuadros por segundo de 60
option = original_video

[LogSettings]
DaysThreshold = 3
```
Asegúrate de proporcionar las rutas correctas para `WatchFolder`, `IgnoreFolder` y `video_folder`. Puedes ajustar la opción de `Framerate` según tus preferencias.

## Uso
1. Ejecuta el archivo `newReplay.py` con el siguiente comando:
```
python newReplay.py
```
   Esto iniciará el programa y comenzará a buscar nuevos archivos de video en la carpeta especificada en `WatchFolder`.

2. Cuando se detecte un nuevo archivo de video, se reproducirá automáticamente sin sonido. Puedes usar las teclas "Page Up" y "Page Down" para navegar por los videos.

3. Los videos reproducidos se registrarán en archivos de registro ubicados en la carpeta logs. Los archivos de registro antiguos se eliminarán según la configuración especificada en DaysThreshold.

4. Puedes detener el programa presionando la tecla "Esc".

¡Disfruta de tus repeticiones de juego automatizadas!

## Créditos
Este proyecto fue desarrollado por Oliver Consterla (Alderan Smile). Si tienes alguna pregunta o sugerencia, no dudes en contactarme.
