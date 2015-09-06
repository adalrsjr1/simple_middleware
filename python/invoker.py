from marshaller import Marshaller
from marshaller import Message
from server import ServerRequestHandler
from remotes import *

class Invoker:
    localRep = {}
    def __init__(self, m):
        print ">>> Invoker"
        self.marshaller = m

    def addServer(self, s):
        self.server = s;
        self.server.listen()

    def register(self, id, name, obj):
        self.__inner_register(name, obj)
        self.__inner_register(id, obj)

    def __inner_register(self, key, value):
        if not key in self.localRep:
            self.localRep[key] = value

    def forward(self, message):
        in_msg = self.marshaller.decode(message)

        obj = self.localRep[in_msg.target_obj]        
        args = in_msg.args
        method = in_msg.method
        
        result = getattr(obj, (method))(*args)
        
        to_json = Message(None, None, None, result)
        out_msg = self.marshaller.encode(to_json)
   

        return out_msg

def main():
    
    m = Marshaller()
    i = Invoker(m)
    s = ServerRequestHandler('',5000, i)
    i.addServer(s);

if __name__ == '__main__':
    main()