import socket

def start():
	#socket creation
	fd = socket. socket(socket.AF_INET, socket.SOCK_STREAM) #ip4 sockstream is for TCP protocol
	#bind to localhost port 8080
	fd.bind(('localhost', 8080))
	fd.listen(1)
	print("waiting for incoming client...")
	#looping allows multiple connections/requests
	#uncomment to accept mult connections
	#while True:
	#accepting connection
	conn, addr = fd.accept()
	print(f"connection from {addr}")

	#receive data, assuming we got something from client
	data = conn.recv(1024)
	if data:
		print(f"{addr}: {data.decode()}")
		#writing back to client

		#conn.sendall(data) # echo back to the received message
		bye_Message = "bye from server"
		conn.sendall(bye_Message.encode())
	
start()
