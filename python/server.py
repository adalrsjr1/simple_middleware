import socket
import threading
import sys

class ServerRequestHandler:

    def __init__(self, host, port, invoker):
        self.lock = threading.Lock()

        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        self.invoker = invoker


    def listen(self):
        self.sock.listen(5)
        while True:
            try:
                client, address = self.sock.accept()
                client.settimeout(60)
                threading.Thread(target = self.listenToClient, args = (client, address)).start()
            except (KeyboardInterrupt, SystemExit):
                self.sock.close()
                sys.exit(0)
        

    def listenToClient(self, client, address):
        size = 1024
        while True:
            try:
                data = client.recv(size)
                if data:
                    self.lock.acquire()
                    response = self.invoker.forward(data)
                    self.lock.release()
                    client.send(response)
                else:
                    raise error('Client disconnected')
            except Exception, e:
                client.close()
                return False
            finally:
                client.close()

def main():
    port_num = 5000 
    ServerRequestHandler('',port_num).listen()

if __name__ == "__main__":
    main()