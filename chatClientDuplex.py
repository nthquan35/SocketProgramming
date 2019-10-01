from socket import *
import sys
import threading

# function for receiving message from client
def send_to_server(clsock):
    send_msg = input('Type Message: ')
    clsock.sendall(send_msg.encode())
    while True: 
        send_to_server(clsock)

# function for receiving message from server
def recv_from_server(clsock):
    data = clsock.recv(1024).decode()
    if data == 'q':
        print('Closing connection')
        sys.exit()
    print('Message Received: ', data)
    while True:
        recv_from_server(clsock)


# this is main function
def main():
    # TODO (1) - define HOST name, this would be an IP address or 'localhost' (1 line)
    HOST = '127.0.0.1'
    # TODO (2) - define PORT number (1 line) (Google, what should be a valid port number) 
    PORT = 65432

    # Create a TCP client socket
	#(AF_INET is used for IPv4 protocols)
	#(SOCK_STREAM is used for TCP)
    # TODO (3) - CREATE a socket for IPv4 TCP connection (1 line)
    clientSocket = socket(AF_INET,SOCK_STREAM)
    

    # request to connect sent to server defined by HOST and PORT
    # TODO (4) - request a connection to the server (1 line)
    clientSocket.connect((HOST,PORT))
    print('Client is connected to a chat server!\n')

    t1 = threading.Thread(target=send_to_server, args= (clientSocket,))
    t2 = threading.Thread(target=recv_from_server, args= (clientSocket,))
    t1.start()
    t2.start()
    

    #while True:
        # call the function to send message to server
        #send_to_server(clientSocket)
        # call the function to receive message server
        #recv_from_server(clientSocket)

    
# This is where the program starts
if __name__ == '__main__':
    main()
