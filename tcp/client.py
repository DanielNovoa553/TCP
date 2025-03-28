import socket


def start_client():
    """
    Starts a TCP client that connects to a TCP server on localhost at port 5000.
    Allows the user to send messages and displays server responses.

    - Sends "DISCONNECT" to close the connection and exit.

    Error handling:
    - Captures socket errors and handles connection issues gracefully.

    Usage:
        python client.py
    """
    host = 'localhost'
    port = 5000

    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, port))
        print("Conectado al servidor...")

        while True:
            try:
                message = input("Introduzca un mensaje: ").strip()

                if not message:
                    print("El mensaje no puede estar vacío. Inténtelo nuevamente.")
                    continue

                client.send(message.encode('utf-8'))

                if message == "DESCONEXION":
                    print("Desconectando desde el servidor...")
                    client.close()
                    break

                response = client.recv(1024).decode('utf-8')
                print(f"Respuesta del servidor: {response}")

            except socket.error as e:
                print(f"Socket error: {e}")
                break

    except Exception as e:
        print(f"Error conectando al servidor: {e}")


if __name__ == "__main__":
    start_client()
