'''
    Esam jaafar
    2023/10/11
    ICS 344 - Information Security - Network Security Basics
    
'''



import socket

def create_udp_socket():
    return socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def send_udp_data(udp_socket, dest_addr, port, data):
    udp_socket.sendto(data, (dest_addr, port))

def main():
    dest_addr = '127.0.0.1'
    port = 9090
    user_input_data = input("Enter the data to be sent: ")
    data = bytes(user_input_data, 'utf-8') 
    
    udp_socket = create_udp_socket()
    send_udp_data(udp_socket, dest_addr, port, data)

if __name__ == "__main__":
    main()
