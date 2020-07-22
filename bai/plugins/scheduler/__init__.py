from datetime import datetime

import nonebot
import pytz
from aiocqhttp.exceptions import Error as CQHttpError


#早上提醒打卡
@nonebot.scheduler.scheduled_job('cron', hour=8)
async def _():
    bot = nonebot.get_bot()
    try:
        await bot.send_private_msg(user_id=596552206, message='起床啦！记得健康上报')
        await bot.send_private_msg(user_id=596552206, message='回复:"健康上报"或"打卡",我会自动为您打卡')
    except CQHttpError:
        pass


#每小时报时
@nonebot.scheduler.scheduled_job('cron', hour='*')
async def _():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    try:
        if now.hour in range(6, 23):
            await bot.send_private_msg(user_id=596552206, message=f'等灯等登等噔～现在时间，{now.hour}点整，注意休息鸭^ω^')
    except CQHttpError:
        pass