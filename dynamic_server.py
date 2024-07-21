import socket
import threading


def get_message(conn, addr):
    print("W I T N E S S  M E \n")
    # lock = threading.Lock()
    connected = True;
    while connected:
        data = conn.recv(1024)
        # with lock: //adding or removing client
        if data:
            if data.decode().lower() == "exit":
                connected = False
                print(f"{addr} disconnected")
                break
            print(f"{addr}: {data.decode()}")
            bye_message = data.decode()
            conn.sendall(bye_message.encode())
    print("closing connection")
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
        print(f"[active connections] {threading.active_count() - 1}")
    thread.join()
    # need to close
    print("hang?")
    fd.close()


start()
