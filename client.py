import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.connect(('localhost', 3030))
socket.sendall("Hello world".encode("utf-8"))
data = socket.recv(1024)
socket.close()