import requests
import json
import time
from bs4 import BeautifulSoup as bs
import random
import threading


def getComment(url, title):
    headers={
        'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Mobile Safari/537.36'
    }
    page = requests.get(url, headers=headers)
    soup = bs(page.text, "lxml")
    text = soup.find("div", class_="content-text")
    if text is None:
        return

    #funny = soup.find(class_="laugh-comment")
    #f.write(funny.text + '\n')
    '''
    comment = soup.find_all(class_="main-text")
    if len(comment) > 5:
        comment_num = 5
    else:
        comment_num = len(comment)
    f = open(str(title)+".txt", "a+", encoding="utf-8")
    for i in range(comment_num):
        f.write("帖子：" + text.text + '\n')
        f.write("回复：" + comment[i].text + '\n')
    f.close()
    print(title+"END")
    '''
    f = open(str(title) + ".txt", "a+", encoding="utf-8")
    f.write("帖子：" + text.text.strip() + '\n')
    f.close()


def getVisit(url_value, title):
    for a in range(1, 20):
        #print("[START]:" + str(a) + " " + title)
        url_visit = url_value + str(a) + "/"
        headers = {
            'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Mobile Safari/537.36'
        }
        time.sleep(random.uniform(1, 3))
        try:
            file = requests.get(url_visit, headers=headers)
            #time.sleep(2)
            list = json.loads(file.text)
        except Exception as e:
            print(e)
            continue
        for i in list:
            uid = i['data']['id']
            url = 'https://www.qiushibaike.com/article/'+str(uid)
            time.sleep(random.random())
            getComment(url, title)


def getPage(url_value, title):
    for a in range(20, 35):
        url_visit = str(url_value).format(str(a))
        headers = {
            'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Mobile Safari/537.36'
        }
        time.sleep(random.uniform(1, 3))
        try:
            file = requests.get(url_visit, headers=headers)
            #time.sleep(2)
            soup = bs(file.text,"lxml")
        except Exception as e:
            print(e)
            continue
        content_list = soup.find_all(class_="newArticle")
        for content in content_list:
            number = content.find(class_="laugh-comment")
            if number is None:
                continue
            number = int(number.text.split(" ")[0])
            if number > 100:
                uid = content.find(class_="content-text").contents[1]
                uid = uid['href']
                url = 'https://www.qiushibaike.com' + str(uid)
                getComment(url, title)







if __name__ == "__main__":
    '''
    url_list = ['https://www.qiushibaike.com/?page=',
      'https://www.qiushibaike.com/hot/?page=','https://www.qiushibaike.com/text/?page=']
    title_list = ["", "历史2", "历史3", "历史4"]
    thread_list = []
    for (url, title) in zip(url_list, title_list):
        my_thread = threading.Thread(target=getVisit, args=(url, title))
        my_thread.setDaemon(True)
        thread_list.append(my_thread)
    for my_thread in thread_list:
        my_thread.start()
    for my_thread in thread_list:
        my_thread.join()
    print("++++++++++++++++END++++++++++++++++++")
    url = 'https://www.qiushibaike.com/history/'
    title = "穿越"
    for i in range(20):
        getPage(url, title)
    '''

    url = 'https://www.qiushibaike.com/textnew/page/{}/?s=5106648'
    title = "新鲜"
    getPage(url, title)

