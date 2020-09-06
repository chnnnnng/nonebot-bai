import nonebot
import requests
from quart import request
from jinja2 import PackageLoader,Environment
from .main import login

bot = nonebot.get_bot()  # 在此之前必须已经 init

env = Environment(loader=PackageLoader('webserver','templates'))

#热更新借口，向此接口发送POST请求即可重启
@bot.server_app.route('/update', methods=['POST'])
async def update():
    try:
        return 'OK'
    finally:
        requests.post("http://127.0.0.1:94/update")#向本机94端口的一个小服务发送post


@bot.server_app.route('/send_msg_to_single_user', methods=['POST'])
async def send_msg_to_single_user():
    await bot.send_private_msg(user_id=request.form['who'], message=request.form['what'])

