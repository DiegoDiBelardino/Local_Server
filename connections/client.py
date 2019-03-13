import threading

def recv_str(sock):
    data = sock.recv(1024)
    print(data)

def download(sock,str=True):
    """
    scarica dati e li scrive in un file
    :param sock:connessione
    :return:
    """
    if str:
        th_recv = threading.Thread(target=recv_str, args=(sock,))
    th_recv.start()

