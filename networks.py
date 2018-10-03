#Author: Yost
#Team BPWY

from socket import *

#setup lists for sockets, clients, responses
sockets=[]  #for setupClients(numPlayers)
clients=[]  #for setupClients(numPlayers)
responses=[]  #for sendRecv(data)
	
#get number of player from somewhere...
def setupClients(numPlayers):
#UDP connection to see if players are out there
    s0=socket(AF_INET,SOCK_DGRAM)
    s0.bind(('',5000))
#for each player setup, assign a port to use, and setup a connection
#add client sockets to sockets[] and add client connections to clients[]
    for x in range(1,numPlayers+1):
        ts=socket()  #temporary socket
        sockets.append(ts)  #add to sockets[]
        #print ts
        #print sockets[x-1]
        #print x
        tc ,ta = s0.recvfrom(1024) #what does client have to say?
        while tc != "hello server":  #if client has correct password
            tc ,ta = s0.recvfrom(1024) 
        s0.sendto('{}'.format((5000+x)),ta)  #tells client which port they can use
        sockets[x-1].bind(('',5000+x))  #player 1 gets port 5001, etc.
        sockets[x-1].listen(1)  #looks for client on established port
        #print 'started listening'
        c,a = sockets[x-1].accept()
	    #print ("Player {} is on port {}.".format(x,(5000+x))
        clients.append(c)  #add to clients[]
		
#for each player setup, shoot data to each of them and get a response
def sendRecv(data):
    responses=[]  #dump list
    for x in range(1,numPlayers+1):
        clients[x-1].send(data)
        stuff=clients[x-1].recv(1024)
        responses.append(stuff)  #store responses in responses[x-1]
        return responses
		
def closeSocket():
    for x in range(1,numPlayers+1):
        clients[x-1].close()