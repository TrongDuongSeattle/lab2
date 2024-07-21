import socket
import threading

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
lock = threading.Lock()

def start():
    while True:
        fd = socket. socket(socket.AF_INET, socket.SOCK_STREAM)
        fd.bind(('localhost', 8080))
        fd.listen(3)
        print("waiting for the incoming client...")
        while True:
            #this is blocking, so technically this is synchronous
            conn, addr = fd.accept()
            print(f"connection form {addr}")
            data = conn.recv(1024)
            if data:
                print(f"{addr}: {data.decode()}")
                bye_message = "bye from server"
                conn.sendall(bye_message.encode())
        fd.close()


start()
