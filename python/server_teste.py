from capsule import Capsule
from remotes import Teste
import uuid
import time


def main():

    capsule = Capsule("127.0.0.1", 5000)
    # reset Name Service if necessary
    # capsule.resetNS()
    teste = Teste()

    capsule.registerRemoteObject(uuid.uuid1(), "Teste", teste, "127.0.0.1", 5000)

    while True:
        time.sleep(1)

if __name__ == '__main__':
    main()