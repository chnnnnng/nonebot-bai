import requests
import  json
if __name__ == '__main__':
    payload = {
        'spoken':'你好呀',
        'appid':'b3ba79e8367cdcdfbaa2363c6d7c219c'
    }
    res = requests.post('https://api.ownthink.com/bot',data=payload)
    j = json.loads(res.text)
    print(j)