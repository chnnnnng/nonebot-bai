import nonebot
from quart import render_template

bot = nonebot.get_bot()  # 在此之前必须已经 init


@bot.server_app.route('/login')
async def login():
    # await bot.send_private_msg(596552206, '你的主页被访问了')
    return await render_template('login.html')