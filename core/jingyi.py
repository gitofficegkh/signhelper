# 精易(https://bbs.125.la/)论坛自动签到
import requests


def sign_jingyi(cookie, formhash):
    url = 'https://bbs.125.la/plugin.php?id=dsu_paulsign:sign&operation=qiandao&infloat=1'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.47',
        'Cookie': cookie,
    }
    data = {
        'formhash': formhash,
        'submit': '1',
        'targerurl': '',
        'todaysay': '',
        'qdxq': 'kx',
    }
    req = requests.post(url, headers=headers, data=data)
    # print(req.text)
    # print(req.json()['status'], type(req.json()['status']))
    if req.json()["status"] == 0:
        mes = req.json()['msg']
    elif '您需要先登录才能继续本操作' in req.text:
        mes = '签到失败，请更新cookie和formhash！'
    elif req.json()["status"] == 1:
        mes = '签到成功！'
    else:
        print('jingyi:', req.text)
        mes = '签到失败，请联系管理员，提交错误信息！'
    return '精易-->' + mes
