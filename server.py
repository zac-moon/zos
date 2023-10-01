import socket
import threading

def handle(client_socket):
    data = client_socket.recv(1024).decode('utf-8')
    print(data)
    datas = data.split(':')
    type = datas[0]

    if type == 'l':
        id,password = datas[1],datas[2]
        try:
            file = open(f'cldb/users/{id}')
            corPass = file.read()
            file.close()
            if password == corPass:
                client_socket.send('true'.encode('utf-8'))
            else:
                client_socket.send('false2'.encode('utf-8'))
        except FileNotFoundError:
            client_socket.send('false1'.encode('utf-8'))

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host,port = 'localhost',11704     
server_socket.bind((host, port))


server_socket.listen(5)

print(f"Server is listening on {host}:{port}")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")
    client_thread = threading.Thread(target=handle, args=(client_socket,))
    client_thread.start()
