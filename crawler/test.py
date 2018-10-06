import configparser
import os
import sys
import firebase_admin
import pytz
import warnings
import pandas as pd
import requests
import re
import numpy as np
import collections
from bs4 import BeautifulSoup
from datetime import datetime
from firebase_admin import credentials, firestore

def set_data(url):
    content = {'title': '',
                'link': '',
                'push': 0,
                'down': 0,
                'arr': 0,
                'allpush': 0,
                'date': '',
                'author': '',
                'pushtext': [],
                'downtext': [],
                'arrtext': [],
                'context': ''}
                
    index = 'https://www.ptt.cc'
    NOT_EXIST = BeautifulSoup('<a>本文已被刪除</a>', 'lxml').a
    warnings.filterwarnings('ignore')  # 忽略警告
    index = 'https://www.ptt.cc'
    www = url.replace('https://www.ptt.cc', '')

    payload = {  # 滿18歲驗證 over18.php  f12>network index.html前有over18.php
        'from': www,  # 要進哪個版
        'yes': 'yes'  # 預設回答
    }

    rs = requests.session()
    res = rs.post('https://www.ptt.cc/ask/over18',verify=False, data=payload)
    res = rs.get(url, verify=False)

    soup = BeautifulSoup(res.text, 'lxml')  # 要分析物體包含在BeautifulSoup的物件當中
    arts = soup.find_all('div', 'push') #回傳結果是list 可以加上[任意數字] 來顯示list中的第幾筆資料 [].text 加上text可以省

    for art in arts:
        text = art.find('span', 'push-content')
        if not text:
            return 0
        text = text.getText()
        text = text[2:]
        push = art.find('span', 'push-tag').getText()
        if push[0] == '推':
            content['push'] = content['push'] + 1
            content['pushtext'].append(text)
        elif push[0] == '噓':
            content['down'] = content['down'] + 1
            content['downtext'].append(text)
        else:
            content['arr'] = content['arr'] + 1
            content['arrtext'].append(text)

    art_info = soup.find_all('div', 'article-metaline')
    print(len(art_info))
    if not art_info:
        return 0
    if not art_info[1]:
        return 0

    print(url)
    print(art_info[0].getText())

    content['author'] = art_info[0].getText()
    content['author'] = content['author'][2:]
    content['title'] = art_info[1].getText()
    content['title'] = content['title'][2:]
    content['date'] = art_info[2].getText()
    content['date'] = content['date'][2:]
    content['link'] = url
    content['allpush'] = content['push'] + content['down'] + content['arr']

    context = soup.find(id="main-content").text #取得內文
    target_context = u'※ 發信站: 批踢踢實業坊(ptt.cc),'
    context = context.split(target_context) #去除掉 target_content
    context = context[0].split(content['date'])
    main_context = context[1].replace('--', '') #去除掉文末 --
    dt = datetime.strptime(content['date'], '%a %b %d %X %Y')
    dt = pytz.timezone('Asia/Taipei').localize(dt)
    content['date'] = dt
    content['context'] = main_context

if __name__ == '__main__':
    set_data('https://www.ptt.cc/bbs/Baseball/M.1526546177.A.4EE.html')