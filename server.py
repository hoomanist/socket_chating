import socket
print("*** server is listening")
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(("0.0.0.0", 8001))
serversocket.listen(1)
conn, addr = serversocket.accept()
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
printer = f"{addr[0]} said {data.decode()}"
print(printer)
