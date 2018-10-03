#Author: Yost
#Team BPWY

from socket import *

#client calls into server to establish connection
def serverConnect(IPaddress):
    #setup UDP connection and send in password
    s=socket(AF_INET,SOCK_DGRAM)
    s.sendto("hello server",('IPaddress',5000))
    #get message from server telling which port to use for TCP
    portinfo=s.recvfrom(1024)
    port = int(getport[0])
    #setup TCP connection on assigned port
    s=socket()
    s.connect(('IPaddress',port))
	
#client receives info from server and then replies
def recvSend(data):
#get message from server
    message=s.recv(1024)
#send data to server
    s.send(data)
    return message
	
def closeSocket():
    s.close()