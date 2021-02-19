
import socket  
import sys  
import os  

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.settimeout(5)
s.connect_ex(('62.171.151.158',443)) 


byte = str.encode("Server:\r\n")
s.send(byte)
banner = s.recv(1024)
print(banner)