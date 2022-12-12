from conf import config
import requests


def sendmessage(message):
    '''
    对信息进行发送，根据需求调用指定的通道
    :param message: 要发送的信息
    :return:
    '''
    send_list = config.send_config()
    # print(send_list)
    if send_list:
        for i in send_list:
            if i['name'] == 'serverchan':
                if i['sendkey']:
                    if '失败' in message:
                        title = 'SignHelperTip，签到有失败，点击查看详情。'
                    else:
                        title = 'SignHelperTip，签到成功，点击查看详情。'
                    requests.post(
                        url=f'https://sctapi.ftqq.com/{i["sendkey"]}.send',
                        data={
                            'title': title,
                            'desp': message,
                        }
                    )
                else:
                    print('serverchan-->请配置发送信息所需要的sendkey！')
    else:
        print('没有配置消息通道！')
    return


if __name__ == '__main__':
    sendmessage('ceshi')
