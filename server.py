import socket
import threading
import serverGui
from datetime import datetime

maxClients = 5
host = 'localhost'
port = 12347 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))

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

        client.send('GET_USERNAME'.encode('ascii'))
        username = client.recv(1024).decode('ascii')
        usernames.append(username)
        clients.append(client)

        consoleWrite(f'User {username} connected from {str(address)}')
        client.send("Connected to server".encode('ascii'))
        broadcast(f'{username} has joined chat'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

def consoleWrite(text):
    print(text)
    newConsoleText =  str(serverGui.Console.label.text() + '\n' + str(datetime.now()) + " >> " + text)
    serverGui.Console.label.setText(newConsoleText)

def startServer():
    server.listen(maxClients)
    consoleWrite(f'Server listening on {host}:{port}')
    thread = threading.Thread(target=receive)
    thread.start()

def stopServer():
    server.close()
    consoleWrite('Clients Disconnected')

