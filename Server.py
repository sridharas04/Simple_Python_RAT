import socket
import os
def server_program():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 5000))
    server.listen(1)
    print("Server Started....!")
    while True:
        connection, address = server.accept()
        print('Got connection from', address) 
        data = connection.recv(1024).decode()
        print(data)
        if not data:
            break
        print("from connected user: " + str(data))
        response = os.system( data+">out.txt")
        f = open("out.txt",'r',encoding = 'utf-8')
        data = f.read()
        f.close()
        connection.send(data.encode())
        if(response == 0):
            print("Executed Successfully")
        else:
            print("Command not found")

    connection.close()

if __name__ == '__main__':
    server_program()
