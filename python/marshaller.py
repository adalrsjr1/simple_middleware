import json

class Message:
    def __init__(self, target_obj, method, args, result=None):
        self.target_obj = target_obj
        self.method = method
        self.args = args
        self.result = result


class Marshaller():

    def encode(self, obj):
        if isinstance(obj, Message):
            return json.dumps({"target_obj":obj.target_obj, "target_method":obj.method, "args":obj.args, "result":obj.result})
        return json.JSONEncoder.default(self, obj)

    def decode(self, obj):   
        msg = json.loads(obj)
        n_msg = Message(msg['target_obj'], msg['target_method'], msg['args'], msg['result'])
        return n_msg
    

def main():
    msg = Message("objeto1", "method2", [1,3.14,"oi",[1,2,3], {"a":1, "b":[1,2]}])

    m = Marshaller()
    x = m.encode(msg)
    d = m.decode(x)
    print d["args"]

if __name__ == "__main__":
    main()