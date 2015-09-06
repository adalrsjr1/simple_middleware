import socket
import threading
import sys

class ClientRequestHandler:

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, host, port):
        server_address = (host, port)
        self.sock.connect(server_address)

    def send(self, message):
        try:
            self.sock.sendall(message)

            amount_rec = 0
            amount_exp = len(message)

            count = 0
            while count <= 1024 and amount_rec < amount_exp :
                data = self.sock.recv(1024)
                amount_rec += len(data)
                count += 1
                #print "%d %d %d" % (amount_rec, amount_exp, count)
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