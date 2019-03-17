import threading

class Engine():
    def __init__(self,conn):
        self.data = None
        self.th_recv = None
        self.conn = conn
        self.path = ""

    def file(self,cmd):
        if cmd == "open":
            self.c_file = open(self.path,"wb")

    def recvu(self,conn, printed=True):
        self.data = conn.recv(1024)
        if printed:
            print(self.data)
        else:
            if "StArT" in self.data:
                self.file("open")
            elif "StOp" in self.data:
                self.file("stop")
            else:
                self.c_file.write(self.data)


    def download_th(self,conn,printed):
        """
        scarica dati e li scrive in un file
        :param conn:
        :return:
        """
        self.th_recv = threading.Thread(target=self.recvu, args=(self.conn,printed,))
        self.th_recv.start()

    def stop_th(self):
        self.th_recv.stop()

    def reset_th(self,printed):
        self.th_recv = threading.Thread(target=self.recvu, args=(self.conn, printed,))
        self.th_recv.start()

class engine_prova():
    def __init__(self):
        self.data = None

    def recvu(self, printed=True):
        while True:
            self.data = "lol2"
            if printed:
                print(self.data)

    def download_th(self,printed):
        """
        scarica dati e li scrive in un file
        :param conn:
        :return:
        """
        th_recv = threading.Thread(target=self.recvu, args=(printed,))
        if printed:
            print("thread start")
            th_recv.start()