import socket
import time

#Slave - UDP client. It sends messages, recieves echo and compares them.
s = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)

s.connect (('127.0.0.1',50000))

print('Connecting to Master @ 127.0.0.1:50000')

while (True):
    
    data = input()
    data_enc = data.encode()
    s.send(data_enc)
    if data == '-1':
        print('Performing exit...')
        break
    start = time.time()
    print ('Sending data to Master...')
    data_recieved, client = s.recvfrom (16)
    end = time.time()
    if data_recieved != data_enc:
        print ('Message lost, err')
        break
    else:
        print ('Master echoed: ', data_recieved.decode(),
               '. Time Elapsed: ', end-start)

