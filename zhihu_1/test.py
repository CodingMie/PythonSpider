import jieba
import matplotlib.pyplot as plt
import jieba.analyse
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from scipy.misc import imread


text = open('mylove.txt', encoding="utf-8").read()
jieba.add_word("大老师")
jieba.add_word("大张伟")
jieba.add_word("阳光彩虹小白马")
jieba.add_word("人间精品")
jieba.add_word("DM48")
jieba.add_word("倍儿爽")
jieba.del_word("张伟")
jieba.del_word("抄袭")
jieba.del_word("首歌")
jieba.cut(text)
jieba.analyse.set_stop_words('停用词.txt')
tags = jieba.analyse.extract_tags(text, topK=200, withWeight=True)
words_ls = jieba.cut(text, cut_all=False)
stopwords = []
word_list = []
for word in open('停用词.txt', 'r', encoding="utf-8"):
    stopwords.append(word.strip())
for seg in words_ls:
    if seg not in stopwords:
            word_list.append(seg)


words = []
for v, n in tags:
    words.append(str(v))
words_split = " ".join(word_list)
bg = imread('bg11.jpg')
image_colors = ImageColorGenerator(bg)
wc = WordCloud(mask=bg, font_path="simhei.ttf",background_color="white")    # 字体这里有个坑，一定要设这个参数。否则会显示一堆小方框wc.font_path="simhei.ttf"   # 黑体

my_wordcloud = wc.generate(words_split)
plt.imshow(wc)
# 关闭坐标轴
plt.axis('off')
# 绘制词云
plt.figure()
plt.imshow(wc.recolor(color_func=image_colors))
plt.axis('off')
# 保存图片
wc.to_file('xbm1.png')

#wc.to_file('zzz1.png') # 保存图片文件