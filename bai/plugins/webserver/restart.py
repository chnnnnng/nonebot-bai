import os
import sys
import time
from os import path

if __name__ == '__main__':
    time.sleep(2)
    print("开始重启")
    os.system('ps -aux | grep bot.py | grep -v \"grep\" | awk \'{print $2}\' | xargs kill -9')
    os.system('sleep 10s')
    #os.system('pkill python')
    #python = sys.executable
    #os.execl(python, 'python', path.join(path.dirname(path.dirname(path.dirname(path.dirname(__file__)))), 'bot.py'))