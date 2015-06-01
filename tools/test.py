import os
import socket
import sys

sys.path.insert(0, os.getcwd())

from dynamite.message import Message


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect(("127.0.0.1", 8888))
        message = Message()
        s.send(message.to_bytes())
    finally:
        s.shutdown(socket.SHUT_RDWR)
        s.close()


if __name__ == '__main__':
    main()
