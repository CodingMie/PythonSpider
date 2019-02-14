import urllib.request
import json
import time
import random
import requests
from bs4 import BeautifulSoup as bs
from Crypto.Cipher import AES
import base64


def getProxies():
    ProxiesList = []
    with open("ip.txt", 'r', encoding="utf-8") as fin:
        for line in fin:
            proxies = eval(line)
            ProxiesList.append(proxies)
    return ProxiesList


first_param = '{rid:"", offset:"0", total:"true", limit:"20", csrf_token:""}'
second_param = "010001"
third_param = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
forth_param = "0CoJUm6Qyw8W8jud"
proxies_list = getProxies()


def get_params(i):
    if i == 0:
        first_param = '{rid:"", offset:"0", total:"true", limit:"20", csrf_token:""}'
    else:
        offset = str(i * 20)
        first_param = '{rid:"", offset:"%s", total:"%s", limit:"20", csrf_token:""}' % (offset, 'flase')
    iv = "0102030405060708"
    first_key = forth_param
    second_key = 16 * 'F'
    h_encText = AES_encrypt(first_param, first_key, iv)
    h_encText = AES_encrypt(h_encText, second_key, iv)
    return h_encText


def get_encSecKey():
    encSecKey = "257348aecb5e556c066de214e531faadd1c55d814f9be95fd06d6bff9f4c7a41f831f6394d5a3fd2e3881736d94a02ca919d952872e7d0a50ebfa1769a7a62d512f5f1ca21aec60bc3819a9c3ffca5eca9a0dba6d6f7249b06f5965ecfff3695b54e1c28f3f624750ed39e7de08fc8493242e26dbc4484a01c76f739e135637c"
    return encSecKey


def AES_encrypt(text, key, iv):
    pad = 16 - len(text) % 16
    text = text + pad * chr(pad)

    encryptor = AES.new(key.encode('UTF-8'), AES.MODE_CBC, iv.encode('UTF-8'))
    encrypt_text = encryptor.encrypt(text.encode('UTF-8'))
    encrypt_text = base64.b64encode(encrypt_text)
    encrypt_text = encrypt_text.decode('UTF-8')
    return encrypt_text


def getJson(url, params, encSecKey):
    header = {  # 请求头部
        'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Connection': 'close'
    }
    data = {
        "params": params,
        "encSecKey": encSecKey
    }
    #postdata = urllib.parse.urlencode(data).encode('utf8')  # 进行编码
    #request = urllib.request.Request(url, headers=header, data=postdata)
    #reponse = urllib.request.urlopen(request).read().decode('utf8')
    proxies = random.sample(proxies_list, 1)[0]
    try:
        json_dict = requests.post(url, headers=header, data=data, proxies=proxies, timeout=1).json()
    except Exception as e:
        print(e)
        return 0
    return json_dict


def getComment(hot_song_id, title):
    print(title)
    time.sleep(random.uniform(1, 3))
    url = 'http://music.163.com/weapi/v1/resource/comments/R_SO_4_' + hot_song_id + '?csrf_token='  # 歌评url
    # post请求表单数据
    params = get_params(0)
    encSecKey = get_encSecKey()
    json_dict = getJson(url, params, encSecKey)
    if json_dict == 0:
        return
    total_comment = json_dict['total']
    page = int((total_comment/20)+1)
    for x in reversed(range(page)):
        print(x)
        params = get_params(x)
        encSecKey = get_encSecKey()
        json_dict = getJson(url, params, encSecKey)
        if json_dict == 0:
            continue
        if not("comments" in json_dict):
            continue
        comments = json_dict['comments']  # 获取json中的热门评论
        for c in reversed(comments):
            if "beReplied" in c and len(c['beReplied']) > 0 and c["beReplied"][0]['content'] is not None:
                with open("网易云2.txt", "a+", encoding="utf-8") as f:
                    f.write("问题：" + c['beReplied'][0]['content'] + '\n')
                    f.write("回复：" + c['content'] + '\n')
                    f.close()


def getSoup(url):
    header = {  # 请求头部
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    #request = urllib.request.Request(url=url, headers=header, proxies=proxies)
    time.sleep(random.uniform(2, 3))
    #file = urllib.request.urlopen(request)  # 打开url
    try:
        file = requests.get(url, headers=header, timeout=1)
    except Exception as e:
        print(e)
        return 0
    soup = bs(file.text, "lxml")
    return soup


def getSongList(url):
    soup = getSoup(url)
    if soup == 0:
        return
    songul = soup.find("ul", class_="f-hide")
    songlist = songul.find_all("a")
    print("【2】GETSONGLIST")
    for song in songlist:
        song_href = str(song['href'])
        song_id = song_href.partition("=")[2]
        getComment(song_id, title=song.text)


for i in range(10, 36):
    url = 'http://music.163.com/discover/playlist/?order=hot&cat=%E5%8D%8E%E8%AF%AD&limit=35&offset='+str(35*i)
    soup = getSoup(url)
    playlist = soup.find_all(class_="msk")
    for p in playlist:
        print("【1】MAIN")
        playlist_href = str(p['href'])
        url = 'http://music.163.com'+playlist_href
        getSongList(url)
