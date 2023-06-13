import os
import time

def log(message):
    log_folder = os.path.join(os.getcwd(), 'logs')
    os.makedirs(log_folder, exist_ok=True)
    log_file = time.strftime('%d%m%Y.log')
    log_path = os.path.join(log_folder, log_file)

    with open(log_path, 'a') as file:
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        print(f'[{timestamp}] {message}\n')
        file.write(f'[{timestamp}] {message}\n')
