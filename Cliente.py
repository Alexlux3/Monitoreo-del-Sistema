import psutil
import socket
import tkinter as tk
from tkinter import ttk

def show_cpu_frequency(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(b"cpu_frequency")
        data = s.recv(1024).decode("utf-8")
    show_result_window(data)

def memory_performance(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(b"memory_performance")
        data = s.recv(1024).decode("utf-8")
    show_result_window(data)

def storage_performance(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(b"storage_performance")
        data = s.recv(1024).decode("utf-8")
    show_result_window(data)

def network_usage(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(b"network_usage")
        data = s.recv(1024).decode("utf-8")
    show_result_window(data)

def end_program():
    root.destroy()

def show_result_window(text):
    result_window = tk.Toplevel(root)
    result_window.title("Result")
    result_label = tk.Label(result_window, text=text, wraplength=400, justify="left")
    result_label.pack(padx=10, pady=10)

def update_information():
    option = menu_combobox.get()
    host = ip_entry.get()
    port = int(port_entry.get())

    if option == "Show CPU Frequency":
        show_cpu_frequency(host, port)
    elif option == "Memory Performance":
        memory_performance(host, port)
    elif option == "Storage Performance":
        storage_performance(host, port)
    elif option == "Network Usage":
        network_usage(host, port)
    elif option == "End Program":
        end_program()

# Create the main window
root = tk.Tk()
root.title("Remote System Information")

# Create and configure widgets
menu_label = ttk.Label(root, text="Select an option:")
menu_label.grid(row=0, column=0, pady=10)

menu_options = [
    "Show CPU Frequency",
    "Memory Performance",
    "Storage Performance",
    "Network Usage",
    "End Program"
]

menu_combobox = ttk.Combobox(
    root,
    values=menu_options,
    state="readonly"
)
menu_combobox.grid(row=0, column=1, padx=10, pady=10)

ip_label = ttk.Label(root, text="Enter IP:")
ip_label.grid(row=1, column=0, pady=10)

ip_entry = ttk.Entry(root)
ip_entry.grid(row=1, column=1, padx=10, pady=10)

port_label = ttk.Label(root, text="Enter Port:")
port_label.grid(row=2, column=0, pady=10)

port_entry = ttk.Entry(root)
port_entry.grid(row=2, column=1, padx=10, pady=10)

update_button = ttk.Button(root, text="Update", command=update_information)
update_button.grid(row=3, column=0, columnspan=2, pady=10)

# Start the main loop
root.mainloop()
