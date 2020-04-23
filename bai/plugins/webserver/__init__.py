import os
import sys
from os import path

import nonebot
from apscheduler.schedulers.blocking import BlockingScheduler

bot = nonebot.get_bot()  # 在此之前必须已经 init


@bot.server_app.route('/')
async def admin():
    # await bot.send_private_msg(596552206, '你的主页被访问了')
    return 'QBot管理页面'


def restart():
    os.system('sh ' + path.join(path.dirname(path.dirname(path.dirname(path.dirname(__file__)))), 'update.sh'))


@bot.server_app.route('/update', methods=['POST'])
async def update():
    try:
        return 'OK'
    finally:
        python = sys.executable
        os.execl(python, python,path.join(path.dirname(__file__),'restart.py'))

