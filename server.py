#!/bin/python3
import socket

from communicator import TextFile


class Server:
    def __init__(self, ip: str, port: int):
        self.ip = ip
        self.port = port

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.ip, self.port))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    data: bytes = conn.recv(1024)
                    if not data:
                        break

                    text_file: TextFile = TextFile(file_path=data.decode())

                    if text_file.file_exists():
                        text_file.file_content = text_file.read()
                        conn.sendall(bytes(text_file.serialize(), 'utf-8'))
                    else:
                        conn.sendall(bytes('File not found', 'utf-8'))


if __name__ == '__main__':
    server = Server('localhost', 9997)
    server.start()
