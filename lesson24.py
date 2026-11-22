import socket

HOST = "127.0.0.1"
PORT = 5060

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()
    print("სერვერი ელოდება კლიენტს...")

    conn, addr = server.accept()
    with conn:
        data = conn.recv(1024).decode("utf-8")
        print("მივიღეთ:", data)
        conn.sendall(data.upper().encode("utf-8"))

print("სერვერი დასრულდა")


import socket

HOST = "127.0.0.1"
PORT = 5060

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    client.sendall("hello socket".encode("utf-8"))
    response = client.recv(1024).decode("utf-8")
    print("პასუხი:", response)