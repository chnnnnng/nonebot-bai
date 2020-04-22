import requests
import  json
if __name__ == '__main__':
    payload = {
        'spoken':'你好呀',
        'appid':'b3ba79e8367cdcdfbaa2363c6d7c219c'
    }
    res = requests.post('https://api.ownthink.com/bot',data=payload)
    resp_payload = json.loads(res.text)
    if resp_payload['message'] == 'success':
        if  resp_payload['data']['type']== 5000:
            # 返回文本类型的回复
            print(resp_payload['data']['info']['text'])