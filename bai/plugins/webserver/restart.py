import os
import sys
import time
from os import path

if __name__ == '__main__':
    print("开始重启")
    time.sleep(2)
    python = sys.executable
    os.execl(python, 'python', path.join(path.dirname(path.dirname(path.dirname(path.dirname(__file__)))), 'bot.py'))