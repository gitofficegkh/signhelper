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
        "open": True,
        "cookie": "__gads=ID=24f10dffb06da104-223a940e6ad000e6:T=1643888841:RT=1643888841:S=ALNI_MYAcGtfL48eq1D4r7d3YQzQs9KH7Q; __bid_n=18506ee2b8999cd97c4207; FEID=v10-39ae2776b81d07d0c6558f2eda5ef8dba7f3260a; htVC_2132_saltkey=LvmzXRx1; htVC_2132_lastvisit=1670855419; htVC_2132_auth=77cfbuLEfB34wK%2B6Z25oCdEp6TQSO6uEON%2FpNufsW%2BA%2BPHt2%2FwMNJquFj22OqTlO2oKl5Wwo2eDgjOM2i91jzlewuTJj; htVC_2132_lastcheckfeed=1488324%7C1670859045; htVC_2132_sid=0; htVC_2132_connect_is_bind=0; htVC_2132_nofavfid=1; htVC_2132_atarget=1; htVC_2132_smile=1D1; wzws_sessionid=gWU0OWQ4M4AxMTAuMTg1LjE3LjE1NKBjmJpqgmRiMWNhYQ==; Hm_lvt_46d556462595ed05e05f009cdafff31a=1670427220,1670858550,1670945402; __gpi=UID=0000068c388fbdd5:T=1654948603:RT=1670945388:S=ALNI_MY4l-RpNSluNfaGHmFWT4JBzziOqA; htVC_2132_noticonf=1488324D1D3_3_1; __xaf_fpstarttimer__=1670946466107; __xaf_ths__={"data":{"0":1,"1":86400,"2":60},"id":"9a881b67-d2ad-4180-a224-4d2429331283"}; __xaf_thstime__=1670946466440; FPTOKEN=cmUfLKrROPk86aeTHD96pcqA49H1m3SX+e/LnD6Bqh5MrGfnsdA2KkOQrmFEVafwkoWHPs0K4z0bYV0IqOsxLWc/yeM2ydxpejxf0vlJ8RlWtq3Fcuj/DkEsOxtShKZmg+6JhqNkU6HJAlfHw5o9NWE2gEDPv6I2UbM/c9Vw0dCKe6hSNX1EAD6ucxJijS1zHYsiL3AHt/6Su0NW54acaDnaC0tczXr678eYQhTL8kxeBU2nD+a5SYSOTq56mmvJ8hDX8luafIJClENJ7ZT0qVoWRCGzqpVxJk4jNjMr8sMvF5SDTVurnXrhyJpJLvDL84AzRaGelbrex7s6EHSpXmts9Md6+iBOMK6crhlKTOP2ARuN7USL3XkBDo9L8yKCHugCcLGkVClGLg2+ZpD0G+7JymxAsP+J0lyJGMW/W9a/dfPg7VPW39wcIES8cUSp|k9dVOoggQtLQKVbHA+Ee8qMFj4TlcV4qCeMiz+Hv1V0=|10|7b8ad401b2e00727032ae9e8d1cb1274; __xaf_fptokentimer__=1670946466575; htVC_2132_viewid=tid_1677080; htVC_2132_st_p=1488324%7C1670946916%7Ce121d5c25bcf588f49a627ca5dbbaa3e; htVC_2132_visitedfid=65D24D16; htVC_2132_st_t=1488324%7C1670948756%7C832779233c2342450108cccad9c53756; htVC_2132_forum_lastvisit=D_65_1670948756; htVC_2132_ulastactivity=1670948756%7C0; Hm_lpvt_46d556462595ed05e05f009cdafff31a=1670948792; htVC_2132_lastact=1670948787%09forum.php%09ajax",
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
