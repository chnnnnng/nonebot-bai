import datetime
from bs4 import BeautifulSoup
import requests
from nonebot import on_command, CommandSession

#自动健康上报（20年暑假有效）

hr_url = 'http://mapp.zjut.edu.cn/_web/_apps/eform/eform/api/survey/create.rst?domainId=1&topicId=17&beginTimes='
hr_data = {'subjectData': '{"subject":"question-subject_17","readyOnly":false,"data":[{"qid":"question-263","options":[{"oid":"option-1038","checked":true,"value":"201906061102"}],"value":["201906061102"]},{"qid":"question-265","options":[{"oid":"option-1040","checked":true,"value":"陈杨"}],"value":["陈杨"]},{"qid":"question-268","options":[{"oid":"option-1043","checked":true,"value":"1043"},{"oid":"option-1044","checked":false,"value":"1044"}],"value":["1043"]},{"qid":"question-134","options":[{"oid":"option-819","checked":false,"value":"819"},{"oid":"option-820","checked":true,"value":"820"},{"oid":"option-821","checked":false,"value":"821"},{"oid":"option-1221","checked":false,"value":"1221"},{"oid":"option-1371","checked":false,"value":"1371"},{"oid":"option-single-1371","checked":true,"value":""}],"value":["820",""]},{"qid":"question-267","options":[{"oid":"option-1042","checked":true,"value":"信息工程学院"}],"value":["信息工程学院"]},{"qid":"question-246","options":[{"oid":"question-246","checked":true,"value":"1009"}],"value":["1009"]},{"qid":"question-315","options":[{"oid":"","checked":true,"value":"江苏省 常州市 武进区 南夏墅 庙桥 "},{"oid":"province-315","checked":true,"value":"省份"},{"oid":"city-315","checked":true,"value":"地级市"},{"oid":"district-315","checked":true,"value":"区县、县级市"},{"oid":"address-315","checked":true,"value":" 南夏墅 庙桥 "}],"value":["江苏省 常州市 武进区 南夏墅 庙桥 "]},{"qid":"question-248","options":[{"oid":"option-1011","checked":false,"value":"1011"},{"oid":"option-1012","checked":true,"value":"1012"}],"value":["1012"]},{"qid":"question-296","options":[{"oid":"","checked":true,"value":"江苏省 常州市 武进区 南夏墅 庙桥 "},{"oid":"province-296","checked":true,"value":"省份"},{"oid":"city-296","checked":true,"value":"地级市"},{"oid":"district-296","checked":true,"value":"区县、县级市"},{"oid":"address-296","checked":true,"value":" 南夏墅 庙桥 "}],"value":["江苏省 常州市 武进区 南夏墅 庙桥 "]},{"qid":"question-266","options":[{"oid":"option-1041","checked":true,"value":"15700088294"}],"value":["15700088294"]},{"qid":"question-137","options":[{"oid":"option-826","checked":true,"value":"陈青松"}],"value":["陈青松"]},{"qid":"question-138","options":[{"oid":"option-827","checked":true,"value":"15151962448"}],"value":["15151962448"]},{"qid":"question-249","options":[{"oid":"option-1013","checked":true,"value":"1013"},{"oid":"option-1014","checked":false,"value":"1014"},{"oid":"option-1015","checked":false,"value":"1015"},{"oid":"option-1016","checked":false,"value":"1016"},{"oid":"option-1205","checked":false,"value":"1205"}],"value":["1013"]},{"qid":"question-308","options":[{"oid":"","checked":true,"value":"江苏省 常州市 武进区 南夏墅 庙桥 "},{"oid":"province-308","checked":true,"value":"省份"},{"oid":"city-308","checked":true,"value":"地级市"},{"oid":"district-308","checked":true,"value":"区县、县级市"},{"oid":"address-308","checked":true,"value":" 南夏墅 庙桥 "}],"value":["江苏省 常州市 武进区 南夏墅 庙桥 "]},{"qid":"question-142","options":[{"oid":"option-837","checked":true,"value":"837"},{"oid":"option-838","checked":false,"value":"838"},{"oid":"option-single-838","checked":true,"value":""}],"value":["837",""]},{"qid":"question-307","options":[{"oid":"option-1208","checked":false,"value":"1208"},{"oid":"option-single-1208","checked":true,"value":""},{"oid":"option-1209","checked":true,"value":"1209"}],"value":["","1209"]},{"qid":"question-489","options":[],"value":[]},{"qid":"question-146","options":[{"oid":"option-843","checked":false,"value":"843"},{"oid":"option-single-843","checked":true,"value":""},{"oid":"option-844","checked":true,"value":"844"}],"value":["","844"]},{"qid":"question-148","options":[{"oid":"option-846","checked":false,"value":"846"},{"oid":"option-single-846","checked":true,"value":""},{"oid":"option-847","checked":false,"value":"847"},{"oid":"option-single-847","checked":true,"value":""},{"oid":"option-1373","checked":true,"value":"1373"}],"value":["","","1373"]},{"qid":"question-150","options":[{"oid":"option-849","checked":false,"value":"849"},{"oid":"option-single-849","checked":true,"value":""},{"oid":"option-850","checked":false,"value":"850"},{"oid":"option-single-850","checked":true,"value":""},{"oid":"option-1374","checked":true,"value":"1374"}],"value":["","","1374"]},{"qid":"question-152","options":[{"oid":"option-852","checked":false,"value":"852"},{"oid":"option-single-852","checked":true,"value":""},{"oid":"option-853","checked":true,"value":"853"}],"value":["","853"]},{"qid":"question-311","options":[{"oid":"option-1219","checked":false,"value":"1219"},{"oid":"option-single-1219","checked":true,"value":""},{"oid":"option-1220","checked":true,"value":"1220"}],"value":["","1220"]},{"qid":"question-154","options":[{"oid":"option-855","checked":false,"value":"855"},{"oid":"option-single-855","checked":true,"value":""},{"oid":"option-857","checked":true,"value":"857"}],"value":["","857"]},{"qid":"question-159","options":[{"oid":"question-159","checked":true,"value":"1097"}],"value":["1097"]},{"qid":"question-162","options":[{"oid":"option-871","checked":false,"value":"871"},{"oid":"option-single-871","checked":true,"value":""},{"oid":"option-872","checked":true,"value":"872"}],"value":["","872"]},{"qid":"question-279","options":[],"value":[]},{"qid":"question-165","options":[{"oid":"option-877","checked":false,"value":"877"},{"oid":"option-single-877","checked":true,"value":""},{"oid":"option-879","checked":true,"value":"879"}],"value":["","879"]},{"qid":"question-177","options":[{"oid":"option-897","checked":false,"value":"897"},{"oid":"option-single-897","checked":true,"value":""},{"oid":"option-899","checked":true,"value":"899"}],"value":["","899"]},{"qid":"question-173","options":[{"oid":"option-889","checked":false,"value":"889"},{"oid":"option-single-889","checked":true,"value":""},{"oid":"option-891","checked":true,"value":"891"}],"value":["","891"]},{"qid":"question-741","options":[{"oid":"option-2572","checked":false,"value":"2572"},{"oid":"option-single-2572","checked":true,"value":""},{"oid":"option-2573","checked":true,"value":"2573"}],"value":["","2573"]},{"qid":"question-749","options":[],"value":[]},{"qid":"question-750","options":[{"oid":"option-2591","checked":false,"value":"2591"},{"oid":"option-2592","checked":true,"value":"2592"}],"value":["2592"]},{"qid":"question-756","options":[{"oid":"question-data756","checked":true,"value":""}],"value":[""]},{"qid":"question-748","options":[{"oid":"option-2590","checked":true,"value":""}],"value":[""]},{"qid":"question-747","options":[{"oid":"option-2584","checked":false,"value":"2584"},{"oid":"option-single-2584","checked":true,"value":""},{"oid":"option-2585","checked":false,"value":"2585"},{"oid":"option-single-2585","checked":true,"value":""},{"oid":"option-2586","checked":false,"value":"2586"},{"oid":"option-single-2586","checked":true,"value":""},{"oid":"option-2587","checked":false,"value":"2587"},{"oid":"option-single-2587","checked":true,"value":""},{"oid":"option-2588","checked":false,"value":"2588"},{"oid":"option-single-2588","checked":true,"value":""},{"oid":"option-2589","checked":false,"value":"2589"},{"oid":"option-single-2589","checked":true,"value":""}],"value":["","","","","",""]},{"qid":"question-493","options":[{"oid":"option-1767","checked":false,"value":"1767"},{"oid":"option-1768","checked":false,"value":"1768"},{"oid":"option-1771","checked":true,"value":"1771"},{"oid":"option-2568","checked":false,"value":"2568"},{"oid":"option-1772","checked":false,"value":"1772"}],"value":["1771"]},{"qid":"question-299","options":[{"oid":"option-1185","checked":true,"value":"1185"}],"value":["1185"]}]}'}
hr_header = {'Cookie':'JSESSIONID=28E05B0634ADAADF6A6B8DBC82EE2D9C','Content-Type':'application/x-www-form-urlencoded'}
login_url = 'http://auth.zjut.edu.cn/zfca/login?service=http%3A%2F%2Fmapp.zjut.edu.cn%2Findex.jsp%3FdomainId%3D1%26act%3D1'
login_data = {"useValidateCode":"0","isremenberme":"1","ip":"","username":"201906061102","password":"chenyang20010703","lt":"_c7D49047C-6D1C-661C-3B2D-591F68FBA68D_kD1FE34A2-8AB7-F44B-AAD5-C72304ED2A1E","_eventId":"submit","submit1":"(unable to decode value)","losetime":"240"}
login_header = {"Host":"auth.zjut.edu.cn","Connection":"keep-alive","Content-Length":"214","Pragma":"no-cache","Cache-Control":"no-cache","Upgrade-Insecure-Requests":"1","Origin":"http://auth.zjut.edu.cn","Content-Type":"application/x-www-form-urlencoded","User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","Referer":"http://auth.zjut.edu.cn/zfca/login?service=http%3A%2F%2Fmapp.zjut.edu.cn%2Findex.jsp%3FdomainId%3D1%26act%3D1","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8","Cookie":"JSESSIONID=6FF42F06E73D12A41C5B9C57DD14E0A5"}


