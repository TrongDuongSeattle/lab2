import socket


def start():
    fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #server ip or hostname
    #using own machine for now so matching ip
    fd.connect(("localhost", 8080))
    #q single connection is a different port
    #encode so hackers can't understand if they capture package
    #client writing message to send to server
    message = "hello from client"
    fd.sendall(message.encode())
    #then you have to receive from server side
    data = fd.recv(1024)
    print(f"server responded: {data.decode()}")

    #close connection
    fd.close()


#calling start method
start()
