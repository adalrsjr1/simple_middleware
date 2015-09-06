import socket
import threading
import sys
from pprint import pprint

class ClientRequestHandler:
    _BUFF_SIZE = 1024

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, host, port):
        server_address = (host, port)
        self.sock.connect(server_address)

    def send(self, message):
        try:
            self.sock.sendall(message)

            amount_rec = 0
            data = ''
            while data[-1:] != '}' or amount_rec < self._BUFF_SIZE :
                data += self.sock.recv(self._BUFF_SIZE)
                amount_rec += len(data)
        finally:
            print >>sys.stderr, 'closing socket'
            self.sock.close()

        return data

def main():
    port_num = 5000 
    c = ClientRequestHandler()
    c.connect('127.0.0.1',port_num)
    c.send('hello world!')

if __name__ == "__main__":
    main()