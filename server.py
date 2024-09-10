import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.bind(('localhost', 3030))
socket.listen(1)

conn, addr = socket.accept()

while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.send(data)
    print(data.decode('utf-8'))
conn.close()
