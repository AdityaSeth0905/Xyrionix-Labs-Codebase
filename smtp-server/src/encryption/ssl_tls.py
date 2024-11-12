import socket
import ssl
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

class SSLServer:
    def __init__(self, host='localhost', port=4433, certfile='server.crt', keyfile='server.key'):
        self.host = host
        self.port = port
        self.certfile = certfile
        self.keyfile = keyfile

    def start(self):
        # Create a TCP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((self.host, self.port))
        sock.listen(5)
        logger.info(f'Server listening on {self.host}:{self.port}')

        # Wrap the socket with SSL
        ssl_sock = ssl.wrap_socket(sock, certfile=self.certfile, keyfile=self.keyfile, server_side=True)

        while True:
            client_socket, addr = ssl_sock.accept()
            logger.info(f'Connection from {addr}')
            self.handle_client(client_socket)

    def handle_client(self, client_socket):
        with client_socket:
            data = client_socket.recv(1024)
            logger.info(f'Received: {data.decode()}')
            client_socket.sendall(b'Hello from SSL Server!')

class SSLClient:
    def __init__(self, host='localhost', port=4433):
        self.host = host
        self.port = port

    def start(self):
        # Create a TCP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Wrap the socket with SSL
        ssl_sock = ssl.wrap_socket(sock)

        try:
            ssl_sock.connect((self.host, self.port))
            ssl_sock.sendall(b'Hello from SSL Client!')
            response = ssl_sock.recv(1024)
            logger.info(f'Response from server: {response.decode()}')
        except Exception as e:
            logger.error(f'Error: {e}')
        finally:
            ssl_sock.close()

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='SSL/TLS Server and Client')
    parser.add_argument('--mode', choices=['server', 'client'], required=True, help='Run as server or client')
    args = parser.parse_args()

    if args.mode == 'server':
        server = SSLServer()
        server.start()
    elif args.mode == 'client':
        client = SSLClient()
        client.start()