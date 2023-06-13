import os
import requests

config_file_path = 'config.ini'

if not os.path.isfile(config_file_path):
    # Descargar el archivo config.ini desde el repositorio en GitHub
    url = 'https://raw.githubusercontent.com/tu_usuario/tu_repositorio/ruta_al_archivo/config.ini'
    response = requests.get(url)

    if response.status_code == 200:
        with open(config_file_path, 'wb') as file:
            file.write(response.content)
        print("El archivo config.ini ha sido descargado exitosamente.")
    else:
        print("No se pudo descargar el archivo config.ini desde el repositorio.")
else:
    print("El archivo config.ini ya existe.")
