# README.md
# Cliente y Servidor TCP en Python

Este proyecto implementa un cliente y servidor TCP que se comunican en la misma máquina (localhost) usando el puerto 5000.

## Instrucciones
### Requisitos
- Python 3 instalado

### Ejecución
1. Abre dos terminales: una para el servidor y otra para el cliente y navega hasta la carpeta tcp con el comando: cd tcp

2. En la primera terminal, ejecuta el servidor:
   ```
   python servidor.py
   ```

3. En la segunda terminal, ejecuta el cliente:
   ```
   python cliente.py
   ```

4. Interactúa desde el cliente:
   - Ingresa cualquier mensaje y observa la respuesta en mayúsculas desde el servidor.
   - Si dejas en blanco el mensaje validara hasta que se introduzca un mensaje.
   - Ingresa "DESCONEXION" para finalizar la conexión.
   - El servidor quedara en espera para otra conexión.

## Pruebas Manuales
- **Prueba 1:** Envía un mensaje normal desde el cliente, por ejemplo, "hola servidor", y verifica que el servidor responda con HOLA CLIENTE y el mensaje que envio en mayusculas.
- **Prueba 2:** Envía "DESCONEXION" y verifica que la conexión se cierre en el cliente pero el servidor queda activo para nuevas conexiones con otro clinte.
