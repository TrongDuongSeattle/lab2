import socket
import sys


def start():
    hostname = sys.argv[1]
    #while True:
    for _ in range(1):
        fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        fd.connect(("localhost", 8080))
        message = "hello from client " + sys.argv[1]
        fd.sendall(message.encode())
        data = fd.recv(1024)
        print(f"server responded: {data.decode()}")
        fd.close()


start()
