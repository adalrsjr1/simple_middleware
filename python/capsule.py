import threading
import time

from marshaller import Marshaller
from marshaller import Message
from server import ServerRequestHandler
from client import ClientRequestHandler
from marshaller import Message
from nameservice import NameService
from nameservice import IRef
from requestor import Requestor
from invoker import Invoker

from pprint import pprint

class Capsule:

    def __init__(self, host, port):

        self.ns = NameService()

        self.marshaller_client = Marshaller()
        self.c = ClientRequestHandler()
        self.requestor = Requestor(self.marshaller_client, self.c)

        self.server = threading.Thread(target = self.createServer, args = (host, port) )

        self.server.daemon = True

        self.server.start()            

    def resetNS(self):
        self.ns.reset()

    def createServer(self, host, port):
        self.marshaller_server = Marshaller()
        self.invoker = Invoker(self.marshaller_server)
        self.s = ServerRequestHandler(host, port, self.invoker)
        self.invoker.addServer(self.s);

    def registerRemoteObject(self, id, name, obj, host, port):
        self.ns.register(id, name, host, port)
        self.invoker.register(id, name, obj)

    def invoke(self, obj, method, args):
        result = self.requestor.invoke(obj, method, args)
        return result

def main():
    c = Capsule("127.0.0.1", 5000)

    print c.invoke("obj", "method2", [1,2,3]).result


    while True:
        time.sleep(1)

if __name__ == '__main__':
    main()