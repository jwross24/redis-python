import socket


def main():
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    client_connection, _ = server_socket.accept()

    with client_connection:
        while True:
            data = client_connection.recv(1024)
            if not data:
                break
            client_connection.sendall(b"+PONG\r\n")


if __name__ == "__main__":
    main()
