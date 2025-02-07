import socket
import time
#Master - UDP Server. It performs echo.
s = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)

s.bind (('127.0.0.1',50000))

print ('Creating socket @ 127.0.0.1:50000')

while (True):

    data, client = s.recvfrom(16)

    if data.decode() == '-1':
        print('Performing exit...')
        break
    else:
        time.sleep(5)
        print ('Echoing ', data.decode(), 
               ' back to: ', client)
        s.sendto(data, client)

