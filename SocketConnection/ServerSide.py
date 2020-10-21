import socket
import sys

TCP_IP = '127.0.0.1'
TCP_PORT = 8090 #Reserve a Port
BUFFER_SIZE = 1024

try:
	#Create an AF_INET (IPv4), STREAM socket (ICP)
	tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
except socket.error: print ("Error occurred while creating socket! Error code:" + str(e[0]) + ", Error message: " + e[1])


tcp_socket.bind((TCP_IP, TCP_PORT))
#Listen for incoming connections (max queued connections: 2)
tcp_socket.listen(2)
print ('Listening...')

#Waits for incoming connections (blocking call)
connection, address = tcp_socket.accept()
print ("Connected with:", address)

data = connection.recv(BUFFER_SIZE)
print ("Message from client: ", data)

#respose for the message from client
connection.sendall("Thanks for connecting") 
connection.close()

