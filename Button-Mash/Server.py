# Python program to implement server side of chat room.
import socket
import select
import sys
import threading
import time

"""The first argument AF_INET is the address domain of the 
socket. This is used when we have an Internet Domain with 
any two hosts The second argument is the type of socket. 
SOCK_STREAM means that data or characters are read in 
a continuous flow."""
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# checks whether sufficient arguments have been provided
if len(sys.argv) != 3:
    print("Correct usage: script, IP address, port number")
    exit()

# takes the first argument from command prompt as IP address
IP_address = str(sys.argv[1])

# takes second argument from command prompt as port number
Port = int(sys.argv[2])

""" 
binds the server to an entered IP address and at the 
specified port number. 
The client must be aware of these parameters 
"""
server.bind((IP_address, Port))

""" 
listens for 100 active connections. This number can be 
increased as per convenience. 
"""
server.listen(100)

list_of_clients = []
playerScore = {}

def clientthread(conn, addr):
    # sends a message to the client whose user object is conn
    while True:
        if(len(list_of_clients)==2):
            countdown()
            timeout = time.time() + 10
            while True:
                if time.time() > timeout:
                    try:
                        message = conn.recv(2048)
                        if message:

                            """prints the message and address of the 
                            user who just sent the message on the server 
                            terminal"""
                            print("<" + addr[0] + "> " + message)

                            playerScore[conn] += 1
                            broadcast(conn)

                        else:
                            """message may have no content if the connection 
                            is broken, in this case we remove the connection"""
                            remove(conn)

                    except:
                        continue
                else:
                    gameover(conn)
        else:
            print("Not enough players")



def countdown():
    server.sendall(b'ready')
    time.sleep(2)
    server.sendall(b'GO!')


def gameover(connection):
    for clients in list_of_clients:
        if clients != connection:
            try:
                clients.send(b'gameover')
            except:
                clients.close()

                # if the link is broken, we remove the client
                remove(clients)
    broadcast(connection)


"""Using the below function, we broadcast the message to all 
clients who's object is not the same as the one sending 
the message """


def broadcast(connection):
    sum = 0
    for player in playerScore:
        sum += playerScore[player]
    message = ''
    for player in playerScore:
        message = message + str((playerScore[player])*100//sum) + ' '
    for clients in list_of_clients:
        if clients != connection:
            try:
                clients.send(message)
            except:
                clients.close()

                # if the link is broken, we remove the client
                remove(clients)


"""The following function simply removes the object 
from the list that was created at the beginning of  
the program"""


def remove(connection):
    #pretend its still here shhhh
    print('Someone Lost Connection')

while True:
    """Accepts a connection request and stores two parameters,  
    conn which is a socket object for that user, and addr  
    which contains the IP address of the client that just  
    connected"""
    conn, addr = server.accept()

    """Maintains a list of clients for ease of broadcasting 
    a message to all available people in the chatroom"""
    list_of_clients.append(conn)
    playerScore[conn] = 0

    # prints the address of the user that just connected
    print(addr[0] + " connected")

    # creates and individual thread for every user
    # that connects
    u = threading.Thread(target=clientthread, args=(conn, addr))
    u.start()

conn.close()
server.close()
