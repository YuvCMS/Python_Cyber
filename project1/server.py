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

client, addr = s.accept()

print(f'Connection receive from {addr}')
'''
while True : 
    data = input('Enter a msg')
    client.sendall(str.encode(data))  
    msg = client.recv(1024).decode()
    if not msg :
        break
    print(msg) 
'''
client.close()
