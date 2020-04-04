import socket

target = input("enter target:  ")
massage = input("enter message: ")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if target == "hooman-m":
    ip = "192.168.1.3"
elif target == "laptop":
    ip="192.168.1.4"
elif target == "air":
    ip = "192.168.1.7"
message = massage.encode()
sock.connect((ip, 8001))
sock.send(message)
