import core
from conf import config
from tools import sendmessage


def main(*args):
    '''
    启动主函数，根据配置对指定的网站进行签到，并调用配置好的消息通道发送提示信息
    :param args:
    :return:
    '''
    print('开始处理……')
    sign_list = config.sign_config()
    if sign_list:
        massage_box = []
        for i in sign_list:
            if i['name'] == 'jingyi':
                massage_jingyi = core.jingyi.sign_jingyi(cookie=i['cookie'], formhash=i['formhash'])
                massage_box.append(massage_jingyi)
            elif i['name'] == 'kxdao':
                massage_kxdao = core.kxdao.sign_kxdao(cookie=i['cookie'], formhash=i['formhash'])
                massage_box.append(massage_kxdao)
            elif i['name'] == '52pojie':
                massage_52pojie = core.wuaipojie.sign_52pojie(cookie=i['cookie'])
                massage_box.append(massage_52pojie)
            elif i['name'] == 'bilibili':
                a = []
                for c in i['cookie'].split("; "):
                    if "SESSDATA=" in c:
                        a.append(c)
                    elif "bili_jct=" in c:
                        a.append(c)
                    elif "buvid3=" in c:
                        a.append(c)
                    elif "DedeUserID=" in c:
                        a.append(c)
                cookie = '; '.join(a)
                massage_bilibili = core.bilibili.sign_bilibili(cookie=cookie)
                massage_box.append(massage_bilibili)
            elif i['name'] == 'huluxia':
                massage_huluxia = core.huluxia.sign_huluxia(account=i['account'], password=i['password'])
                massage_box.append(massage_huluxia)
            elif i['name'] == 'mt':
                massage_mt = core.mt.sign_mt(cookie=i['cookie'], formhash=i['formhash'])
                massage_box.append(massage_mt)
        # print(massage_box)
        massage = ('\n' * 2).join(massage_box)
        print(massage)
        sendmessage.sendmessage(message=massage)
    else:
        print('没有开启任何一个签到任务！')
    return


if __name__ == '__main__':
    main()
