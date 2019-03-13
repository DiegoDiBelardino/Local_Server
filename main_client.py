import socket,threading,sys
import connections.client as client
#CLIENTONE

ip_path = "cache files/addresses"
sock = socket.socket()

user_name = input("INSERISCI IL TUO USERNAME: ")
#variables
connected = False
ip = open(ip_path).read()
port = 30000


print("CIAO! L'ip registrato e': %s"%ip)
while True:
    inp = input()
    if not connected:
        if inp == "ip":
            print(ip)
        if inp == "exit":
            sys.exit()
        if inp == "change ip":
            ip = input("inserisci nuovo ip target --> ")
            open(ip_path,"w").write(ip)
        if inp == "connect":
            sock.connect((ip,port))
            print("CONNESSIONE RIUSCITA A %s"%ip)
            client.download(sock)
            connected = True
    else:
        sock.send(user_name + "say: " +bytes(inp))