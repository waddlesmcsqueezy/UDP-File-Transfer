from socket import *

server_port = 69
buffer_size = 512
server_address = "192.168.50.203"
client_socket = socket(AF_INET, SOCK_DGRAM)
client_socket.connect((server_address, server_port))

print("Enter the target server IP address: ")
print("Enter the name of the file you wish to send: ")

fname = input()
data = open(fname, 'rb').read()
send = [data[i:i + buffer_size] for i in range(0, len(data), buffer_size)]

client_socket.sendall(len(data).to_bytes(8, 'big'))
client_socket.sendall(data)

for string in send:
    client_socket.send(string)

client_socket.close()
