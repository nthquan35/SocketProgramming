# Import socket module
from socket import *
import sys # In order to terminate the program

FLAG = False  # this is a flag variable for checking quit

# function for receiving message from client
def recv_from_client(conn):
	global FLAG
	try:
		# Receives the request message from the client
		message = conn.recv(1024).decode()
		# if 'q' is received from the client the server quits
		if message == 'q':
			conn.send('q'.encode())
			print('Closing connection')
			conn.close()
			FLAG = True
		print('Message Received: ' + message)
	except:
		conn.close()


# function for receiving message from client
def send_to_client(conn):
	global FLAG
	try:
		send_msg = input('Type Message: ')
		# the server can provide 'q' as an input if it wish to quit
		if send_msg == 'q':
			conn.send('q'.encode())
			print('Closing connection')
			conn.close()
			FLAG = True
		conn.send(send_msg.encode())
	except:
		conn.close()


# this is main function
def main():
	global FLAG

	# TODO (1) - define HOST name, this would be an IP address or 'localhost' (1 line)
	HOST = '127.0.0.1'
	# TODO (2) - define PORT number (1 line) (Google, what should be a valid port number)
	# make sure the ports are not used for any other application
	serverPort = 65432

	# Create a TCP server socket
	#(AF_INET is used for IPv4 protocols)
	#(SOCK_STREAM is used for TCP)
	# TODO (3) - CREATE a socket for IPv4 TCP connection (1 line)
	serverSocket = socket(AF_INET,SOCK_STREAM)

	# Bind the socket to server address and server port
	# TODO (4) - bind the socket for HOSR and serverPort (1 line)
	serverSocket.bind((HOST,serverPort))

	# Listen to at most 1 connection at a time
	# TODO (5) - listen and wait for request from client (1 line)
	serverSocket.listen(1)

	# Server should be up and running and listening to the incoming connections
	print('The chat server is ready to connect to a chat client')
	# TODO (6) - accept any connection request from a client (1 line)
	connectionSocket, addr = serverSocket.accept()
	print('Server is connected with a chat client\n')

	# This is the loop for chating, the connection is already made with the
	# client now the server and client will be able to chat with each other
	while True:
		# call the receive function
		recv_from_client(connectionSocket)
		# this condition checks if anyone has pressed 'q' or not
		if FLAG == True:
			break

		# call the send function
		send_to_client(connectionSocket)
		# this condition checks if anyone has pressed 'q' or not
		if FLAG == True:
			break

	# closing serverScoket before exiting
	serverSocket.close()
	#Terminate the program after sending the corresponding data
	sys.exit()


# This is where the program starts
if __name__ == '__main__':
	main()
