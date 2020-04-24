import nonebot
from quart import request

from . import common
bot = nonebot.get_bot()  # 在此之前必须已经 init


@bot.server_app.route('/login', methods=['GET','POST'])
async def login():
    if request.method == 'GET':
        # await bot.send_private_msg(596552206, '你的主页被访问了')
        template = common.getTemplate('login')
        return template.render()  # 渲染
    else:
        await bot.send_private_msg(596552206, '发送验证码')
        return "OK"
