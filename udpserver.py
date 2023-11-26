from socket import *
server_port = 69
buffer_size = 512
server_socket = socket(AF_INET,SOCK_DGRAM)
server_socket.bind(('',server_port))
print('The Server is ready to receive')

while True:
	try:

		file_size = b""
		while len(file_size) < 8:
			more_size = server_socket.recv(8 - len(file_size))
			if not more_size:
				raise Exception("File shorter than expected")
			file_size += more_size

		file_size = int.from_bytes(file_size, 'big')

		packet = b""
		while len(packet) < file_size:
			buffer = server_socket.recv(file_size - len(packet))
			if not buffer:
				raise Exception("File transfer ended unexpectedly")
			packet += buffer
			
		print("Please enter a name for the received file (include extension): ")
		fname = input()
		with open(fname, 'wb') as f:
			f.write(packet)
		
	except:
		'connection was closed by remote host'
