import socket
import sys

target = sys.argv[1]

file = open("engine/tools/getIps/all-subdomains.txt")
dlist = file.read().splitlines()

for line in dlist:
    try:
        ip = socket.gethostbyname(line)
        print(ip)
    except:
        pass