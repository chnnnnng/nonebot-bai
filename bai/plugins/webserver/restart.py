from apscheduler.schedulers.blocking import BlockingScheduler

if __name__ == '__main__':
    i=0
    while(True):
        i+=1

def x():
    sched = BlockingScheduler()
    sched.add_job(xx, 'interval', seconds=5)
    sched.start()


def xx():
    return