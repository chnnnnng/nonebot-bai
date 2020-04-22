from datetime import datetime

import nonebot
import pytz
from aiocqhttp.exceptions import Error as CQHttpError


@nonebot.scheduler.scheduled_job('cron', hour='*', minute='0/20', second='*')
async def _():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    try:
        await bot.send_private_msg(user_id=596552206, message=f'现在时间:{now.minute}:{now.second}')
    except CQHttpError:
        pass