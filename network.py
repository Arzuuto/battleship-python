import socket
import sys

class Network:
    def __init__(self, host='127.0.0.1', port=8086): #port need to be in the parameter
        self.host = host
        self.port = port
        self.socket = None
        self.client_socket = None
        self.addr = None

    # Host a game
    def start_server(self):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.bind((self.host, self.port))
            self.socket.listen()
            print("Server started, listening on " + str(self.host) + ":" + str(self.port))
            self.client_socket, self.addr = self.socket.accept()
            print("Connection from " + str(self.addr) + " has been established.")
        except Exception as e:
            print("Error starting server: " + str(e))
            sys.exit(84)

    # Connect to a host as a client
    def connect_to_server(self, port):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.host, port))
            print("Connected to server at " + str(self.host) + ":" + str(port))
        except Exception as e:
            print("Error connecting to server: " + str(e))
            sys.exit(84)

    # Send the data to the other player
    def send(self, data):
        try:
            if self.client_socket:
                self.client_socket.sendall(data.encode())
            else:
                self.socket.sendall(data.encode())
        except Exception as e:
            print("Error sending data: " + str(e))
    
    # Receive data throught the socket
    def receive(self):
        if self.client_socket:
            return self.client_socket.recv(1024).decode()
        else:
            return self.socket.recv(1024).decode()

    # Close connection
    def close_connection(self):
        if self.client_socket:
            self.client_socket.close()
        if self.socket:
            self.socket.close()

