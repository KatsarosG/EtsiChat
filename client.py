import socket
import threading

host = 'localhost'
port = 12347

username = 'testClient' 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connectToServer():
    client.connect((host, port))
    receive_thread = threading.Thread(target=recieve)
    receive_thread.start()

    write_thread = threading.Thread(target=write)
    write_thread.start()

def recieve():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'GET_USERNAME':
                client.send(username.encode('ascii'))
            else:
                print(message)
        except:
            print("An error occured!")
            client.close()
            break

def write():
    while True:
        message = f'{username}: {input("")}'
        client.send(message.encode('ascii'))


