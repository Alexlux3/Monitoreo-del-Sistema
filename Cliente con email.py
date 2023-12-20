import socket

def main():
    host = "192.168.100.118"  # Reemplaza con la dirección IP del servidor
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        client_socket.sendall(b"memory_usage")
        data = client_socket.recv(1024).decode("utf-8")

        print(data)

if __name__ == "__main__":
    main()
