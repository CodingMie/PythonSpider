import requests
import json
import time
import re
from bs4 import BeautifulSoup as bs
import random
from Proxy import getProxy

def getComment(url,title):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
    }
    cookies = {
        'cookie': 'bid=LoW-gcbNw4s; gr_user_id=89963d41-6d51-4aa6-80a5-2ea3b589188e; _vwo_uuid_v2=D79228CDBBAEE6BC0D96FF7E6E4BFD918|03ccdfcc181f1981879f36ec34eed339; ap=1; ps=y; ll="108288"; viewed="5414391_26986954_26958126_3360807_1103015"; _ga=GA1.3.1103338133.1528706829; ct=y; FTAPI_AT=FUCKIE; FTAPI_BLOCK_SLOT=FUCKIE; FTAPI_ST=FUCKIE; FTAPI_PVC=1029201-3-jiuicm47; ue="544286175@qq.com"; push_noty_num=0; push_doumail_num=0; _ga=GA1.2.1103338133.1528706829; _gid=GA1.3.2002265729.1530587937; _gid=GA1.2.917029490.1530595974; dbcl2="49393504:26A20uechgY"; Hm_lvt_6d4a8cfea88fa457c3127e14fb5fabc2=1530587937,1530587940,1530605852,1530605854; ck=jhcK; __utma=30149280.1103338133.1528706829.1530672555.1530672555.1; __utmc=30149280; __utmz=30149280.1530672555.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmv=30149280.4939; __utmb=30149280.7.5.1530672555; frodotk="6f9699218b86ac684ec3cb64a2940538"'
    }
    time.sleep(random.uniform(1, 3))
    page = requests.get(url, cookies=cookies, headers=headers)
    soup = bs(page.text, "lxml")
    print(title)
    comment = soup.find_all(class_="comment")
    for c in comment:
        with open("豆瓣2.txt", "a+", encoding="utf-8") as f:
            f.write("问题：" + title + '\n')
            f.write('回复：' + c.find("p").text.strip() + '\n')
            f.close()


for a in range(20, 40):
    url_visit = 'https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=%E7%94%B5%E8%A7%86%E5%89%A7&start={}'.format(a*20)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
    }
    cookies = {
        'cookie':'bid=LoW-gcbNw4s; gr_user_id=89963d41-6d51-4aa6-80a5-2ea3b589188e; _vwo_uuid_v2=D79228CDBBAEE6BC0D96FF7E6E4BFD918|03ccdfcc181f1981879f36ec34eed339; ap=1; ps=y; ll="108288"; viewed="5414391_26986954_26958126_3360807_1103015"; __yadk_uid=96fRnsrWV5DjWpq8rcL8J4Qn6mtVS6ho; ct=y; ue="544286175@qq.com"; push_noty_num=0; push_doumail_num=0; _ga=GA1.2.1103338133.1528706829; _gid=GA1.2.917029490.1530595974; dbcl2="49393504:26A20uechgY"; ck=jhcK; __utma=30149280.1103338133.1528706829.1530672555.1530672555.1; __utmc=30149280; __utmz=30149280.1530672555.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmv=30149280.4939; __utmb=30149280.7.5.1530672555; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1530672560%2C%22https%3A%2F%2Fwww.douban.com%2Fgroup%2Ftopic%2F119741333%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=223695111.1103338133.1528706829.1530608765.1530672560.3; __utmb=223695111.0.10.1530672560; __utmc=223695111; __utmz=223695111.1530672560.3.3.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/group/topic/119741333/; _pk_id.100001.4cf6=879b2f22caee8dc8.1530587957.3.1530672646.1530608775.'
    }
    #try:
    file = requests.get(url_visit, headers=headers, cookies=cookies).json()   #这里跟之前的不一样，因为返回的是 json 文件
    #except:
        #print("lala")
        #continue
    time.sleep(random.uniform(2, 3))

    for i in range(20):
        dict=file['data'][i]   #取出字典中 'data' 下第 [i] 部电影的信息
        title=dict['title']
        urlname=dict['url']
        time.sleep(random.uniform(1, 2))
        getComment(urlname, title)
