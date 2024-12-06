import socket 

#socket

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
host = '127.0.0.1'
port = 9000
#bind

s.bind((host, port))

#listen 

s.listen()

#accept 

conn , addr = s.accept()
print(f'connection receive from {addr}')
