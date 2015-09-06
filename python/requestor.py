from client import ClientRequestHandler
from marshaller import Marshaller
from marshaller import Message
from nameservice import NameService
from nameservice import IRef

class Requestor:

    def __init__(self, m, c):
        self.marshaller = m
        self.client = c
        self.ns = NameService()

    def invoke(self, obj, method, args):
        iRef = self.ns.lookupName(obj)[0]
        return self.invokeByAddr(iRef.host, iRef.port, iRef.name, method, args)

    def invokeByAddr(self, host, port, obj, method, args):
        msg = Message(obj, method, args)

        json = self.marshaller.encode(msg)

        self.client.connect(host, port)

        response = self.client.send(json)

        result = self.marshaller.decode(response)
        return result

def main():
    m = Marshaller()
    c = ClientRequestHandler()

    r = Requestor(m, c)

    response = r.invoke("obj", "method2", [1,2,3])
    print response.result

if __name__ == "__main__":
    main()