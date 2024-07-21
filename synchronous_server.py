import socket

'''
- 3 clients send request to the serve

per python doc
The preferred way to use a Lock is an async with statement:

    lock = asyncio.Lock()

    # ... later
    async with lock:
        # access shared state

which is equivalent to:

    lock = asyncio.Lock()

    # ... later
    await lock.acquire()
    try:
        # access shared state
    finally:
        lock.release()
        
        
Synchronous means blocking
'''


def start():
    while True:
        fd = socket. socket(socket.AF_INET, socket.SOCK_STREAM)
        fd.bind(('localhost', 8080))
        #  Enable a server to accept connections.
        #  number is amount clients we can queue up before refusing
        fd.listen(3)
        print("waiting for the incoming client...")
        #  while True:
        while True:
            conn, addr = fd.accept()
            print(f"connection form {addr}")
            data = conn.recv(1024)
            if data:
                print(f"{addr}: {data.decode()}")
                bye_message = "bye from server"
                conn.sendall(bye_message.encode())
        fd.close()


start()
