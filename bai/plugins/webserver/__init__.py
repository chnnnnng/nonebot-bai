import os
import sys
from os import path

import nonebot

bot = nonebot.get_bot()  # 在此之前必须已经 init

@bot.server_app.route('/admin')
async def admin():
    #await bot.send_private_msg(596552206, '你的主页被访问了')
    return '欢迎来到管理页面'


@bot.server_app.route('/update')
async def update():
    try:
        print("重启。。。。。。。")
        return 'OK'
    finally:
        #python = sys.executable
        #os.execl(python, 'python', path.join(path.dirname(__file__), 'restart.py'))
        os.system('sh ' + path.join(path.dirname(path.dirname(path.dirname(path.dirname(__file__)))), 'update.sh'))