from capsule import Capsule

def main():
    capsule = Capsule("127.0.0.1", 5001)

    print capsule.invoke("Teste", "method", [2,5]).result

if __name__ == '__main__':
    main()