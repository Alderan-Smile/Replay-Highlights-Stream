import os
import configparser

config_file = 'config.ini'

def configExist():
    if not os.path.isfile(config_file):
        config = configparser.ConfigParser()
        config['Paths'] = {
            'WatchFolder': 'C:\\Users\\Admn\\Videos\\Overwolf\\Outplayed',
            'IgnoreFolder': 'C:\\Users\\Admn\\Videos\\Overwolf\\Outplayed\\temp-capture'
        }
        config['DEFAULT'] = {'video_folder': 'C:\\Users\\Admn\\Videos\\Overwolf\\Outplayed'}
        config['Framerate'] = {
            '# Opciones de tasa de cuadros por segundo:': None,
            '# - original_player: Tasa de cuadros por segundo original del reproductor': None,
            '# - original_video: Tasa de cuadros por segundo original del video': None,
            '# - 15: Tasa de cuadros por segundo de 15': None,
            '# - 30: Tasa de cuadros por segundo de 30': None,
            '# - 45: Tasa de cuadros por segundo de 45': None,
            '# - 60: Tasa de cuadros por segundo de 60': None,
            'option': 'original_player'
        }
        config['LogSettings'] = {'DaysThreshold': '3'}

        with open(config_file, 'w') as file:
            config.write(file)
            print(f"Archivo '{config_file}' creado exitosamente.")