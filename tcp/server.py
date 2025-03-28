import socket


def start_server():
    """
    Starts a TCP server on localhost at port 5000.
    Handles client connections and responds to messages.

    - If "DISCONNECT" is received, the server closes the connection with that client
      and remains available for new connections.
    - Any other message is returned in uppercase.

    Error handling:
    - Captures socket errors and prints error messages to the console if something goes wrong.

    Usage:
        python server.py
    """

    host = 'localhost'
    port = 5000

    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((host, port))
        server.listen()
        print(f"Servidor escuchando en {host}:{port}...\n")

        while True:
            try:
                connection, address = server.accept()
                print(f"Connection established with: {address}\n")

                while True:
                    message = connection.recv(1024).decode('utf-8')
                    if not message:
                        break

                    print(f"Mensaje recibido del cliente: {message}")
                    if message == "DESCONEXION":
                        print(f" El Cliente {address} solicito la desconexión.\n")
                        connection.close()
                        print("Esperando mensaje de un nuevo cliente...")
                        break

                    message = message.upper()
                    response = f"HOLA CLIENTE, HAS ENVIADO EL MENSAJE: {message}"
                    connection.send(response.encode('utf-8'))
                    print(f"Respuesta enviado al cliente: {response}\n")

            except socket.error as e:
                print(f"Socket error: {e}")

    except Exception as e:
        print(f"Error inciando el servidor: {e}")


if __name__ == "__main__":
    start_server()
