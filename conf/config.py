# 在此文件内进行网站签到配置
# name 不用修改
# open 为True则开启签到，Fals不开启
# cookie 网站cookie
# formhash 有的网站需要有的不需要，根据情况配置
# account 社区账号
# password 社区账号对应的密码
import os
# 签到配置
website_config = [
    # 吾爱破解网站配置
    {
        "name": "52pojie",
        "open": False,
        "cookie": "",
    },
    # 科学刀配置
    {
        "name": "kxdao",
        "open": False,
        "cookie": "",
        "formhash": "",
    },
    # 精易论坛配置
    {
        "name": "jingyi",
        "open": False,
        "cookie": "",
        "formhash": "",
    },
    # 哔哩哔哩配置
    {
        "name": "bilibili",
        "open": False,
        "cookie": "",
    },
    # 葫芦侠配置
    {
        "name": "huluxia",
        "open": False,
        "account": "",
        "password": "",
    },
    # mt论坛配置
    {
        "name": "mt",
        "open": True,
        "cookie": os.environ.get("MT_Cookies", None),
        "formhash": os.environ.get("MT_Formhash", None),
    },
]

# 发送提示信息配置
sendmessage_config = [
    # server酱sendkey
    {
        "name": "serverchan",
        "open": True,
        "sendkey": os.environ.get("SERVERCHAN_SENDKEY", None),
    },
]


# 以下内容不用修改
def sign_config():
    """
    检查开启签到的网站，返回已经开启的网站
    :return: config_list
    """
    config_list = []
    for i in website_config:
        if i["open"]:
            config_list.append(i)
    # print(config_list)
    return config_list


def send_config():
    """
    检查开启的发送信息通道，返回已经开启的通道
    :return: config_list
    """
    config_list = []
    for i in sendmessage_config:
        if i["open"]:
            config_list.append(i)
    # print(config_list)
    return config_list


if __name__ == "__main__":
    sign_config()
