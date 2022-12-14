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
        "cookie": "X_CACHE_KEY=689dceaa037344d632e19acc58d15383; cQWy_2132_saltkey=D1uq7l71; cQWy_2132_lastvisit=1670598049; cQWy_2132_connect_is_bind=0; cQWy_2132_nofavfid=1; cQWy_2132_atarget=1; cQWy_2132_forum_lastvisit=D_41_1670862635; cQWy_2132_visitedfid=41; cQWy_2132_smile=5D1; cQWy_2132_sid=o3ZItD; cQWy_2132_home_diymode=1; cQWy_2132_ulastactivity=5198yOdD1733h+juvqQrs8JUHygKT0ovm5f9//DedlxZBGRUV/db; cQWy_2132_auth=b8273NRQ1f8tAo46dbtjwVSIN8XDRINCaFock7nspUk1Z3K9+IqCNHXuhoEMFGjH7imGFX2STCfThVWnwXWHaXXDrg; cQWy_2132_misigntime=1670947722; cQWy_2132_sendmail=1; cQWy_2132_lastact=1670947739	home.php	spacecp; cQWy_2132_lastcheckfeed=12184|1670947739",
        "formhash": "18967d44",
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
