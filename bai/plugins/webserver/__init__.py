import nonebot
import requests

bot = nonebot.get_bot()  # 在此之前必须已经 init


#热更新借口，向此接口发送POST请求即可重启
@bot.server_app.route('/update', methods=['POST'])
async def update():
    try:
        return 'OK'
    finally:
        requests.post("http://127.0.0.1:94/update")#向本机94端口的一个小服务发送post

