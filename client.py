import socket
import ssl

HOST = "localhost"
PORT = 5000

context = ssl._create_unverified_context()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn = context.wrap_socket(sock, server_hostname=HOST)

conn.connect((HOST, PORT))

print("Connected to server")

while True:
    msg = input("> ")

    conn.send((msg + "\n").encode())

    if msg == "QUIT":
        break

    data = conn.recv(4096).decode()

    print(data)

conn.close()