import socket


def start():
	fd = socket. socket(socket.AF_INET, socket.SOCK_STREAM)
	fd.bind(('localhost', 8080))
	fd.listen(1)
	print("waiting for incoming client...")
	conn, addr = fd.accept()
	print(f"connection from {addr}")

	data = conn.recv(1024)
	if data:
		print(f"{addr}: {data.decode()}")
		bye_Message = "bye from server"
		conn.sendall(bye_Message.encode())


start()
