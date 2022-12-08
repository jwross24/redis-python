import socket


def main():
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    conn, _ = server_socket.accept() # wait for client

    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(b"+PONG\r\n")


if __name__ == "__main__":
    main()
