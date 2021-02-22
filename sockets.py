import socket

# Create Socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET is ipv4 
# SOCK_STREAM is TCP
# So this is a tcp/ip connection

#Server code
s.bind( (socket.gethostname(), 1234) )

#queue
s.listen(5)

While True:
	clientsocket, address = s.accept()
	print(f"Connection from {address} has been established") 