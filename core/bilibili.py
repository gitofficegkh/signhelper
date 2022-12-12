# 哔哩哔哩(https://www.bilibili.com/)自动签到
import requests


def sign_bilibili(cookie):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77',
        'Cookie': cookie,
    }
    url = 'https://api.live.bilibili.com/xlive/web-ucenter/v1/sign/DoSign'
    req = requests.get(url, headers=headers)
    if req.json()['code'] == 1011040:
        mes = '今天已经签到过了！'
    elif req.json()['code'] == 0:
        mes = f'签到成功！获得{req.json()["data"]["text"]}！'
    elif req.json()["code"] == -101:
        mes = '签到失败，请检查cookie！'
    else:
        print('bilibili：', req.text)
        mes = '签到失败，请联系管理员，提交错误信息！'
    return '哔哩哔哩-->' + mes
