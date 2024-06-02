import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  # MEDIUM , PROTOCOL 

# ip_address = "192.168.1.7"
ip_address = "127.0.0.1"

port_number = 2525

my_address = (ip_address,port_number)
s.bind(my_address)

while True:
    data = s.recvfrom(100)
    message = data [0]
    message = message.decode("ascii")  
    file_name , message = message.split("::",1)
    with open(file_name,'a+') as f:
        f.write(message)
    