import socket
import threading


def accepting(socket):
    conn, addr = socket.accept()
    print(conn,addr)


def hosting(socket,port=30000):
    """
    apre una porta sull'uscita n "port"
    :param socket: il socket
    :param port: numero porta
    :return:
    """
    socket.bind(('', port))
    socket.listen(1)
    conn,addr = accepting(socket)
    return conn,addr

def recv(conn,printed=True):
    data = conn.recv(1024)
    if printed:
        print(data)

def download(conn):
    """
    scarica dati e li scrive in un file
    :param conn:
    :return:
    """
    th_recv = threading.Thread(target=recv,args=(conn,))
    while True:
        th_recv.start()

