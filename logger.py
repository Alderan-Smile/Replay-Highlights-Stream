import os
import time

log_folder = os.path.join(os.getcwd(), 'logs')
os.makedirs(log_folder, exist_ok=True)
log_file = time.strftime('%d%m%Y.log')
log_path = os.path.join(log_folder, log_file)

def log(message):
    with open(log_path, 'a') as file:
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        print(f'[{timestamp}] {message}\n')
        file.write(f'[{timestamp}] {message}\n')

def initialize_log():
    with open(log_path, 'a') as file:
        file.write('\n')
        timestamp = time.strftime('%A %d de %B del %Y %H:%M:%S')
        file.write(f'############## {timestamp} ##############\n')

initialize_log()