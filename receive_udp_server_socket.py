'''
    Esam jaafar
    2023/10/11
    ICS 344 - Information Security - Network Security Basics
    
'''
    
    
import socket

def create_socket(ip, port):
    socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket.bind((ip, port))
    return socket

def receive_data(socket, buffer_size=1024):
    data, addr = socket.recvfrom(buffer_size)
    print(f"Received data: {data.decode('utf-8')} from {addr}")

def main():
    ip = '127.0.0.1'
    port = 9090
    socket = create_socket(ip, port)
    
    while True:
        receive_data(socket)

if __name__ == "__main__":
    main()
