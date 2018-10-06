import configparser
import os
import sys
import urllib.parse
import warnings
import firebase_admin
import requests
import pytz
import jieba
import collections
from datetime import datetime
from bs4 import BeautifulSoup
from firebase_admin import credentials, firestore

def set_data(url, db, board_name):
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
    if len(art_info) != 3:
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

    time_format = datetime.strftime(content['date'], '%Y-%m-%d %H:%M:%S')
    doc_ref = db.collection(board_name).document(time_format)
    doc_ref.set(content)

def board_iter(board_name , db, art_num):
    warnings.filterwarnings('ignore')#忽略警告

    url = 'https://www.ptt.cc/bbs/' + board_name + '/index.html'
    index = 'https://www.ptt.cc'
    www = url.replace('https://www.ptt.cc','')
    payload = { #滿18歲驗證 over18.php  f12>network index.html前有over18.php
    'from':www, #要進哪個版
    'yes':'yes' #預設回答
    }
    
    needpage = art_num
    num = needpage / 20
    num = num + 2
    nowpage = 0

    NOT_EXIST = BeautifulSoup('<a>本文已被刪除</a>', 'lxml').a
    rs = requests.session()
    res = rs.post('https://www.ptt.cc/ask/over18', verify=False,data=payload)
    res = rs.get(url, verify=False)

    soup = BeautifulSoup(res.text, 'lxml')  # 要分析物體包含在BeautifulSoup的物件當中
    articles = soup.find_all('div', 'r-ent')
    title = soup.find('a', 'board').getText()
    title = title[3:]
    next_link2 = soup.find('div', 'btn-group-paging').find_all('a', 'btn wide')[1].get('href')

    while(nowpage < needpage):
        url = urllib.parse.urljoin(index, next_link2) # 合出前一頁的網址
        res = rs.post('https://www.ptt.cc/ask/over18', verify=False,data=payload)
        res = rs.get(url, verify=False)
        soup = BeautifulSoup(res.text,'lxml')
        articles = soup.find_all('div', 'r-ent') # 更新articles
        next_link2 = soup.find('div', 'btn-group-paging').find_all('a', 'btn wide')[1].get('href')
        for article in articles:
            nowpage = nowpage + 1
            meta2 = article.find('div', 'title').find('a')or NOT_EXIST  # A or B 前面空則B
            link2 = meta2.get('href')
            link2 = urllib.parse.urljoin(index, link2)
            if(meta2 != NOT_EXIST):
                set_data(link2, db, board_name)

def word_add(content):
        #本函數單純將所有需要分析的字串加總，好進行斷詞
        text = content['title'] + content['context']

        for texti in content['pushtext']:
            text = text + texti
        for texti in content['downtext']:
            text = text + texti
        for texti in content['arrtext']:
            text = text + texti
        return text

def word_freq(board_name, db):
    jieba.set_dictionary('dict.txt.big') #使用jieba的繁體中文字典針對繁體中文做更好的斷詞
    art_ref = db.collection(board_name)
    start = datetime(2018, 4, 1) #可以限定時間範圍或篇數
    start = pytz.timezone('Asia/Taipei').localize(start)
    end = datetime(2018, 4, 30)
    end = pytz.timezone('Asia/Taipei').localize(end)
    #query = art_ref.where(u'date', u'>', start).where(u'date', u'<', end).order_by(u'date', direction=firestore.Query.DESCENDING)
    query = art_ref.order_by(u'date', direction=firestore.Query.DESCENDING).limit(1000) #取1000篇
    results = query.get()

    word_count = collections.Counter()
    for doc in results:
        content = doc.to_dict() #將JSON轉成字典
        content['date'] = content['date'].replace(tzinfo = pytz.utc).astimezone(pytz.timezone('Asia/Taipei')) #手動設定時區
        dt_index = datetime.strftime(content['date'], '%Y-%m-%d') #為了可以操作timeseries將datetime物件轉換成string來存取timeseries
        text = word_add(content) #將所有要分析的文字加總
        counter = word_counter(text)
        word_count = word_count + counter
    
    common_text = ''
    text_wordcd = {}
    for word, times in word_count.most_common(100):#從counter的字典中取出找頻率最高的前三個單詞，加入word_list中作為搜尋的依據
        common_text = common_text + '{0: <10}{1: <2}{2: <5}{3}'.format(word, ' ', str(times), '\n')
        text_wordcd.update({word: times})

    common_text_dict = {'common_text':common_text, #存入資料庫
                        'text_wordcd': text_wordcd}
    doc_ref = db.collection(u'big_analyze').document(board_name)
    doc_ref.set(common_text_dict)


def word_counter(text):
    stopwords = [line.strip() for line in open('stopwords.txt', 'r', encoding='utf-8').readlines()]        
    text = jieba.cut(text) #斷詞
    word_count = collections.Counter() #collection的counter統計在一個物件中重複的子成員的數量，並且支持+-運算
    for word in text:
        if(len(word) > 1 and word != '\r\n' and word not in stopwords): #這裡不直接使用counter是因為counter會把長度1的字串也算進去
            word_count[word] = word_count[word] + 1 #進行次數統計
    return word_count

    
if __name__ == '__main__':
    cred = credentials.Certificate('pycrawler-ffd3634e0b28.json')
    default_app = firebase_admin.initialize_app(cred)
    db = firestore.client()

    board_iter('Baseball', db, 1000)
    word_freq('Baseball',db)
    board_iter('Steam', db, 1000)
    word_freq('Steam',db)
    board_iter('LoL', db, 1000)
    word_freq('LoL',db)
    board_iter('C_Chat', db, 1000)
    word_freq('C_Chat',db)

    time_now = datetime.now()
    time_now = pytz.timezone('Asia/Taipei').localize(time_now)
    time_update = {'update_time' : time_now}
    doc_ref = db.collection(u'database_updatetime').document('update_time')
    doc_ref.set(time_update)

    # python .\database.py