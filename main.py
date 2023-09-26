import socket


def main():
    host = "0.0.0.0"
    port = 8000

    # 创建一个通用的套接字，同时监听TCP和UDP
    # create tcp and upd sockets to listen both TCP and UDP
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.bind((host, port))
    tcp_socket.listen(5)

    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind((host, port))

    print("Listening for TCP and UDP connections on {}:{}".format(host, port))

    while True:
        # 尝试连接TCP
        # try to connect TCP
        try:
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
        except socket.timeout:
            pass
        except Exception as e:
            print("Error handling TCP connection:", e)

        # 尝试连接UDP
        # UDP is not connection-oriented, so it doesn't need connection
        try:
            # number is used to calculate how many times server get messages from clients
            # if you want to make the test longer and preciser, you should think about the number
            number = 0
            while True:
                data, addr = udp_socket.recvfrom(1024)
                print("Received UDP data from {}: {}".format(addr, data.decode()))
                response = b'Hello, client!'
                udp_socket.sendto(response, addr)
                number += 1
                if number >= 10:
                    break
        except socket.timeout:
            pass
        except Exception as e:
            print("Error receiving UDP data:", e)


if __name__ == "__main__":
    main()
