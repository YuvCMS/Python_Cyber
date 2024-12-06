import socket

# Server configuration
HOST = '127.0.0.1'
PORT = 9000
PASSWORD = "mypassword"  # Replace with your desired password

# Create the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Server is running on {HOST}:{PORT} and waiting for a connection...")

# Accept client connection
client_socket, client_address = server_socket.accept()
print(f"Connection received from {client_address}")

try:
    # Request password from client
    client_socket.sendall(b"SERVER>> Please provide the password: ")
    received_password = client_socket.recv(1024).decode().strip()

    if received_password != PASSWORD:
        client_socket.sendall(b"SERVER>> Access denied")
        print("Access denied: Incorrect password")
        client_socket.close()
    else:
        client_socket.sendall(b"SERVER>> Access granted. You can now chat with the server.\nType 'end' to disconnect.")
        print("Access granted: Client authenticated")

        # Chat loop
        while True:
            client_message = client_socket.recv(1024).decode().strip()
            if client_message.lower() == "end":
                print("Client ended the connection.")
                client_socket.sendall(b"SERVER>> Connection closed")
                break

            print(f"CLIENT>> {client_message}")
            server_message = input("Enter a message for the client: ")
            client_socket.sendall(f"SERVER>> {server_message}".encode())
finally:
    client_socket.close()
    server_socket.close()
