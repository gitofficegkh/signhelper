# mt(https://bbs.binmt.cc/)论坛自动签到
import requests


def sign_mt(cookie, formhash):
    print(cookie)
    print(formhash)
    url = f'https://bbs.binmt.cc/k_misign-sign.html?operation=qiandao&format=button&formhash={formhash}&inajax=1&ajaxtarget=midaben_sign'
    headers = {
        'Cookie': cookie,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70',
    }
    req = requests.get(url=url, headers=headers)
    # print(req.text)
    if '今日已签' in req.text:
        mes = '今日已签到！'
    elif '有非法字符' in req.text:
        mes = '签到失败，请更新cookie和formhash！'
    elif '签到成功' in req.text:
        mes = '签到成功！'
    else:
        print('mt:', req.text)
        mes = '签到失败，请联系管理员，提交错误信息！'
    return 'mt-->' + mes
