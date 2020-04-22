from nonebot.default_config import *

#配置超级用户
SUPERUSERS = {596552206}

#命令起始符
COMMAND_START = {'', '/', '!', '／', '！'}

#配置IP和端口
HOST = '0.0.0.0'
PORT = 93

#配置昵称
NICKNAME = {'小柏', '小白', '陈小柏', '陈小白', '爸爸', '爷爷'}

#ownthink Appid
OWNTHINK_APPID = 'b3ba79e8367cdcdfbaa2363c6d7c219c'


#Ownthink现阶段不能识别Appid，因此要手动替换部分字符
OWNTHINK_REPLACE_WORDS = {
    '小思': '小柏'
}