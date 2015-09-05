from client import ClientRequestHandler
from marshaller import Marshaller
from marshaller import Message


class Requestor:

    def __init__(self, m, c):
        self.marshaller = m
        self.client = c

    def invoke(self, host, port, obj, method, args):
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

    print r.invoke("localhost", 5000, "obj1", "method2", [1,2,3])

if __name__ == "__main__":
    main()