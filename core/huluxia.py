# 葫芦侠社区自动签到
import requests, hashlib, time, random


def sign_huluxia(account, password):
    key = login(account, password)
    if '请检查账号密码是否正确' in key:
        return '葫芦侠-->' + key
    return '葫芦侠-->' + sign(plate_list=plate(key=key), key=key)


headers = {
    'User-Agent': 'okhttp/3.8.1',
}


def md5_encode(content):
    md5_en = hashlib.md5()
    md5_en.update(content.encode('utf-8'))
    return md5_en.hexdigest()


def login(account, password):
    '''
    登录
    :param account: 账号
    :param password: 密码
    :return: key
    '''
    url = 'http://floor.huluxia.com/account/login/ANDROID/4.1.8?platform=2&gkey=000000&app_version=4.1.2&versioncode=350&market_id=tool_web&_key=&device_code=%5Bd%5Dd5f270d8-fc06-4230-b185-67da7669508b&phone_brand_type=UN'
    data = {
        'account': account,
        'login_type': '2',
        'password': md5_encode(password),
        'sign': '04E1FEFEDF1936728314CCE4F427FF84',
    }
    req = requests.post(url=url, headers=headers, data=data)
    if '失败' in req.text:
        return '登陆失败，请检查账号密码是否正确！'
    return req.json()['_key']


def plate(key):
    '''
    获取板块列表
    :param key: key
    :return: 板块名称和板块ID
    '''
    plate_list = []
    url = f'http://floor.huluxia.com/category/list/ANDROID/2.0?platform=2&gkey=000000&app_version=4.1.2&versioncode=350&market_id=tool_web&_key={key}&device_code=%5Bd%5Dd5f270d8-fc06-4230-b185-67da7669508b&phone_brand_type=UN&is_hidden=1'
    req = requests.get(url=url, headers=headers)
    for i in req.json()['categories']:
        cat_id = i['categoryID']
        if cat_id != 0 and cat_id != 94:
            title = i['title']
            plate_list.append({'title': title, 'id': cat_id})
    return plate_list


def sign(plate_list, key):
    '''
    签到
    :param plate_list: 板块列表
    :param key: key
    :return: 签到结果
    '''
    mes = []
    for i in plate_list:
        title = i['title']
        cat_id = i['id']
        url = f'http://floor.huluxia.com/user/signin/ANDROID/2.0?platform=2&gkey=000000&app_version=4.1.2&versioncode=350&market_id=tool_web&_key={key}&device_code=%5Bd%5Dd5f270d8-fc06-4230-b185-67da7669508b&phone_brand_type=UN&cat_id={cat_id}'
        data = {'sign': '10F3223E9B9936114F754A20B2EB4D8F'}
        req = requests.post(url=url, headers=headers, data=data)
        mes.append(title + '：' + req.json()['msg'])
    return ''.join(mes)
