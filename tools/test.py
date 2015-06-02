import os
import socket
import sys

sys.path.insert(0, os.getcwd())

from dynamite.message import Message


def main():
    s = None
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("127.0.0.1", 8888))
        message = Message()
        s.send(message.to_bytes())
    finally:
        if s is not None:
            try:
                s.shutdown(socket.SHUT_RDWR)
                s.close()
            except socket.error:
                pass


if __name__ == '__main__':
    main()
