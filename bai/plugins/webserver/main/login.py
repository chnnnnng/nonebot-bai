import nonebot
from jinja2 import PackageLoader,Environment
from quart import render_template

bot = nonebot.get_bot()  # 在此之前必须已经 init
env = Environment(loader=PackageLoader('webserver','templates'))


@bot.server_app.route('/login')
async def login():
    # await bot.send_private_msg(596552206, '你的主页被访问了')
    template = env.get_template('login/login.html')  # 获取一个模板文件
    return await template.render()  # 渲染