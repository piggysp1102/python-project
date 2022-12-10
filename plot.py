# _*_ coding:utf-8 _*_
"""
@File     : plot.py
@Project  : airbnb
@Time     : 2022/11/12 20:22
@Author   : MYW
@Software : PyCharm
@License  : (C)Copyright 2018-2028, Taogroup-NLPR-CASIA
@Last Modify Time      @Version     @Desciption
--------------------       --------        -----------
2022/11/12 20:22        1.0             None
"""
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from nltk import word_tokenize
from collections import Counter
import re
import jieba
from wordcloud import WordCloud

china = ""
english = ""

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
df= pd.read_csv('airbnb-SH-listings.csv/listings-locations.csv')
df['neighbourhood'] = df['neighbourhood'].apply(lambda x:x.split("/")[0].strip())
df1 = df.groupby('neighbourhood')['host_id'].count()
plt.pie(x=df1.values,labels=df1.index.values)
plt.show()
plt.savefig("pie.png",dpi=300)
plt.cla()
df2 = df.groupby("room_type")['host_id'].count()
p1 = plt.bar(x=df2.index,height=df2.values)
plt.bar_label(p1)
plt.xlabel("房屋类型")
plt.ylabel("计数")
plt.show()
plt.savefig("bar.png",dpi=300)
plt.cla()
df3 = pd.read_csv("airbnb-SH-listings.csv/listings.csv")
df4 = df3[['host_since','number_of_reviews']]
df4["host_since"] = pd.to_datetime(df4['host_since'])
df4['day_count'] = max(df4['host_since']) - df4['host_since']
print(df4['day_count'].dt.days)
plt.scatter(x=df4['day_count'].dt.days,y=df4['number_of_reviews'])
plt.xlabel("注册时间")
plt.ylabel("评论数")
plt.show()
plt.savefig("scatter.png",dpi=300)
plt.cla()
df5 = df3[['description','number_of_reviews']].sort_values('number_of_reviews',ascending=False).head(int(len(df3)*0.1))
df5 = df5['description'].values.tolist()
print(df5)
for d in df5:
    d = str(d).replace("</b>","").replace("<b>","")
    s = d.split("<br />")
    for i in s:
        ch = re.findall(u"([\u4e00-\u9fff]+)", i)
        if ch:
            china+=i
        else:
            english+=i

# print(china)
# print(english)
stopwords = [line.strip() for line in open('stopwords.txt',encoding='UTF-8').readlines()]
en_words = word_tokenize(english)
ch_words = jieba.cut(china)
ch_words = [i for i in ch_words if i not in stopwords]
en_words = [i for i in en_words if i not in stopwords]
all_words = ch_words+en_words
all_words = Counter(all_words).most_common(100)
print(all_words)

q = dict(all_words)
w = WordCloud(font_path='simhei.ttf',background_color='White').fit_words(q)
# plt.rcParams['font.family'] = ['sans-serif']
# plt.rcParams['font.sans-serif'] = ['SimHei']
plt.imshow(w)
plt.show()
plt.savefig("scatter.png",dpi=300)
# print(words_count)

