"""This class handles the play/game functions."""

import socket


import time


class Play:

    def __init__(self, hostname='127.0.0.1', port=8001):
        self.hostname = '127.0.0.1'
        self.port = 8001
        self.address = (hostname, port)
        self.FORMAT = 'utf-8'
        self.HEADER = 64

    def main(self, username, password):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
            sock.connect(self.address)
            mes = "game"
            message = mes.encode(self.FORMAT)
            sock.send(message)
            time.sleep(1)
            message = username.encode(self.FORMAT)
            sock.send(message)
            time.sleep(1)
            message = password.encode(self.FORMAT)
            sock.send(message)
            time.sleep(1)
            print("Do you want to play agains AI?  (Y, N)\n")
            while True:
                liike = input()
                if liike == "Y":
                    message1 = "0"
                    break
                elif liike == "N":
                    message1 = "1"
                    break
            message1 = message1.encode(self.FORMAT)
            sock.send(message1)
            viesti = sock.recv(self.HEADER).decode(self.FORMAT)
            while not viesti:
                viesti = sock.recv(self.HEADER).decode(self.FORMAT)
            print(viesti)
            viesti = sock.recv(self.HEADER).decode(self.FORMAT)
            while not viesti:
                viesti = sock.recv(self.HEADER).decode(self.FORMAT)
            print(viesti)
            viesti = sock.recv(self.HEADER).decode(self.FORMAT)
            while not viesti:
                viesti = sock.recv(self.HEADER).decode(self.FORMAT)
            print(viesti)
            print("Give your move (R, P, S)\n")
            while True:
                liike = input()
                if liike == "R" or liike == "S" or liike == "P":
                    break
            message = liike.encode(self.FORMAT)
            sock.send(message)
            time.sleep(1)
            print("Opponents move\n")
            time.sleep(1)
            viesti = sock.recv(self.HEADER).decode(self.FORMAT)
            while not viesti:
                viesti = sock.recv(self.HEADER).decode(self.FORMAT)
            print(viesti)

            print("\n")
            viesti = sock.recv(self.HEADER).decode(self.FORMAT)
            while not viesti:
                viesti = sock.recv(self.HEADER).decode(self.FORMAT)
            print(viesti)
            return 0
