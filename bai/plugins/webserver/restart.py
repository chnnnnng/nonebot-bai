import os
import sys
from os import path

if __name__ == '__main__':
    print("开始重启")
    python = sys.executable
    os.execl(python, python, path.join(path.dirname(path.dirname(path.dirname(path.dirname(__file__)))), 'bot.py'))