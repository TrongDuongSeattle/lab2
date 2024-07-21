import socket
import sys


def start():
    hostname = sys.argv[1]
    fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    fd.connect(("localhost", 8080))
    while True:
        message = input("> ")
        if message.lower() == "exit":
            fd.sendall(message.encode())
            break
        # message = message + "from client " +sys.argv[1]
        fd.sendall(message.encode())
        print("message sent")

        data = fd.recv(1024)
        # conn, addr = fd.accept()
        print(f"{data.decode()} -> server received")
        # data = fd.recv(1024)
        # print(f"{data.decode()} -> client received")
    print("closing connection")
    fd.close()


start()