@on_command('healthreport', aliases=('健康上报', '打卡'))
async def healthreport(session: CommandSession):
    await session.send("好的，稍等2")
    sess = requests.Session()
    cookie = getJsessionid(sess, '201906061102','chenyang20010703')
    hr_header['Cookie'] = cookie
    await session.send(dopost())


def dopost():
    r = requests.post(hr_url+getTime(),data=hr_data,headers=hr_header)
    return r.text


def getTime():
    d = datetime.datetime.now()
    return d.__format__('%Y-%m-%d %H:%H:%S')


def getLtAndCookie(sess):
    r = sess.get(login_url)
    soup = BeautifulSoup(r.text,"html.parser")
    return [soup.find(attrs={'name': 'lt'})['value'],r.headers['Set-Cookie']]


def doLogin(sess,username,password,lt,cookie):
    login_data['username'] = username
    login_data['password'] = password
    login_data['lt'] = lt
    login_header['Cookie'] = cookie
    r = sess.post(login_url, data=login_data, headers=login_header, allow_redirects=False)
    return r

def getJsessionid(sess,username,password):
    t = getLtAndCookie(sess)
    r = doLogin(sess, username, password, t[0], t[1])
    r2 = requests.get(r.headers['Location'])
    return r2.headers['Set-Cookie']