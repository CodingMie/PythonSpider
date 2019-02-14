import requests
from Proxy import getProxy
from bs4 import BeautifulSoup as bs
import time
import random


#proxies_list = getProxy()


def get_comment(url):
    time.sleep(random.uniform(1, 3))
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'Connection': 'close'
    }
    cookies = {
        'cookie':'bid=LoW-gcbNw4s; gr_user_id=89963d41-6d51-4aa6-80a5-2ea3b589188e; _vwo_uuid_v2=D79228CDBBAEE6BC0D96FF7E6E4BFD918|03ccdfcc181f1981879f36ec34eed339; __yadk_uid=PfFXSdtlw7MOusCyCNgwYevgeDaPS5uA; ap=1; ps=y; ll="108288"; Hm_lvt_16a14f3002af32bf3a75dfe352478639=1528882764; viewed="5414391_26986954_26958126_3360807_1103015"; ct=y; ue="544286175@qq.com"; push_noty_num=0; push_doumail_num=0; _ga=GA1.2.1103338133.1528706829; dbcl2="49393504:26A20uechgY"; ck=jhcK; __utmc=30149280; __utmz=30149280.1530672555.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=30149280.4939; __utma=30149280.1103338133.1528706829.1530682842.1530687762.4; _pk_ref.100001.3ac3=%5B%22%22%2C%22%22%2C1530691257%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.3ac3=*; __utma=81379588.1103338133.1528706829.1530607039.1530691258.2; __utmc=81379588; __utmz=81379588.1530691258.2.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03=0ceb835d-446c-4e89-b6cd-c7aec8699e2f; gr_cs1_0ceb835d-446c-4e89-b6cd-c7aec8699e2f=user_id%3A1; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03_0ceb835d-446c-4e89-b6cd-c7aec8699e2f=true; _pk_id.100001.3ac3=ba82f70944f780f4.1530607039.2.1530694988.1530608764.; __utmb=30149280.96.4.1530689947775; __utmb=81379588.49.10.1530691258'
    }
    #proxies = random.sample(proxies_list, 1)[0]
    try:
        page = requests.get(url, headers=headers, cookies=cookies)
    except Exception as e:
        print(e)
        return
    soup = bs(page.text, "lxml")
    title = soup.find(property='v:itemreviewed')
    comment = soup.find_all(class_="comment-content")
    for c in comment:
        with open("豆瓣读书.txt", "a+", encoding="utf-8") as f:
            f.write("问题：" + title.text.strip() + '\n')
            f.write('回复：' + c.text.strip() + '\n\n')
            f.close()


def get_book():
    for a in range(3, 50):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        }
        url = 'https://book.douban.com/tag/%E5%A4%96%E5%9B%BD%E6%96%87%E5%AD%A6?start={}&type=T'.format(a*20)
        try:
            file = requests.get(url, headers=headers).text
        except Exception as e:
            print(e)
            continue
        page = bs(file, "lxml")
        book_list = page.find_all(class_='nbg')
        for book in book_list:
            book_url = book['href']
            get_comment(book_url)


if __name__ == "__main__":
        get_book()
