# 吾爱破解(https://www.52pojie.cn/)论坛自动签到
import requests


def sign_52pojie(cookie):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77',
        'Cookie': cookie,
    }
    # 申请签到
    apply_url = 'https://www.52pojie.cn/home.php?mod=task&do=apply&id=2&referer=%2F'
    apply_req = requests.post(apply_url, headers=headers, allow_redirects=False)
    if '登录或注册' in apply_req.text:
        mes = '签到失败，cookie可能失效，请检查更新。'
    else:
        # 进行签到
        sign_url = 'https://www.52pojie.cn/home.php?mod=task&do=draw&id=2'
        sign_req = requests.post(sign_url, headers=headers)
        # 任务已完成
        if '任务已完成' in sign_req.text:
            # print('签到成功！')
            mes = '签到成功！'
        # 不是进行中的任务
        elif '不是进行中的任务' in sign_req.text:
            # print('已经签到过了.')
            mes = '今天已经签到过了！'
        else:
            print('wuaipojie:', sign_req.text)
            mes = '签到失败，请联系管理员，提交错误信息！'
    return '吾爱破解-->' + mes
