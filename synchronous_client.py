import socket


def start():
    for _ in range(3):
        fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        fd.connect(("localhost", 8080))
        message = "hello from client"
        fd.sendall(message.encode())
        data = fd.recv(1024)
        print(f"server responded: {data.decode()}")
        fd.close()


start()
