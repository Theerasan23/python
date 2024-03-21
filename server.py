import socket
import threading
import subprocess

clients = []

HOST = "127.0.0.1"
PORT = 2345

def handle_client(client_socket, addr):
    print(f"Accepted connection from {addr}")
    clients.append(client_socket)

    while True:
  
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break

        print(f"* {addr}: {data}")

        command = data.strip()
        try:

            if command == "exit":
                client_socket.close()
                clients.remove(client_socket)
                break
         
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
            client_socket.send(output)
        except subprocess.CalledProcessError as e:
           
            client_socket.send(f"Error executing command: {str(e)}".encode('utf-8'))

        
        for client in clients:
            if client != client_socket:
                try:
                    client.send(bytes(data, 'utf-8'))
                except:
                    
                    clients.remove(client)

   
    client_socket.close()
    print(f"Connection from {addr} closed")

def main():
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    
    server_socket.bind((HOST, PORT))

   
    server_socket.listen(5)
    print("starting on port " + str(PORT))

    while True:
      
        client_socket, addr = server_socket.accept()

       
        client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_thread.start()

if __name__ == "__main__":
    main()
