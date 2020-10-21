import socket 
import sys

TCP_IP = '127.0.0.1'
TCP_PORT = 8090 #Reserve a Port
BUFFER_SIZE = 1024
MESSAGE_TO_SERVER = "Hello, World!"

try:
	#Create an AF_INET (IPv4), STREAM socket (ICP)
	tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
except socket.error: print ("Error occurred while creating socket! Error code:" + str(e[0]) + ", Error message: " + e[1])



tcp_socket.connect((TCP_IP, TCP_PORT))


try:
	#Sending Message
	tcp_socket.send(MESSAGE_TO_SERVER) 
except socket.error: print ("Error occurred while sending data to server. Error code: " + str(e[0]) + ", Error message: " + e[1])


print("Message sent successfully")

#Recieve the response from the server
data = tcp_socket.recv(BUFFER_SIZE)
tcp_socket.close() #Close the Socket when done
print ("Response from the server: ", data)
