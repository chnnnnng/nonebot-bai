import os
from os import path

from apscheduler.schedulers.blocking import BlockingScheduler


def x():
    sched = BlockingScheduler()
    sched.add_job(xx, 'interval', seconds=5)
    sched.start()


def xx():
    os.system('sh ' + path.join(path.dirname(path.dirname(path.dirname(path.dirname(__file__)))), 'update.sh'))


if __name__ == '__main__':
    x()