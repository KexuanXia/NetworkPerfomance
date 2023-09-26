import socket


def udp_listening():
    host = "0.0.0.0"
    port = 8001

    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind((host, port))

    print("Listening for UDP connections on {}:{}".format(host, port))

    while True:
        data, addr = udp_socket.recvfrom(1024)
        print("Received UDP data from {}: {}".format(addr, data.decode()))
        response = b'Hello, client!'
        udp_socket.sendto(response, addr)


if __name__ == "__main__":
    udp_listening()