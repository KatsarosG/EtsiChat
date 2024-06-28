import socket
import threading

host = 'localhost'
port = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(5)

clients = []
usernames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            username = usernames[index]
            broadcast(f'{username} left the chat'.encode('ascii'))
            usernames.remove(username)
            break

def receive():
    while True:
        client, address = server.accept()
        print(f'Connected with {str(address)}')

        client.send('GET_USERNAME'.encode('ascii'))
        username = client.recv(1024).decode('ascii')
        usernames.append(username)
        clients.append(client)

        print(f'Nickname of client is: {username}')
        client.send("Connected to server".encode('ascii'))
        broadcast(f'{username} has joined chat'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print(f'Server listening on {host}:{port}')
receive()
