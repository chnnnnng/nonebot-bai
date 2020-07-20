from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from jieba import posseg


@on_command('healthreport', aliases=('健康上报', '打卡'))
async def healthreport(session: CommandSession):
    #city = session.get('city', prompt='你想查询哪个城市的天气呢？')
    #weather_report = await get_weather_of_city(city)
    await session.send("好的")