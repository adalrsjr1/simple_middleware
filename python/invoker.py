from marshaller import Marshaller
from marshaller import Message
from server import ServerRequestHandler

class Invoker:
    localRep = {}
    def __init__(self, m):
        self.marshaller = m

    def addServer(self, s):
        self.server = s;
        s.listen()

    def register(self, id, name, obj):
        __registerObj(name, obj)
        __registerIdObj(id, obj)

    def __inner_register(self, key, value):
        if not localRep.has_hey(key):
            localRep[key] = value

    def __registerObj(self, name, obj):
        self.__register(name, obj)

    def __registerIdObj(self, id, obj):
        self.__register(id, obj)      

    def forward(self, message):
        msg = self.marshaller.decode(message)
        msg.target_obj = None
        msg.method = None
        msg.args = None
        msg.result = None
        #obj = localRep[msg.target_obj]

        #result = getattr(obj, message.method, message.args)
        
        
        json = self.marshaller.encode(msg)
        print "json::: " + json
        
        return json

def main():
    
    m = Marshaller()
    i = Invoker(m)
    s = ServerRequestHandler('',5000, i)
    i.addServer(s);

if __name__ == '__main__':
    main()