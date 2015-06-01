import os
import sys

sys.path.insert(0, os.getcwd())

from dynamite.server import main

main('127.0.0.1', 8888)
