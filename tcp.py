import socket


def tcp_listening():
    host = "0.0.0.0"
    port = 8000

    # 创建一个通用的套接字，同时监听TCP
    # create tcp and upd sockets to listen both TCP
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.bind((host, port))
    tcp_socket.listen(5)

    print("Listening for TCP connections on {}:{}".format(host, port))

    while True:
        client_socket, client_addr = tcp_socket.accept()
        print("Accepted TCP connection from {}:{}".format(client_addr[0], client_addr[1]))
        try:
            # if TCP connection has been established, always receive data till connection is aborted
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                print(f"Received: {data.decode('utf-8')}")
                response = "Hello, client!\n".encode('utf-8')
                client_socket.send(response)
        except Exception as e:
            print(f"Error: {e}")
        finally:
            client_socket.close()


if __name__ == "__main__":
    tcp_listening()