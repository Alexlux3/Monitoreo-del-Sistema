import socket
import psutil
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import threading

# Configuración de correo electrónico
email_address = "alexdari65@gmail.com"
email_password = "gaap vibb kvll eiud"
recipient_email = "kleberfabritxzio@hotmail.com"

def send_email_notification(subject, body):
    # Configurar conexión SMTP
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Crear objeto MIMEMultipart
    message = MIMEMultipart()
    message["From"] = email_address
    message["To"] = recipient_email
    message["Subject"] = subject

    # Adjuntar cuerpo del mensaje
    message.attach(MIMEText(body, "plain"))

    # Iniciar conexión SMTP
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(email_address, email_password)
        server.sendmail(email_address, recipient_email, message.as_string())

def monitor_memory():
    while True:
        memory = psutil.virtual_memory()
        if memory.percent > 40:
            send_email_notification("Uso de memoria alto", "El uso de memoria es superior al 40%.")
        # Dormir durante 5 minutos antes de verificar nuevamente
        psutil.time.sleep(300)

def main():
    host = "192.168.100.18"
    port = 12345

    # Iniciar hilo para monitorear la memoria
    memory_thread = threading.Thread(target=monitor_memory)
    memory_thread.start()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()

        print(f"Server listening on {host}:{port}")

        while True:
            client_socket, addr = server_socket.accept()
            with client_socket:
                print(f"Connection from {addr}")
                data = client_socket.recv(1024)
                
                if data == b"memory_performance":
                    response = f"Memory Usage Percentage: {psutil.virtual_memory().percent}%"
                else:
                    response = "Invalid request"

                client_socket.sendall(response.encode("utf-8"))

if __name__ == "__main__":
    main()
