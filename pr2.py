import socket
HOST = 'localhost' 
PORT = 8080        

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((HOST, PORT))
print('Connected to {}:{}'.format(HOST, PORT))


while True:
    # Send a message to the server
    message = input('Enter a message: '  )
    client_socket.sendall(message.encode())
        # Receive a response from the server
    data = client_socket.recv(1024).decode()
    print('Received response: {}'.format(data))
# Close the connection
print('Closing connection')
client_socket.close()

