from os import path

import jinja2
import nonebot
from jinja2 import PackageLoader,Environment
from quart import render_template

bot = nonebot.get_bot()  # 在此之前必须已经 init


@bot.server_app.route('/login')
async def login():
    # await bot.send_private_msg(596552206, '你的主页被访问了')
    templateLoader = jinja2.FileSystemLoader(searchpath=path.join(path.dirname(__file__),'templates'))
    templateEnv = jinja2.Environment(loader=templateLoader)
    TEMPLATE_FILE = "login.html"
    template = templateEnv.get_template(TEMPLATE_FILE)
    return await template.render()  # 渲染