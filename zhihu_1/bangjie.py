from lxml import html
import requests
import json
import re
import time


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

    def getComments(self, id, page):  # id（字符串类型）：某条微博的id，page（整型）：评论翻页参数
        url = 'https://m.weibo.cn/api/comments/show?id=' + id + '&page=' + str(page)
        response = requests.get(url)
        ob_json = json.loads(response.text)
        if ob_json['ok'] == 1:
            list_comments = ob_json['data']['hot_data']
            return list_comments

    def printAllTopic(self, page):
        list_cards = self.getWeibo('1713926427', page)
        # 遍历当页所有微博，输出内容，并根据id查找输出热门评论
        if list_cards:
            for card in list_cards:
                if card['card_type'] == 9:  # 过滤出微博，card_type=9的是微博card，card_type=11的是推荐有趣的人
                    id = card['mblog']['id']
                    text = card['mblog']['text']
                    if re.search('___', text) != None:  # 用正则匹配，将博文有下划线的微博过滤出来，有下划线的是“话题微博”
                        tree = html.fromstring(text)
                        text = tree.xpath('string(.)')  # 用string函数过滤掉多余标签
                        print(u"### 话题: " + text + '\n')
                        with open("榜姐.txt", "a+", encoding="utf-8") as f:
                            f.write('问题：' + text + '\n');
                            f.close()
                        # 根据微博id获取热门评论，并输出
                        list_comments = crawl_weibo.getComments(id, 1)  # 热门评论只需要访问第一页
                        if list_comments:
                            count_hotcomments = 1
                            for comment in list_comments:
                                if 'pic' in comment:
                                    continue
                                if 'reply_text' in comment:
                                    continue
                                text = comment['text']  # 评论内容
                                tree = html.fromstring(text)
                                text = tree.xpath('string(.)')  # 用string函数过滤掉多余标签
                                # 输出评论数据
                                print(text + '\n')
                                count_hotcomments = count_hotcomments + 1
                                with open("榜姐.txt", "a+", encoding="utf-8") as f:
                                    f.write('回复：' + text + '\n');
                                    f.close()
                        else:
                            break;
        else:
            return 1


# 实例化爬虫类并调用成员方法进行输出
crawl_weibo = CrawlWeibo()
page = 1;
while 1:
    time.sleep(0.5);
    res = crawl_weibo.printAllTopic(page)
    if res == 1:
        break;
    page = page+1

print("***************END")