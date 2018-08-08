#! /usr/bin/python
import socket

for i in range(201,209):
  ip = '52.58.xx.'+ str(i)
  name, alias, addresslist = socket.gethostbyaddr(ip)
  print(ip + " ptr " + name)

for i in range(0,128):
  ip = '52.58.xx.'+ str(i)
  name, alias, addresslist = socket.gethostbyaddr(ip)
  print(ip + " ptr " + name)
