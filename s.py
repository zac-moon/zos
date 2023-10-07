import socket
import threading

def handle_client(client_socket):
    try:
        data = client_socket.recv(1024).decode('utf-8')
        print(data)
        datas = data.split(':')
        command_type = datas[0]

        if command_type == 'l':
            # Handle login request
            id, password = datas[1], datas[2]
            try:
                with open(f'cldb/users/{id}', 'r') as file:
                    correct_password = file.read().strip()
                    if password == correct_password:
                        client_socket.send('true'.encode('utf-8'))
                    else:
                        client_socket.send('false2'.encode('utf-8'))
            except FileNotFoundError:
                client_socket.send('false1'.encode('utf-8'))

        elif command_type == 'f':
            # Handle file-related requests (e.g., saving a file)
            file_type, user, file_name, entry = datas[1], datas[2].split('/')[0], datas[2].split('/')[1], datas[3]
            print(f'File : {file_type} - user[{user}] filename[{file_name}] in hd ')

            if file_type == 'save':
                with open(f'cldb/hd/{user}/{file_name}', 'w') as file:
                    file.write(entry)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host, port = 'localhost', 11704

    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Server is listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == '__main__':
    main()
