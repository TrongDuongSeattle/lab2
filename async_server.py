import socket
import threading
'''

Lock is an
async with statement:
    lock = asyncio.Lock()

    # ... later
    async with lock:
# access shared state

which is equivalent
to:

lock = asyncio.Lock()

# ... later
await lock.acquire()
try:
# access shared state
finally:
    lock.release()
'''


# accept client message


def get_message(client_socket, client_address):
    lock = threading.Lock()
    data = client_socket.recv(1024)
    with lock:
        if data:
            print(f"{client_address}: {data.decode()}")
            bye_message = "bye from server"
            client_socket.sendall(bye_message.encode())


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
    fd.close()


start()
