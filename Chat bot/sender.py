import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

Target_IP = "127.0.0.1"
# Target_IP = "192.168.1.25"
port_no = 2525
target_address = (Target_IP,port_no)
quit = True
while quit:
    file_name = input("Please enter the txt file name :")
    with open(str(file_name) , 'r') as f:
        message = f.read()
    
    message_encrypted = str(file_name+"::"+message).encode('ascii')
    s.sendto(message_encrypted,target_address)
    print("Your file has been sent!")
    choice = input("Do you want to quit?")
    if choice =='y' or choice =='Y':
        quit = False
