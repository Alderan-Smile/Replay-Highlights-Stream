# Replay Highlights Stream
[![es](https://img.shields.io/badge/lang-es-yellow.svg)](https://github.com/Alderan-Smile/outplayed/blob/main/Readme.md)

This project is a tool for automatically playing video files in a specific folder.

## Requirements

- Python 3.6 or higher
- Python packages: `configparser`, `subprocess`, `time`, `keyboard`, `watchdog`, `moviepy`, `pyglet`, `pydub`, `opencv-python-headless`, `requests`

## Installation

1. Clone this repository on your local machine.
2. Install the required Python packages by running the following command in your terminal:

pip install configparser subprocess time keyboard watchdog moviepy pyglet pydub opencv-python-headless requests


## Configuration

Before running the program, make sure to configure the following parameters in the `config.ini` file:

```ini
[Paths]
WatchFolder = C:\Users\Admn\Videos\Overwolf\Outplayed
IgnoreFolder = C:\Users\Admn\Videos\Overwolf\Outplayed\temp-capture

[DEFAULT]
video_folder = C:\Users\Admn\Videos\Overwolf\Outplayed

[Framerate]
# Frame rate options:
# - original_player: Original frame rate of the player
# - original_video: Original frame rate of the video
# - 15: 15 frames per second
# - 30: 30 frames per second
# - 45: 45 frames per second
# - 60: 60 frames per second
option = original_video

[LogSettings]
DaysThreshold = 3
```
Make sure to provide the correct paths for `WatchFolder`, `IgnoreFolder`, and `video_folder`. You can adjust the `Framerate` option according to your preferences.

## Usage
1. Run the `newReplay.py` file with the following command:

```
python newReplay.py
```

This will start the program and begin searching for new video files in the folder specified in `WatchFolder`.

2. When a new video file is detected, it will automatically play without sound. You can use the "Page Up" (Replay scene) and "Page Down" (Back scene) keys in macros to switch between scenes.

3. Played videos will be logged in log files located in the logs folder. Old log files will be deleted based on the threshold specified in DaysThreshold.

4. You can stop the program by pressing the "Esc" key.

Enjoy your automated game replays!

## Credits
This project was developed by Oliver Consterla (Alderan Smile). If you have any questions or suggestions, feel free to contact me.
