#!/bin/python3
import socket


class Client:
    def __init__(self, ip: str, port: int):
        self.ip = ip
        self.port = port

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.ip, self.port))
            print(f"Connected to {self.ip}:{self.port}")
            while True:
                data: str = input('Dateipfad: ')
                if not data:
                    break
                s.sendall(data.encode())
                data: str = s.recv(1024).decode()
                print(data)


if __name__ == '__main__':
    client = Client('localhost', 9997)
    client.start()
