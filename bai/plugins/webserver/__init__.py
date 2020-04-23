import nonebot
import requests
from quart import render_template

bot = nonebot.get_bot()  # 在此之前必须已经 init


@bot.server_app.route('/login')
async def login():
    # await bot.send_private_msg(596552206, '你的主页被访问了')
    return render_template('login/login.html')


#热更新借口，向此接口发送POST请求即可重启
@bot.server_app.route('/update', methods=['POST'])
async def update():
    try:
        return 'OK'
    finally:
        requests.post("http://127.0.0.1:94/update")

