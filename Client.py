import socket
def client_program():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Enter IP address of target: ")
    host =input()
    port = 5000
    client.connect((host, port))
    message = input(" Enter command: ")
    while message.lower().strip() != 'exit':
        client.send(message.encode())
        data = client.recv(1024).decode()
        print(data)
        message = input(" $ ")
    client.close()

if __name__ == '__main__':
    client_program()

