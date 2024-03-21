import socket

def main():


    HOST = input("Enter server IP: ")
    PORT = int(input("Enter server port: "))


    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
    client_socket.connect((HOST, PORT))
    print(b"Connected to {}",HOST.encode('utf-8'))

    while True:

        message = input("[shell]:> ")
        client_socket.send(bytes(message, 'utf-8'))

   
        response = client_socket.recv(1024).decode('utf-8')
        print("---------------------------------------------------------")
        print(response)
        print("---------------------------------------------------------")

    client_socket.close()

if __name__ == "__main__":
    main()
