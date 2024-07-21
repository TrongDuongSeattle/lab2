import socket
import threading


"""
When messages are written, there is no guarantee that the whole message will make to server
could define length of buffer sent and make sure to read that many bytes
first byte could denote size of buffer and then read until that size. 

would have to flush to make sure everything is also sent

if the whole message isn't sent (or read?) could cause a hang because of blocking
 considered making a list of threads to handle but that takes more learing tand this is late
"""

def get_message(conn, addr):
    # lock = threading.Lock()
    connected = True;
    while connected:
        data = conn.recv(1024)
        # with lock: //adding or removing client
        if data:
            if data.decode().lower() == "exit":
                connected = False
                break
            print(f"{addr}: {data.decode()}")
            echo_message = data.decode()
            conn.sendall(echo_message.encode())
    # ends this thread
    conn.close()


def start():
    fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    fd.bind(('localhost', 8080))
    fd.listen(3)
    print("waiting for the incoming client...")
    while True:
        conn, addr = fd.accept()
        print(f"connection from {addr}")
        thread = threading.Thread(
            target=get_message,
            args=(conn, addr, )
        )
        thread.start()
    thread.join()
    # need to close
    print("hang?")
    fd.close()


start()
