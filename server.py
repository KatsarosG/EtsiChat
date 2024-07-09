import socket
import threading
import serverGui
import sys

maxClients = 5
port = 13121 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

clients = []
usernames = []
handleFlag = True
receiveFlag = True

def broadcast(message):
    for client in clients:
        try:
            client.send(message)
        except:
            pass

def handle(client):
    global handleFlag
    while handleFlag:
        try:
            client.settimeout(1.0)
            message = client.recv(1024)
            if not handleFlag:
                break
            broadcastMsg = usernames[clients.index(client)] + ": " + message.decode('ascii')
            broadcast(broadcastMsg.encode('ascii'))
        except socket.timeout:
            continue
        except:
            if not handleFlag:
                break
            index = clients.index(client)
            clients.remove(client)
            client.close()
            username = usernames[index]
            broadcast(f'{username} left the chat'.encode('ascii'))
            usernames.remove(username)
            break

def receive():
    global receiveFlag
    while receiveFlag:
        try:
            server.settimeout(1.0)
            client, address = server.accept()
        except socket.timeout:
            continue
        except:
            if not receiveFlag:
                break
            continue

        client.send('GET_USERNAME'.encode('ascii'))
        username = client.recv(1024).decode('ascii')
        usernames.append(username)
        clients.append(client)

        serverGui.Console.append(f"User '{username}' connected from {str(address)}")
        client.send("Connected to server".encode('ascii'))
        broadcast(f'{username} has joined chat'.encode('ascii'))

        handle_thread = threading.Thread(target=handle, args=(client,))
        handle_thread.start()

def startServer():
    host = socket.gethostbyname(socket.gethostname()) 
    global receive_thread
    server.bind((host, port))
    server.listen(maxClients)
    serverGui.Console.append(f'Server listening on {host}:{port}')
    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

def stopServer():
    global receiveFlag, handleFlag
    receiveFlag = False
    handleFlag = False
    broadcast('SERVER_STOPPED'.encode('ascii'))
    # Close the server socket to unblock accept call
    server.close()
    # Close all client sockets to unblock recv calls
    for client in clients:
        client.close()
    # Wait for receive_thread to terminate
    '''
    if receive_thread and receive_thread.is_alive():
        receive_thread.join()
    '''
    serverGui.Console.append('Server Stopped!')

# Ensure the receive_thread is defined globally
receive_thread = None
