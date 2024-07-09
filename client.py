import socket
import threading
import clientGui

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
recieveFlag = True

def connectToServer(host, port):
    client.connect((host, int(port)))
    receive_thread = threading.Thread(target=recieve)
    receive_thread.start()

    #write_thread = threading.Thread(target=write)
    #write_thread.start()

def recieve():
    while recieveFlag:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'GET_USERNAME':
                client.send(username.encode('ascii'))
            elif message == 'SERVER_STOPPED':
                print('Server Closed')
                clientGui.ChatBox.append('Server Disconnected')
                break
            else:
                print(message)
                clientGui.ChatBox.append(message)
        except:
            print("An error occured!")
            client.close()
            break

def sendMessage():
    client.send(clientGui.MessageBox.toPlainText().encode('ascii'))
