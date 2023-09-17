import socket

def server():
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((ip, port))
        server_socket.listen(5)

        print(f"Server listening on {ip}:{port}")

        while True:
            client_socket, client_address = server_socket.accept()
            data = client_socket.recv(1024).decode()

            if data:
                print(f"Received data from {client_address}:")
                print(data)

            client_socket.close()

    except Exception as e:
        print(f"An error occurred: {e}")
        exit()

ip = '127.0.0.1'
port = 12345

server()
