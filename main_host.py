import socket
import connections.host as host

#HOSTONE
user_name = input("INSERISCI IL TUO USERNAME: ")

#inizializzazione e connessione
sock = socket.socket()
port = 30000


#setup connessione
print("SETUP CONNESSIONE")
conn,addr = host.hosting(sock)   #porta default = 30000
print("CONNESSIONE RIUSCITA")

host.download(conn)
#switch and other
connected = False


while True:
    inp = input()
    if inp == "close":
        conn.close()
    conn.send(user_name + "say: " + bytes(inp))