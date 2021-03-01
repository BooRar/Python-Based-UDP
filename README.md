# Python-Based-UDP
Simple UDP client and server

## UDP Overview:
UDP is the abbreviation of User Datagram Protocol. UDP makes use of Internet Protocol of the TCP/IP suit. In communications using UDP, a client program sends a message packet to a destination server wherein the destination server also runs on UDP.

![alt text](https://pythontic.com/udp-client-server-overview.png)

## Properties of UDP:
The UDP does not provide guaranteed delivery of message packets. If for some issue in a network if a packet is lost it could be lost forever.
Since there is no guarantee of assured delivery of messages, UDP is considered an unreliable protocol.
The underlying mechanisms that implement UDP involve no connection-based communication. There is no streaming of data between a UDP server or and an UDP Client.
An UDP client can send "n" number of distinct packets to an UDP server and it could also receive "n" number of distinct packets as replies from the UDP server.
Since UDP is connectionless protocol the overhead involved in UDP is less compared to a connection based protocol like TCP.

![alt text](https://pythontic.com/udp-client-server.png)

Graphics courtesy of [pythontic.com](https://pythontic.com/)
