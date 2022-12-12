# 科学刀(https://www.kxdao.net/)论坛自动签到
import requests, time


def sign_kxdao(cookie, formhash):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77',
        'Cookie': cookie,
    }
    message_1 = sign(headers, formhash)
    if '失败' in message_1:
        return '科学刀-->' + message_1
    else:
        message_2 = question(headers, formhash)
        message_3 = posting(headers, formhash)
        return '科学刀-->' + message_1 + message_2 + message_3


def sign(headers, formhash):
    url = 'https://www.kxdao.net/plugin.php?id=dsu_amupper&ppersubmit=true&formhash=' + formhash + '&infloat=yes&handlekey=dsu_amupper&inajax=1&ajaxtarget=fwin_content_dsu_amupper'
    req = requests.get(url=url, headers=headers)
    if '您已签到完毕，今日已无需再次签到' in req.text:
        # print('你今天已经签到过了！')
        mes = '你今天已经签到过了！'
    elif '您当前的访问请求当中含有非法字符，已经被系统拒绝' in req.text:
        # print('签到非法，请检查cookie与fromhash是否失效！')
        mes = '签到失败，请检查cookie与fromhash是否失效！'
    elif '累计签到' in req.text:
        # print('签到成功！')
        mes = '签到成功！'
    else:
        print('kxdao:', req.text)
        mes = '签到失败，请联系管理员，提交错误信息！'
    return mes


def question(headers, formhash):
    url = 'https://www.kxdao.net/plugin.php?id=ahome_dayquestion:pop'
    data_answer = {
        'formhash': formhash,
        'answer': '1',
        'submit': 'true',
    }
    data_next = {
        'formhash': formhash,
        'next': 'true',
    }
    data_finish = {
        'formhash': formhash,
        'finish': 'true',
    }
    for i in range(1, 5):
        if i == 1 or i == 3:
            req = requests.post(url=url, headers=headers, params=data_answer)
            if '您今天已经参加过答题，明天再来吧' in req.text:
                return '已答题！'
        elif i == 2:
            requests.post(url=url, headers=headers, params=data_next)
        else:
            requests.post(url=url, headers=headers, params=data_finish)
            return '答题完成！'


def posting(headers, formhash):
    url = 'https://www.kxdao.net/forum.php?mod=post&action=newthread&fid=55&extra=&topicsubmit=yes'
    posttime = time.time()
    data = {
        'formhash': formhash,
        'posttime': posttime,  # 时间戳
        'wysiwyg': '1',
        'typeid': 40,  # 41为报道打卡，40为灌水专区
        'subject': '每日打卡',  # 标题
        'message': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(posttime)),  # 内容
        'readperm': '',
        'price': '',
        'rushreplyfrom': '',
        'rushreplyto': '',
        'rewardfloor': '',
        'replylimit': '',
        'stopfloor': '',
        'creditlimit': '',
        'allownoticeauthor': '1',
        'addfeed': '1',
        'usesig': '1',
        'save': '',
    }
    try:
        requests.post(url=url, headers=headers, params=data)
        return '灌水区已发帖！'
    except Exception as e:
        return '发帖出错！'


if __name__ == '__main__':
    cookie = "G1NZ_2132_saltkey=AkRS9nzQ; G1NZ_2132_lastvisit=1659609850; G1NZ_2132_client_token=29056F8CD7AE69AEEB14CB4911736691; G1NZ_2132_connect_is_bind=1; G1NZ_2132_connect_uin=29056F8CD7AE69AEEB14CB4911736691; G1NZ_2132_nofavfid=1; G1NZ_2132_atarget=1; G1NZ_2132_smile=5D1; G1NZ_2132_pc_size_c=0; G1NZ_2132_client_created=1660977006; G1NZ_2132_auth=211ft3YXm0OwzwyHs3rGu029xL%2Fs0wj%2FbHa3262UHr8Rv6yojAlcoMJJeGktCasNx1KSvdru5O4FcJZktMKRV%2Bv6; G1NZ_2132_connect_login=1; G1NZ_2132_stats_qc_login=3; G1NZ_2132_myrepeat_rr=R0; G1NZ_2132_ulastactivity=fd84zk2c85CecMb3M31uBLnMvHoEY9YjyjS%2FnkZL5joTJia7MnUC; G1NZ_2132_forum_lastvisit=D_46_1660387455D_73_1660890347D_42_1660890351D_2_1660890363D_36_1660900514D_55_1660978334D_48_1661046654; G1NZ_2132_visitedfid=48D55D36D2D42D73D38D46; G1NZ_2132_sid=bP4rk5; G1NZ_2132_lip=1.12.218.146%2C1661047204; G1NZ_2132_popadv=a%3A0%3A%7B%7D; G1NZ_2132_dsu_amupper=DQo8c3R5bGU%2BDQoucHBlcndibSB7cGFkZGluZzo2cHggMTJweDtib3JkZXI6MXB4IHNvbGlkICNDRENEQ0Q7YmFja2dyb3VuZDojRjJGMkYyO2xpbmUtaGVpZ2h0OjEuOGVtO2NvbG9yOiMwMDMzMDA7d2lkdGg6MjAwcHg7b3ZlcmZsb3c6aGlkZGVufQ0KLnBwZXJ3Ym0gLnRpbWVze2NvbG9yOiNmZjk5MDA7fQ0KLnBwZXJ3Ym0gIGF7ZmxvYXQ6cmlnaHQ7Y29sb3I6I2ZmMzMwMDt0ZXh0LWRlY29yYXRpb246bm9uZX0NCjwvc3R5bGU%2BDQoNCjxkaXYgY2xhc3M9InBwZXJ3Ym0iIGlkPSJwcGVyd2JfbWVudSIgc3R5bGU9ImRpc3BsYXk6IG5vbmUiID4NCjxBIEhSRUY9InBsdWdpbi5waHA%2FaWQ9ZHN1X2FtdXBwZXI6cHBlcmxpc3QiIHRhcmdldD0iX2JsYW5rIj7mn6XnnIvnrb7liLDmjpLooYw8L0E%2BDQo8c3Ryb25nPue0r%2BiuoeetvuWIsDxzcGFuIGNsYXNzPSJ0aW1lcyI%2BMTEyMzwvc3Bhbj7mrKE8L3N0cm9uZz48YnI%2BDQoNCjxzdHJvbmc%2B6L%2Be57ut562%2B5YiwPHNwYW4gY2xhc3M9InRpbWVzIj42Mzwvc3Bhbj7mrKE8L3N0cm9uZz48YnI%2BDQoNCjxzdHJvbmc%2B5LiK5qyh562%2B5YiwOiA8c3BhbiBjbGFzcz0idGltZXMiPjIwMjItMDgtMjEgMDk6NTA6MTk8L3NwYW4%2BPC9zdHJvbmc%2BDQo8L2Rpdj4NCg%3D%3D; G1NZ_2132_sendmail=1; G1NZ_2132_lastcheckfeed=5324%7C1661054154; G1NZ_2132_checkfollow=1; G1NZ_2132_checkpm=1; G1NZ_2132_lastact=1661054154%09misc.php%09patch"
    formhash = "ee7dd06e"
    print(sign_kxdao(cookie=cookie, formhash=formhash))
