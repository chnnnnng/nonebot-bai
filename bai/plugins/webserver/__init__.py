import os
import threading
from os import path

import nonebot

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
        T = threading.Thread(target=restart())
        T.setDaemon(True)
        T.start()
        T.join()

