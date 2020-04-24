import datetime

import nonebot
import pytz
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
        if (await request.form).get('action') == 'get':
            user = (await request.form).get('qq')
            now = datetime.now(pytz.timezone('Asia/Shanghai'))
            vc = str(int(user[0:5])*int(now.minute)*int(now.hour)*int(now.day)+1000)[0:5]
            await bot.send_private_msg(user_id=596552206, message=f'【{vc}】是您的验证码，该验证码一分钟有效。您的账号正在尝试登陆管理页面，如非本人操作，请防范有关风险。')
            return "OK"
        else:
            return "GET"

