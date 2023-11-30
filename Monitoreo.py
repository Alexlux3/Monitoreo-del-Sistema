import psutil
import tkinter as tk
from tkinter import ttk

def update_information():
    option = menu_combobox.get()
    if option == "Show CPU Frequency":
        show_cpu_frequency()
    elif option == "Memory Performance":
        memory_performance()
    elif option == "Internal Storage Performance":
        storage_performance()
    elif option == "Network Usage":
        network_usage()
    elif option == "End Program":
        end_program()

def show_cpu_frequency():
    cpu_frequency = psutil.cpu_freq()
    show_result_window(f"CPU Frequency: {cpu_frequency.current} MHz")

def memory_performance():
    memory = psutil.virtual_memory()
    show_result_window(
        f"Memory Performance:\n"
        f"Total: {memory.total / (1024 ** 3):.2f} GB\n"
        f"Available: {memory.available / (1024 ** 3):.2f} GB\n"
        f"Usage Percentage: {memory.percent}%"
    )

def storage_performance():
    storage = psutil.disk_usage('/')
    show_result_window(
        f"Internal Storage Performance:\n"
        f"Total: {storage.total / (1024 ** 3):.2f} GB\n"
        f"Used: {storage.used / (1024 ** 3):.2f} GB\n"
        f"Usage Percentage: {storage.percent}%"
    )

def network_usage():
    network_stats = psutil.net_io_counters(pernic=True)
    result = "Network Usage:\n"
    for interface, stats in network_stats.items():
        result += (
            f"Interface: {interface}\n"
            f"Bytes sent: {stats.bytes_sent / (1024 ** 2):.2f} MB\n"
            f"Bytes received: {stats.bytes_recv / (1024 ** 2):.2f} MB\n\n"
        )
    show_result_window(result)

def end_program():
    root.destroy()

def show_result_window(text):
    result_window = tk.Toplevel(root)
    result_window.title("Result")
    result_label = tk.Label(result_window, text=text, wraplength=400, justify="left")
    result_label.pack(padx=10, pady=10)

# Create the main window
root = tk.Tk()
root.title("System Information")

# Variables
result_text = tk.StringVar()

# Create and configure widgets
menu_label = ttk.Label(root, text="Select an option:")
menu_label.grid(row=0, column=0, pady=10)

menu_options = [
    "Show CPU Frequency",
    "Memory Performance",
    "Internal Storage Performance",
    "Network Usage",
    "End Program"
]

menu_combobox = ttk.Combobox(
    root,
    values=menu_options,
    state="readonly"
)
menu_combobox.grid(row=0, column=1, padx=10, pady=10)

update_button = ttk.Button(root, text="Update", command=update_information)
update_button.grid(row=0, column=2, padx=10, pady=10)

# Start the main loop
root.mainloop()
