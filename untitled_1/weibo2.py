from lxml import html
import requests
import json
import time
import re


class CrawlWeibo:

    # 获取指定博主的所有微博card的list
    def getWeibo(self, id, page):  # id（字符串类型）：博主的用户id，page（整型）：微博翻页参数

        url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=' + id + '&containerid=107603' + id + '&page=' + str(
            page)
        response = requests.get(url)
        ob_json = json.loads(response.text)
        if ob_json['ok'] == 1:
            list_cards = ob_json['data']['cards']
            return list_cards  # 返回本页所有的cards

    # 返回某条微博的评论的list
    def getComments(self, id, page):  # id（字符串类型）：某条微博的id，page（整型）：评论翻页参数
        url = 'https://m.weibo.cn/api/comments/show?id=' + id + '&page=' + str(page)
        response = requests.get(url)
        ob_json = json.loads(response.text)
        if ob_json['ok'] == 1:
            list_comments = ob_json['data']['data']
            return list_comments

    def printAllTopic(self, page):
        list_cards = self.getWeibo('5175429989', page)
        if list_cards:
        # 遍历当页所有微博，输出内容，并根据id查找输出热门评论
            for card in list_cards:
                if card['card_type'] == 9:  # 过滤出微博，card_type=9的是微博card，card_type=11的是推荐有趣的人
                    id = card['mblog']['id']
                    text = card['mblog']['text']
                    tree = html.fromstring(text)
                    text = tree.xpath('string(.)')  # 用string函数过滤掉多余标签
                   # with open("test.txt", "a+", encoding="utf-8") as f:
                    #    f.write(u"### 微博内容: " + text + '\n');
                     #   f.close()
                    print(u"### 微博内容: " + text + '\n')
                    # 根据微博id获取热门评论，并输出
                    count = 1;
                    while 1:
                        time.sleep(0.8);
                        list_comments = crawl_weibo.getComments(id, count)  # 热门评论只需要访问第一页
                        if list_comments:
                            count_hotcomments = 1
                            for comment in list_comments:
                                if comment['user']['id'] == 5175429989:
                                    if not("reply_text" in comment):
                                        continue;
                                    text = comment['text']  # 评论内容
                                    tree = html.fromstring(text)
                                    text = tree.xpath('string(.)')  # 用string函数过滤掉多余标签
                                    text = text.partition(":")[2];
                                    name_user = comment['user']['screen_name']  # 评论者的用户名
                                    reply_text = comment['reply_text']  # 评论内容
                                    tree = html.fromstring(reply_text)
                                    reply_text = tree.xpath('string(.)')  # 用string函数过滤掉多余标签
                                    if reply_text.partition(":")[2] != "":
                                        reply_text = reply_text.partition(":")[2]
                                            # 输出评论数据
                                    print('问题：' + reply_text + '\n')
                                    print('回复：'+text + '\n')
                                    with open("小冰3.txt", "a+", encoding="utf-8") as f:
                                        f.write('问题：' + reply_text + '\n');
                                        f.write('回复：'+text + '\n');
                                        f.close()

                                    count_hotcomments = count_hotcomments + 1
                        else:
                            break;
                        count = count + 1

                    print( '***')
        else:
            return 1


    def printAllResponse(self, page, user_id):
        list_cards = self.getWeibo(str(user_id), page)
        if list_cards:
            for card in list_cards:
                if card['card_type'] == 9:  # 过滤出微博，card_type=9的是微博card，card_type=11的是推荐有趣的人
                    id = card['mblog']['id']
                    text = card['mblog']['text']
                    tree = html.fromstring(text)
                    text = tree.xpath('string(.)')  # 用string函数过滤掉多余标签
                    print(u"### 微博内容: " + text + '\n')
                    # 根据微博id获取热门评论，并输出
                    count = 1
                    while 1:
                        time.sleep(0.8)
                        list_comments = crawl_weibo.getComments(id, count)
                        if list_comments:
                            for comment in list_comments:
                                if not("reply_text" in comment):
                                    continue
                                text = comment['text']  # 评论内容
                                tree = html.fromstring(text)
                                text = tree.xpath('string(.)')  # 用string函数过滤掉多余标签
                                text = text.partition(":")[2]
                                    #name_user = comment['user']['screen_name']  # 评论者的用户名
                                reply_text = comment['reply_text']  # 评论内容
                                tree = html.fromstring(reply_text)
                                reply_text = tree.xpath('string(.)')  # 用string函数过滤掉多余标签
                                if ((text.find("网页链接")!= -1) or (reply_text.find("网页链接") != -1)
                                        or text == "" or reply_text == "" or len(text)> 30 or len(reply_text) > 30):
                                    continue
                                if reply_text.partition(":")[2] != "":
                                    reply_text = reply_text.partition(":")[2]
                                        # 输出评论数据
                                print('问题：' + reply_text + '\n')
                                print('回复：'+text + '\n')
                                with open(str(user_id)+".txt", "a+", encoding="utf-8") as f:
                                    f.write('问题：' + reply_text + '\n')
                                    f.write('回复：'+text + '\n')
                                    f.close()
                        else:
                            break
                        count = count + 1

                    print('***')
        else:
            return 1

# 实例化爬虫类并调用成员方法进行输出


if __name__ == '__main__':
    crawl_weibo = CrawlWeibo()
    page = 1
    id = input("id")
    while 1:
        time.sleep(0.5)
        res = crawl_weibo.printAllResponse(page, id)
        if res == 1:
            break
        page = page+1

    print("***************END")


