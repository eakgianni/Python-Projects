import socket 
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)# the address
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "leave"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM#creates socket
server.bind(ADDR)

def handle_client(conn, addr): # runs for each client (individual connections
    print(f "[NEW CONECTION] {addr} connected.")
    
    connected = True
    while connected:
        msg_length = conn.recv(HEDAR) .decode(FORMAT)
        msg_length = int(msg_length)
        msg = conn.recv(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT)
        print(f "[{addr}] {msg}")
        if smg == DISCONNECT_MESSAGE:
            connected = False


def start():#handle new connections
    
    server.listen
    print(f "[LISTNING] Server is listning on {SERVER}")
    while True:
        conn, addr = server.accept()#when new connection, store info about client
        thread = threading.Thread(target=handle_client, args(conn, addr))#create new thread using handleclient function to target thread and taking the conn and add as arguments
        thread.start#thread is made
        
        print(f "[ACTIVE CONNECTIONS] {threading.activeCount() - 1}") #prints n of threads

print("[STARTING] server is starting...")
start()