import os
import sys
import time
from os import path
import os, signal

def kill(pid):
    try:
        a = os.kill(pid, signal.SIGKILL)
        print('已杀死pid为%s的进程,　返回值是:%s' % (pid, a))
    except OSError:
        print('没有如此进程!!!')


if __name__ == '__main__':
    out = os.popen("ps aux | grep bot.py").read()
    for line in out.splitlines():
        print(line)
        if 'bot.py' in line:
            pid = int(line.split()[1])
            print(pid)
            kill(pid)
    # time.sleep(2)
    os.system("ss -p")
    print("开始重启")
    # os.system('sleep 10s; print "REEEEEEEEEEEEEEEE"')
    # os.system('ps -aux | grep bot.py | grep -v \"grep\" | awk \'{print $2}\' | xargs kill -9')
    # os.system('sh ' + path.join(path.dirname(path.dirname(path.dirname(path.dirname(__file__)))), 'update.sh'))
    ##os.system('pkill python')
    python = sys.executable
    os.execl(python, 'python', path.join(path.dirname(path.dirname(path.dirname(path.dirname(__file__)))), 'bot.py'))
