import socket
import random
import time

def handle_client(client_socket):
    try:
        while True:
            value = random.uniform(0, 5)  # Gera um número aleatório entre 0 e 5 com uma casa decimal
            message = f"{value:.1f}mm\n"  # Formata o número com uma casa decimal e adiciona "g"
            client_socket.sendall(message.encode('utf-8'))
            time.sleep(1)
    except (ConnectionAbortedError, ConnectionResetError, BrokenPipeError):
        print('Client disconnected.')
    finally:
        client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen(5)  # Permitir até 5 conexões em espera
    print('Server listening on port 12345...')

    try:
        while True:
            client_socket, client_address = server_socket.accept()
            print(f'Connection from {client_address} has been established.')
            handle_client(client_socket)
    except KeyboardInterrupt:
        print('Server is shutting down...')
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()