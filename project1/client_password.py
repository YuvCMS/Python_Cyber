import socket

# Server configuration
HOST = '127.0.0.1'
PORT = 9000

# Connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

try:
    # Receive initial message from server
    while True:
        server_message = client_socket.recv(1024).decode().strip()
        print(server_message)

        if "Please provide the password" in server_message:
            password = input("Enter password: ")
            client_socket.sendall(password.encode())
        elif "Access denied" in server_message:
            print("Exiting due to incorrect password.")
            break
        elif "Access granted" in server_message:
            # Chat loop
            while True:
                message_to_server = input("Enter a message for the server (type 'end' to disconnect): ")
                client_socket.sendall(message_to_server.encode())

                if message_to_server.lower() == "end":
                    print("Disconnected from server.")
                    break

                server_reply = client_socket.recv(1024).decode().strip()
                print(server_reply)
            break
finally:
    client_socket.close()
