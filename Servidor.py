import socket
import psutil

def get_cpu_frequency():
    return f"CPU Frequency: {psutil.cpu_freq().current} MHz"

def get_memory_performance():
    memory = psutil.virtual_memory()
    return (
        f"Memory Performance:\n"
        f"Total: {memory.total / (1024 ** 3):.2f} GB\n"
        f"Available: {memory.available / (1024 ** 3):.2f} GB\n"
        f"Usage Percentage: {memory.percent}%"
    )

def get_storage_performance():
    storage = psutil.disk_usage('/')
    return (
        f"Storage Performance:\n"
        f"Total: {storage.total / (1024 ** 3):.2f} GB\n"
        f"Used: {storage.used / (1024 ** 3):.2f} GB\n"
        f"Usage Percentage: {storage.percent}%"
    )

def get_network_usage():
    network_stats = psutil.net_io_counters(pernic=True)
    result = "Network Usage:\n"
    for interface, stats in network_stats.items():
        result += (
            f"Interface: {interface}\n"
            f"Bytes sent: {stats.bytes_sent / (1024 ** 2):.2f} MB\n"
            f"Bytes received: {stats.bytes_recv / (1024 ** 2):.2f} MB\n\n"
        )
    return result

def main():
    host = "192.168.100.177"
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()

        print(f"Server listening on {host}:{port}")

        while True:
            client_socket, addr = server_socket.accept()
            with client_socket:
                print(f"Connection from {addr}")
                data = client_socket.recv(1024)
                
                if data == b"cpu_frequency":
                    response = get_cpu_frequency()
                elif data == b"memory_performance":
                    response = get_memory_performance()
                elif data == b"storage_performance":
                    response = get_storage_performance()
                elif data == b"network_usage":
                    response = get_network_usage()
                else:
                    response = "Invalid request"

                client_socket.sendall(response.encode("utf-8"))

if _name_ == "_main_":
    main()
