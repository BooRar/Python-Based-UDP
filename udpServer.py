#!/usr/bin/env python3
import socket

localIP = "10.0.0.5"
localPort = 2001
bufferSize = 1024


msgFromServer = "hello udp client !!"
bytesToSend = str.encode(msgFromServer)
msgFromServer1 = "Just Catching up here"
bytesToSend1 = str.encode(msgFromServer1)
msgFromServer2 = "Lives in a brown brick house"
bytesToSend2 = str.encode(msgFromServer2)


# create Datagram socket

UDPServerSocket = socket.socket(family=socket.AF_INET, type= socket.SOCK_DGRAM)

# bind to address and ip

UDPServerSocket.bind((localIP,localPort))

print("UDP server is up and listening ")

# listen for incomming dstagrams 

while(True):
 bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
 message = bytesAddressPair[0]
 address = bytesAddressPair[1]
 clientMSG =  "message from client : {}".format(message)
 clientIP = "client IP Address : {}".format(address)

 print(clientMSG)
 print(clientIP)

 #sending a reply to client
 UDPServerSocket.sendto(bytesToSend, address)
 UDPServerSocket.sendto(bytesToSend1, address)
 UDPServerSocket.sendto(bytesToSend2, address)

