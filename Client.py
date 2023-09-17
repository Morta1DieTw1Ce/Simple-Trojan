import os
import socket

def client():
    try:
        current_directory = os.getcwd()
        for filename in os.listdir(current_directory):
            file_path = os.path.join(current_directory, filename)  
            if filename.endswith('.txt'):
                with open(file_path, 'r') as file:
                    file_content = file.read()
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip, port))
                s.send(file_content.encode())
    except Exception as e:
        print(f"An error occurred: {e}")
        exit()

ip = '127.0.0.1'
port = 12345


client()
