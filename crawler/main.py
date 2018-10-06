import os
import sys
import requests
import urllib.parse
import configparser
import warnings
import firebase_admin
import pytz
import pandas as pd
import matplotlib.pyplot as plt
import jieba
import numpy as np
import collections
import matplotlib
import random
import re
from bs4 import BeautifulSoup
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QDialog
from PyQt5.QtGui import QFont, QImage
from PyQt5.QtCore import QThread, pyqtSignal, QObject, pyqtSlot, QCoreApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
from firebase_admin import credentials, firestore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from database import board_iter, word_freq
from snownlp import SnowNLP
from datetime import datetime, timedelta
from wordcloud import WordCloud
from mainwindow import Ui_MainWindow #主介面
from boardlist import Ui_BoardList #看板列表
from dialog import Ui_Dialog #check視窗1
from dialog2 import Ui_Dialog2 #check視窗2
from textURL import Ui_textURL

#主視窗
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self) #初始化ui
        self.db_init()
        self.stopwords_list()
        self.get_board_content()
        self.set_board_content(self.content, self.sp_pushtext, self.graphicscene)
        self.set_board_content_tab3(self.wordcd2_text[0], self.wordcd2_graphic)

        self.text_exist_url = ''

        self.pushButton.clicked.connect(self.board_list_window) #將按紐跟函式連結
        self.pushButton_16.clicked.connect(self.refresh_widget)
        self.pushButton_17.clicked.connect(self.set_art_timeseries)
        self.pushButton_18.clicked.connect(self.set_word_timeseries)
        self.pushButton_19.clicked.connect(self.text_url_window)
        self.pushButton_4.clicked.connect(self.self_board_set)

        jieba.set_dictionary('dict.txt.big') #使用jieba的繁體中文字典針對繁體中文做更好的斷詞

    def db_init(self):
        #初始化資料庫連線
        cred = credentials.Certificate('pycrawler-ffd3634e0b28.json')
        default_app = firebase_admin.initialize_app(cred)
        self.db = firestore.client() #資料庫連線

        #顯示資料庫更新時間
        updatetime = self.db.collection('database_updatetime').document('update_time')
        updatetime = updatetime.get()
        updatetime = updatetime.to_dict()
        updatetime['update_time'] = updatetime['update_time'].replace(tzinfo = pytz.utc).astimezone(pytz.timezone('Asia/Taipei')) 
        updatetime = datetime.strftime(updatetime['update_time'], "%Y-%m-%d %H:%M:%S %Z")
        self.label_20.setText('資料庫最終更新時間 : ' + updatetime)

    def stopwords_list(self):
        #從檔案讀取stopwords的list
        self.stopwords = [line.strip() for line in open('stopwords.txt', 'r', encoding='utf-8').readlines()]

    def refresh_widget(self):
        #刷新tab widget
        #這裡因為在另一個線程操作了QWidget，所以會噴警告出來(Qt不希望你在別的線程操作GUI的物件，那樣不安全)
        #使用線程的目的: pyqt的UI跟運算是放在同一個線程執行，因此UI在進行邏輯運算時會卡住，為了解決這個問題需要使用多線程處理運算
        self.board_name = str(self.comboBox.currentText())
        self.art_num = int(self.lineEdit_6.text())
        self.update_board_thread = BoardUpdate(board_name = self.board_name, db = self.db, stopword = self.stopwords, art_num = self.art_num,
                                                wordcdwidth_1 = int(self.graphicsView_5.width()-2), wordcdheight_1 = int(self.graphicsView_5.height()-2),
                                                wordcdwidth_2 = int(self.graphicsView.width()-2), wordcdheight_2 = int(self.graphicsView.height()-2))
        self.thread = QThread() #創造一個線程
        self.update_board_thread.update_content.connect(self.set_board_content) #將信號跟函式連結
        self.update_board_thread.update_content_tab3.connect(self.set_board_content_tab3)
        self.update_board_thread.moveToThread(self.thread) #將QObject移動到另一個線程
        self.update_board_thread.finished.connect(self.thread.quit) #當發出結束信號的時候就離開線程
        self.thread.started.connect(self.update_board_thread.run)
        self.thread.start() #開始跑給線程執行的程式

    def board_list_window(self):
        #打開BoardList()視窗
        self.new_window = BoardList()
        self.new_window.show()

    def open_webpage(self, url):
        #打開WebView視窗
        self.web_view = WebView(parent = self, url = url)
        self.web_view.show()
    
    def text_url_window(self):
        #打開關鍵字出現的視窗
        self.text_url_window = textURL(parent = self, text = self.text_exist_url)
        self.text_url_window.show()

    def get_board_content(self):
        self.board_name = str(self.comboBox.currentText())

        art_ref = self.db.collection(self.board_name) #取得collection(firestore存資料的集合)
        query = art_ref.order_by('date', direction=firestore.Query.DESCENDING).limit(100) #限制範圍
        results = query.get() #get的資料會存在query中，可以用foreach進行遍歷
        self.content = []
        n = 0

        for doc in results:
            dbdt = doc.to_dict() #將JSON檔案轉成dict
            #抓下來的日期時區是UTC+0，為了可以很好的連結關於時間的功能需要轉成台灣時區(UTC+8)
            dbdt['date'] = dbdt['date'].replace(tzinfo = pytz.utc).astimezone(pytz.timezone('Asia/Taipei')) 
            if(n < 3):
                self.content.append(dbdt)
                n = n + 1 #抓3筆資料
            else:
                if(dbdt['allpush'] > self.content[0]['allpush']):
                    self.content[2] = self.content[1]
                    self.content[1] = self.content[0]
                    self.content[0] = dbdt

        self.sp_pushtext = [] 
        self.sp_pushtext.append(self.word_freq(self.content[0])) #此功能會隨機3條挑選含有出現頻率高的字詞的推噓文顯示
        self.sp_pushtext.append(self.word_freq(self.content[1]))
        self.sp_pushtext.append(self.word_freq(self.content[2]))

        self.graphicscene = []
        self.graphicscene.append(self.wordcloud_plot(self.content[0]))
        self.graphicscene.append(self.wordcloud_plot(self.content[1]))
        self.graphicscene.append(self.wordcloud_plot(self.content[2]))

        doc_ref = self.db.collection('big_analyze').document(self.board_name)
        docs = doc_ref.get()
        docs = docs.to_dict() #獲得資料
        self.wordcd2_text = [docs['common_text'], docs['text_wordcd']] #直接從欄位取出
        self.wordcd2_graphic = self.wordcloud_plot(content = 0, flag = 1) #文字雲產生

    def set_board_content(self, content, sp_pushtext, graphicscene):
        #把得到的資料SET上去
        self.groupBox_3.setTitle(self.board_name) #設定看板名稱

        self.label_4.setText(content[0]['title'])
        self.label_4.setFont(QFont("Microsoft JhengHei",16)) #不設定字型的話這物件會根據系統預設的字型還有大小走，所以要規定字型
        self.label_3.setText('推文數: ' + str(content[0]['push']))
        self.label_3.setFont(QFont("Microsoft JhengHei",12)) 
        self.label_1.setText('噓文數: ' + str(content[0]['down']))
        self.label_1.setFont(QFont("Microsoft JhengHei",12)) 
        self.label_2.setText('總推文數: ' + str(content[0]['allpush']))
        self.label_2.setFont(QFont("Microsoft JhengHei",12)) 
        self.pushButton_1.clicked.connect(lambda:self.open_webpage(content[0]['link']))
        self.textBrowser_1.setText(sp_pushtext[0])
        self.textBrowser_1.setFont(QFont("Microsoft JhengHei",12)) 
        self.graphicsView_5.setScene(graphicscene[0])
        self.graphicsView_6.show()
        
        #下面的代碼以此類推，有問題可以參照上方
        self.label_6.setText(content[1]['title'])
        self.label_6.setFont(QFont("Microsoft JhengHei",16)) 
        self.label_7.setText('推文數: ' + str(content[1]['push']))
        self.label_7.setFont(QFont("Microsoft JhengHei",12)) 
        self.label_8.setText('噓文數: ' + str(content[1]['down']))
        self.label_8.setFont(QFont("Microsoft JhengHei",12)) 
        self.label_5.setText('總推文數: ' + str(content[1]['allpush']))
        self.label_5.setFont(QFont("Microsoft JhengHei",12)) 
        self.pushButton_2.clicked.connect(lambda:self.open_webpage(content[1]['link']))
        self.textBrowser_2.setText(sp_pushtext[1])
        self.textBrowser_2.setFont(QFont("Microsoft JhengHei",12)) 
        self.graphicsView_6.setScene(graphicscene[1])
        self.graphicsView_6.show()

        self.label_10.setText(content[2]['title'])
        self.label_10.setFont(QFont("Microsoft JhengHei",16)) 
        self.label_11.setText('推文數: ' + str(content[2]['push']))
        self.label_11.setFont(QFont("Microsoft JhengHei",12)) 
        self.label_12.setText('噓文數: ' + str(content[2]['down']))
        self.label_12.setFont(QFont("Microsoft JhengHei",12)) 
        self.label_9.setText('總推文數: ' + str(content[2]['allpush']))
        self.label_9.setFont(QFont("Microsoft JhengHei",12)) 
        self.pushButton_3.clicked.connect(lambda:self.open_webpage(content[2]['link']))
        self.textBrowser_3.setText(sp_pushtext[2])
        self.textBrowser_3.setFont(QFont("Microsoft JhengHei",12)) 
        self.graphicsView_7.setScene(graphicscene[2])
        self.graphicsView_7.show()

    def set_board_content_tab3(self, wordcd2_text, wordcd2_graphic):
        #更新整版文字分析的部分
        self.textBrowser.setText(wordcd2_text)
        self.textBrowser.setFont(QFont("Microsoft JhengHei",12)) #設定字型
        self.graphicsView.setScene(wordcd2_graphic)
        self.graphicsView.show()

    def word_freq(self, content):
        #此函數取得該篇文章出現頻率最多的單詞，然後將有出現該單詞的推文隨機的挑出3條
        if(content['allpush'] < 3): #推文數量過少的處理，直接顯示所有推文
            if(content['push'] == 0 and content['down'] == 0 and content['arr'] == 0):
                text = '沒有推文'
                return text
            else:
                text = ''
                for push in content['pushtext']:
                    text = text + push
                for down in content['downtext']:
                    text = text + down
                for arr in content['arrtext']:
                    text = text + arr
                return text
        
        text = self.word_add(content) #加總所有部分的文字
        text = jieba.cut(text) #斷詞
        word_count = collections.Counter() #collection的counter統計在一個物件中重複的子成員的數量，並且支持+-運算
        for word in text: 
            if(len(word) > 1 and word != '\r\n' and word not in self.stopwords): #這裡不直接使用counter是因為counter會把長度1的字串也算進去
                word_count[word] = word_count[word] + 1 #進行次數統計

        n = 0
        word_list = []
        for word, times in word_count.most_common(3):#從counter的字典中取出找頻率最高的前三個單詞，加入word_list中作為搜尋的依據
            word_list.append(word) 
            n = n + 1
            if(n >= 3):
                n = 0
                break
        texti = ''
        for push in content['pushtext']: #搜尋推文 噓文 箭頭文
            if(push.find(word_list[random.randint(0, 2)][0]) != -1 and len(push) > 5): #隨機從word_list中取出一種單詞，如果該推文中有出現該單詞就加入回傳的字串
               n = n + 1
               texti = texti + push +'\n'
               if(n == 3):
                   break
        if(n < 3):
            for down in content['downtext']:
                if(down.find(word_list[random.randint(0, 2)][0]) != -1 and len(down) > 5):
                    n = n + 1
                    texti = texti + down +'\n'
                    if(n == 3):
                        break
        if(n < 3):
            for arr in content['arrtext']:
                if(arr.find(word_list[random.randint(0, 2)][0]) != -1 and len(arr) > 5):
                    n = n + 1
                    texti = texti + arr +'\n'
                    if(n == 3):
                        break
        return texti

    def word_add(self, content):
        #本函數單純將所有需要分析的字串加總，好進行斷詞
        text = content['title'] + content['context']

        for texti in content['pushtext']:
            text = text + texti
        for texti in content['downtext']:
            text = text + texti
        for texti in content['arrtext']:
            text = text + texti
        return text

    def wordcd(self, text):
        if (len(text) <2): #如果字串長度太小代表沒有內容，只接return
            return 0
        cut_text = jieba.cut(text) #用jieba斷詞
        i5= " ".join(cut_text)
        font = 'NotoSerifCJKtc-Black.ttf' #原本內建自型會亂碼 要換支援中文的
        wordcloud = WordCloud(collocations=False, font_path=font, max_words=200, width=int(self.graphicsView_5.width()-2),
                              height= int(self.graphicsView_5.height()-2), background_color='white',
                              stopwords= self.stopwords).generate(i5) #產生文字雲
        return wordcloud

    def wordcloud_plot(self, content, flag = 0):
        if(flag == 0):
            text = self.word_add(content) #先將要分析的文字合成一個字串
            wordcloud = self.wordcd(text) #產生文字雲物件
        else:
            wordcloud = self.wordcd2()
        img = np.array(wordcloud.to_image()) #用陣列儲存圖片
        height, width, byteValue = img.shape #將圖片轉換成QPixmap物件
        byteValue = byteValue * width
        image = QImage(img.data, width, height, byteValue, QtGui.QImage.Format_RGB888) #先轉換成QImage
        pxmp = QtGui.QPixmap(image) #轉換成QPixmap
        graphicscene = QtWidgets.QGraphicsScene() #將QPixmap加入到QGraphicsScene這樣就可以在QgraphicsView物件上顯示
        graphicscene.addPixmap(pxmp)

        return graphicscene

    def wordcd2(self):
        font = 'NotoSerifCJKtc-Black.ttf' #原本內建自型會亂碼 要換支援中文的
        wordcloud = WordCloud(collocations=False, font_path=font, max_words=100, width=int(self.graphicsView.width()-2),
                    height= int(self.graphicsView.height()-2), stopwords= self.stopwords,
                    background_color='white').generate_from_frequencies(self.wordcd2_text[1]) #產生文字雲
        return wordcloud

    def get_startend_time(self):
        start = self.lineEdit.text() #從lineEdit物件得到時間字串
        end = self.lineEdit_2.text()
        start = datetime.strptime(start, '%Y-%m-%d') #轉換字串到datetime物件
        end = datetime.strptime(end, '%Y-%m-%d')
        start = pytz.timezone('Asia/Taipei').localize(start) #手動設定時區
        end = pytz.timezone('Asia/Taipei').localize(end) 
        
        return start, end

    def set_art_timeseries(self):
        start, end = self.get_startend_time() #取得起始跟結束時間
        self.board_name = str(self.comboBox.currentText()) #取得看板名字
        #將邏輯運算放到另一個線程執行
        self.art_timeseries_thread = TimeSeries(board_name = self.board_name, start_time = start, end_time = end, db = self.db, flag = 0)
        self.thread = QThread()
        self.art_timeseries_thread.time_series_plot.connect(self.ts_plot_set)
        self.art_timeseries_thread.moveToThread(self.thread)
        self.art_timeseries_thread.finished.connect(self.thread.quit)
        self.thread.started.connect(self.art_timeseries_thread.run)
        self.thread.start()

    def set_word_timeseries(self):
        keyword = self.lineEdit_3.text() #取關鍵字
        start, end = self.get_startend_time()
        self.board_name = str(self.comboBox.currentText())
        if(self.checkBox.isChecked()): #查看是否啟用情感分析
            checked = 1
        else:
            checked = 0
        #將邏輯運算放到另一個線程執行
        self.word_timeseries_thread = TimeSeries(board_name = self.board_name, start_time = start, end_time = end, db = self.db, flag = 1,
                                                keyword = keyword, checked = checked)
        self.thread = QThread()
        self.word_timeseries_thread.time_series_plot.connect(self.ts_plot_set)
        self.word_timeseries_thread.art_list.connect(self.text_url_update)
        self.word_timeseries_thread.moveToThread(self.thread)
        self.word_timeseries_thread.finished.connect(self.thread.quit)
        self.thread.started.connect(self.word_timeseries_thread.run)
        self.thread.start()

    def text_url_update(self, text):
        #將關鍵詞搜尋中出現文字列表更新
        self.text_exist_url = text

    def ts_plot_set(self, ts):
        #為了能在qt的圖片顯示物件上可以顯示matplotlib的物件，matplotlib提供了FigureCanvas作為兩者之間的銜接橋梁
        figure = Figure(figsize=(int(self.graphicsView_19.width()/100), int(self.graphicsView_19.height()/100)))
        matplotlib.rcParams['timezone'] = 'Asia/Taipei' #讓圖片正確顯示本地的時間，使用本地的時區
        axes = figure.gca()
        colors = ['#CB1B45', '#005CAF', '#86C166']
        if isinstance(ts, pd.Series):
            ts.plot(ax = axes, grid = True, title = 'number of occurrence', color = '#005CAF')
        else:
            ts.plot(ax = axes, grid = True, title = 'number of occurrence', color = colors)
        canvas = FigureCanvas(figure) #轉換物件型態
        graphicscene = QtWidgets.QGraphicsScene() 
        graphicscene.addWidget(canvas) #將canvas加入QGraphicsScene物件，這樣就可以在graphicsView物件上顯示
        self.graphicsView_19.setScene(graphicscene)
        self.graphicsView_19.show()
    
    def self_board_set(self):
        #讓使用者設定自己的看板
        self_board_name = self.lineEdit_4.text()
        self_art_num = int(self.lineEdit_5.text())
        #將邏輯運算放到另一個線程執行
        self.self_board_thread = SelfBoardSet(board_name = self_board_name, art_num = self_art_num, db = self.db)
        self.thread = QThread()
        self.self_board_thread.start.connect(lambda: self.self_board_run_show(0))
        self.self_board_thread.moveToThread(self.thread)
        self.self_board_thread.finished.connect(self.thread.quit)
        self.self_board_thread.finished.connect(lambda: self.self_board_run_show(1))
        self.thread.started.connect(self.self_board_thread.run)
        self.thread.start()
    
    def self_board_run_show(self, flag):
        if(flag == 0):
            self.label_25.setText('運行中.....')
        else:
            self.label_25.setText('運行完畢')
            self.comboBox.addItem(self.lineEdit_4.text()) #將使用者的看板加入列表中

class WebView(QWebEngineView):
    #打開網頁
    def __init__(self, parent = None, url = None):
        QWebEngineView.__init__(self)
        self.load(QtCore.QUrl(url))
        self.setWindowTitle('browser')

class BoardList(QMainWindow, Ui_BoardList):
    #顯示熱門看板
    def __init__(self, parent = None):
        super(BoardList, self).__init__(parent)
        self.setupUi(self)
        self.set_list()

    def set_list(self):
        #基本抓取
        index = 'https://www.ptt.cc/bbs/hotboards.html'
        prepage = 'https://www.ptt.cc'
        rs = requests.get(index)
        soup = BeautifulSoup(rs.text, 'lxml')
        board_all = soup.find_all('div',{'class' : 'b-ent'})
        #計數得到編號
        n = 1
        list_str = ''
        for board in board_all:
            meta = board.find('a','board')
            link = meta.get('href') #得到的形式: /bbs/"board name here"/index.html
            name = meta.find('div','board-name').getText()
            nuser = meta.find('div', 'board-nuser').find('span').getText()
            bclass = meta.find('div','board-class').getText()
            title = meta.find('div', 'board-title').getText()
            
            #格式化輸出的時候要注意字型，有些字型的英文大小寫佔的長度不同會導致格式化不齊
            list_str = list_str +'{0: <3}{1: <2}{2: <15}{3: <10}{4: <2}{5: <20}'.format(n,': ',name, nuser, bclass, title)+'\n'
            self.textBrowser.setText(list_str)
            n = n + 1 

class textURL(QMainWindow, Ui_textURL):
    #關鍵字搜尋後產生的網址列表顯示
    def __init__(self, parent = None, text = None):
        super(textURL, self).__init__(parent)
        self.setupUi(self)
        self.text = text
        self.show_text()

    def show_text(self):
        self.textBrowser.setText(self.text)

class BoardUpdate(QObject):
    update_content = pyqtSignal(object, object, object)
    update_content_tab3 = pyqtSignal(str, object)
    finished = pyqtSignal()
    @pyqtSlot()
    def __init__(self, parent = None, board_name = None, db = None, stopword = None, wordcdwidth_1 = None, wordcdheight_1 = None,
                wordcdwidth_2 = None, wordcdheight_2 = None, art_num = None):
        super(BoardUpdate, self).__init__()
        #將需要的資訊傳入
        self.stopwords = stopword
        self.wordcdwidth_1 = wordcdwidth_1
        self.wordcdheight_1 = wordcdheight_1
        self.wordcdwidth_2 = wordcdwidth_2
        self.wordcdheight_2 = wordcdheight_2
        self.board_name = board_name
        self.db = db
        self.art_num = art_num

    def run(self):
        art_ref = self.db.collection(self.board_name) #取得collection(firestore存資料的集合)
        query = art_ref.order_by('date', direction=firestore.Query.DESCENDING).limit(self.art_num) #限制範圍
        results = query.get() #get的資料會存在query中，可以用foreach進行遍歷
        self.content = []
        n = 0

        for doc in results:
            dbdt = doc.to_dict() #將JSON檔案轉成dict
            #抓下來的日期時區是UTC+0，為了可以很好的連結關於時間的功能需要轉成台灣時區(UTC+8)
            dbdt['date'] = dbdt['date'].replace(tzinfo = pytz.utc).astimezone(pytz.timezone('Asia/Taipei')) 
            if(n < 3):
                self.content.append(dbdt)
                n = n + 1 #抓3筆資料
            else:
                if(dbdt['allpush'] > self.content[0]['allpush']):
                    self.content[2] = self.content[1]
                    self.content[1] = self.content[0]
                    self.content[0] = dbdt

        self.sp_pushtext = [] 
        self.sp_pushtext.append(self.word_freq(self.content[0])) #隨機挑選3條含有出現頻率高的字詞的推噓文
        self.sp_pushtext.append(self.word_freq(self.content[1])) #將字串物件串到一個list好回傳到主線程
        self.sp_pushtext.append(self.word_freq(self.content[2]))

        self.graphicscene = []
        self.graphicscene.append(self.wordcloud_plot(self.content[0])) #將文字雲物件串到一個list好回傳回去主線程
        self.graphicscene.append(self.wordcloud_plot(self.content[1]))
        self.graphicscene.append(self.wordcloud_plot(self.content[2]))

        doc_ref = self.db.collection('big_analyze').document(self.board_name) #取出整版分析需要的資料
        docs = doc_ref.get()
        docs = docs.to_dict()
        self.wordcd2_text = [docs['common_text'], docs['text_wordcd']] 
        self.wordcd2_graphic = self.wordcloud_plot(content = 0, flag = 1) #生成文字雲

        self.update_content.emit(self.content, self.sp_pushtext, self.graphicscene) #發送信號
        self.update_content_tab3.emit(self.wordcd2_text[0], self.wordcd2_graphic) 
        self.finished.emit() #結束信號

    def word_freq(self, content):
        #此函數取得該篇文章出現頻率最多的單詞，然後將有出現該單詞的推文隨機的挑出3條
        if(content['allpush'] < 3): #推文數量過少的處理，直接顯示所有推文
            if(content['push'] == 0 and content['down'] == 0 and content['arr'] == 0):
                text = '沒有推文'
                return text
            else:
                text = ''
                for push in content['pushtext']:
                    text = text + push
                for down in content['downtext']:
                    text = text + down
                for arr in content['arrtext']:
                    text = text + arr
                return text
        
        text = self.word_add(content) #加總所有部分的文字
        text = jieba.cut(text) #斷詞
        word_count = collections.Counter() #collection的counter統計在一個物件中重複的子成員的數量，並且支持+-運算
        for word in text: 
            if(len(word) > 1 and word != '\r\n' and word not in self.stopwords): #這裡不直接使用counter是因為counter會把長度1的字串也算進去
                word_count[word] = word_count[word] + 1 #進行次數統計

        n = 0
        word_list = []
        for word, times in word_count.most_common(3):#從counter的字典中取出找頻率最高的前三個單詞，加入word_list中作為搜尋的依據
            word_list.append(word) 
            n = n + 1
            if(n >= 3):
                n = 0
                break
        texti = ''
        for push in content['pushtext']: #搜尋推文 噓文 箭頭文
            if(push.find(word_list[random.randint(0, 2)][0]) != -1 and len(push) > 5): #隨機從word_list中取出一種單詞，如果該推文中有出現該單詞就加入回傳的字串
               n = n + 1
               texti = texti + push +'\n'
               if(n == 3):
                   break
        if(n < 3):
            for down in content['downtext']:
                if(down.find(word_list[random.randint(0, 2)][0]) != -1 and len(down) > 5):
                    n = n + 1
                    texti = texti + down +'\n'
                    if(n == 3):
                        break
        if(n < 3):
            for arr in content['arrtext']:
                if(arr.find(word_list[random.randint(0, 2)][0]) != -1 and len(arr) > 5):
                    n = n + 1
                    texti = texti + arr +'\n'
                    if(n == 3):
                        break
        return texti

    def word_add(self, content):
        #本函數單純將所有需要分析的字串加總，好進行斷詞
        text = content['title'] + content['context']

        for texti in content['pushtext']:
            text = text + texti
        for texti in content['downtext']:
            text = text + texti
        for texti in content['arrtext']:
            text = text + texti
        return text

    def wordcd(self, text):
        if (len(text) <2): #如果字串長度太小代表沒有內容，只接return
            return 0
        cut_text = jieba.cut(text) #用jieba斷詞
        i5= " ".join(cut_text)
        font = 'NotoSerifCJKtc-Black.ttf' #原本內建自型會亂碼 要換支援中文的
        wordcloud = WordCloud(collocations=False, font_path=font, max_words=200, width = self.wordcdwidth_1,
                              height= self.wordcdheight_1, background_color='white',
                              stopwords= self.stopwords).generate(i5) #產生文字雲
        return wordcloud

    def wordcloud_plot(self, content, flag = 0):
        if(flag == 0):
            text = self.word_add(content) #先將要分析的文字合成一個字串
            wordcloud = self.wordcd(text) #產生文字雲物件
        else:
            wordcloud = self.wordcd2()
        img = np.array(wordcloud.to_image()) #用陣列儲存圖片
        height, width, byteValue = img.shape #將圖片轉換成QPixmap物件
        byteValue = byteValue * width
        image = QImage(img.data, width, height, byteValue, QtGui.QImage.Format_RGB888) #先轉換成QImage
        pxmp = QtGui.QPixmap(image) #轉換成QPixmap
        graphicscene = QtWidgets.QGraphicsScene() #將QPixmap加入到QGraphicsScene這樣就可以在QgraphicsView物件上顯示
        graphicscene.addPixmap(pxmp)

        return graphicscene
    
    def wordcd2(self):
        font = 'NotoSerifCJKtc-Black.ttf' #原本內建自型會亂碼 要換支援中文的
        wordcloud = WordCloud(collocations=False, font_path=font, max_words=100, width= self.wordcdwidth_2,
                    height= self.wordcdheight_2, stopwords= self.stopwords,
                    background_color='white').generate_from_frequencies(self.wordcd2_text[1]) #產生文字雲
        return wordcloud

class TimeSeries(QObject):
    time_series_plot = pyqtSignal(object) #宣告pyqt的信號，傳回值是object型態(萬用，可以是任何形式的object，我這裡要傳回pandas.Series)
    art_list = pyqtSignal(object) #傳回字串
    finished = pyqtSignal() #不傳回值，這裡只單純發出結束信號使這個線程結束
    @pyqtSlot()
    def __init__(self, parent = None, board_name = None, start_time = None, end_time = None, db = None, flag = None,
                keyword = None, checked = None):
        super(TimeSeries, self).__init__()
        #由主線程傳入需要的資訊
        self.start_time = start_time
        self.end_time = end_time
        self.db = db
        self.board_name = board_name
        self.flag = flag
        self.keyword = keyword
        self.checked = checked

    def run(self):
        #檢查是進行發文頻率分析或關鍵字搜尋
        if(self.flag == 0):
            self.art_timeseries()
            self.time_series_plot.emit(self.ts)
            self.finished.emit()
        
        else:
            self.word_timeseries()
            self.time_series_plot.emit(self.ts)
            self.art_list.emit(self.text_exist_url)
            self.finished.emit()

    def art_timeseries(self):
        #where功能可以限制資料庫取得資料的範圍，用法參照下面，datetime物件也可以接受大於小於運算子的運算
        #direction參數是sort的順序，遞增或遞減
        art_ref = self.db.collection(self.board_name)
        query = art_ref.where('date', '>', self.start_time).where('date', '<', self.end_time).order_by('date', direction=firestore.Query.DESCENDING)
        results = query.get()

        dt_range = pd.date_range(start = self.start_time, end = self.end_time) #根據上方的起始結束日期產生一條以天為單位的日期
        ts = pd.Series(np.zeros(1), index = dt_range) #產生時間序列物件(其實就是單行的dataframe)
        for doc in results:
            content = doc.to_dict() #JSON轉換成字典
            content['date'] = content['date'].replace(tzinfo = pytz.utc).astimezone(pytz.timezone('Asia/Taipei')) #設定符合本地時區
            dt_index = datetime.strftime(content['date'], '%Y-%m-%d') #為了對time series物件進行操作，把datetime物件轉換成字串
            ts[dt_index] = ts[dt_index] + 1 #用上方產生的index對time series進行操作(符合日期的話，數量+1)
        ts = ts.ix[:-1]
        self.ts = ts
    
    def word_add(self, content):
        #本函數單純將所有需要分析的字串加總，好進行斷詞
        text = content['title'] + content['context']

        for texti in content['pushtext']:
            text = text + texti
        for texti in content['downtext']:
            text = text + texti
        for texti in content['arrtext']:
            text = text + texti
        return text

    def word_timeseries(self):
        art_ref = self.db.collection(self.board_name) #從資料庫取得資料，取得的範圍在兩個日期之間
        query = art_ref.where('date', '>=', self.start_time).where('date', '<=', self.end_time)
        results = query.get()

        dt_range = pd.date_range(start = self.start_time, end = self.end_time) #產生timeseries物件
        ts = pd.Series(np.zeros(1), index = dt_range)
        if(self.checked == 1): #查看是否啟用情感分析
            df = self.word_timeseries_generate_senti(ts, results, self.keyword) 
            df = df.ix[:-1]
            self.ts = df #將要回傳的物件設定(pandas.DataFrame 或 pandas.Series)
        else:
            ts = self.word_timeseries_generate(ts, results, self.keyword)
            ts.drop(self.end_time)
            ts = ts.ix[:-1]
            self.ts = ts

    def word_timeseries_generate(self, ts, results, keyword):
        self.text_exist_url = ''
        for doc in results:
            content = doc.to_dict() #將JSON轉成字典
            content['date'] = content['date'].replace(tzinfo = pytz.utc).astimezone(pytz.timezone('Asia/Taipei')) #手動設定時區
            dt_index = datetime.strftime(content['date'], '%Y-%m-%d') #為了可以操作timeseries將datetime物件轉換成string來存取timeseries
            text = self.word_add(content) #將所有要分析的文字加總
            reg = re.compile('(?=' + self.keyword +')') #使用正則表達式的話可以搜尋重複的字串 ex: ababa 找 aba 結果:2，直接使用find只能找到1
            length = len(reg.findall(text)) #統計關鍵字在該文章中出現的次數
            if(length > 0):
                self.text_exist_url =  self.text_exist_url + content['link'] + '\n' + '作者: {0: <35} 出現次數: {1: <5}'.format(content['author'], length) + '\n'  
                ts[dt_index] = ts[dt_index] + length #將次數加到本日出現的次數中
        return ts
    
    def word_timeseries_generate_senti(self, ts, results, keyword):
        #跟上面的產生序列方式大同小異，但這裡加入了情感分析的分數
        self.text_exist_url = ''
        df = pd.DataFrame({'number of occurrence' : np.zeros(1), 'positive' : np.zeros(1), 'negative' : np.zeros(1)}, index = ts.index)
        doc_list = []
        for doc in results:
            doc_dict = doc.to_dict()
            doc_list.append(doc_dict)
        
        for content in doc_list:
            #content = doc.to_dict() #將JSON轉成字典
            content['date'] = content['date'].replace(tzinfo = pytz.utc).astimezone(pytz.timezone('Asia/Taipei')) #手動設定時區
            dt_index = datetime.strftime(content['date'], '%Y-%m-%d') #為了可以操作timeseries將datetime物件轉換成string來存取timeseries
            text = self.word_add(content) #將所有要分析的文字加總
            reg = re.compile('(?=' + self.keyword +')') #使用正則表達式的話可以搜尋重複的字串 ex: ababa 找 aba 結果:2，直接使用find只能找到1
            length = len(reg.findall(text)) #統計關鍵字在該文章中出現的次數
            if(length > 0):
                self.text_exist_url =  self.text_exist_url + content['link'] + '\n' + content['title']+ '\n' + '作者: {0: <35} 出現次數: {1: <5}'.format(content['author'], length) + '\n'  
                len_posi, len_nega = self.senti_analyze(content, self.keyword)
                df['positive'][dt_index] = df['positive'][dt_index] + len_posi #根據情感分析的結果將次數加上去
                df['negative'][dt_index] = df['negative'][dt_index] + len_nega
                df['number of occurrence'][dt_index] = df['number of occurrence'][dt_index] + length #將次數加到本日出現的次數中
        return df

    def senti_analyze(self, content, keyword):
        #針對內含關鍵字的推文、內文、噓文、箭頭文作情感分析
        #snowNLP套件的情感分析: 對每個句子打分，分數在0~1之間，越靠近1的表示越正面，靠近0的表示負面
        posi_num = 0
        nega_num = 0

        reg = re.compile('(?=' + self.keyword +')') #找內文
        length = len(reg.findall(content['context']))
        if(length > 0):
            s = SnowNLP(content['context'])
            if(s.sentiments > 0.5):
                posi_num = posi_num + 1
            else:
                nega_num = nega_num + 1

        for sentence in content['pushtext']:
            reg = re.compile('(?=' + self.keyword +')') #找推文
            length = len(reg.findall(sentence))
            if(length > 0) :
                s = SnowNLP(sentence)
                if(s.sentiments > 0.5):
                    posi_num = posi_num + 1
                else:
                    nega_num = nega_num + 1

        for sentence in content['downtext']:
            reg = re.compile('(?=' + self.keyword +')') #找噓文
            length = len(reg.findall(sentence))
            if(length > 0):
                s = SnowNLP(sentence)
                if(s.sentiments > 0.5):
                    posi_num = posi_num + 1
                else:
                    nega_num = nega_num + 1
        
        for sentence in content['arrtext']:
            reg = re.compile('(?=' + self.keyword +')') #找箭頭
            length = len(reg.findall(sentence))
            if(length > 0):
                s = SnowNLP(sentence)
                if(s.sentiments > 0.5):
                    posi_num = posi_num + 1
                else:
                    nega_num = nega_num + 1
        return posi_num, nega_num

class SelfBoardSet(QObject):
    start = pyqtSignal()
    finished = pyqtSignal()
    @pyqtSlot()
    def __init__(self, parent = None, board_name = None, art_num = None, db = None):
        super(SelfBoardSet, self).__init__()
        #將必要的資訊傳入
        self.board_name = board_name
        self.art_num = art_num
        self.db = db
    
    def run(self):
        self.start.emit() #發出開始的信號
        board_iter(self.board_name, self.db, self.art_num) #開始爬蟲
        word_freq(self.board_name, self.db) #更新整版分析用的資訊
        self.finished.emit() #發出結束的信號

if __name__ == "__main__":
    app = QApplication(sys.argv)
    with open('style.qss', 'r') as filepath:
        app.setStyleSheet(filepath.read()) #設定window style
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

# python .\main.py
# pyuic5 mainwindow.ui -o mainwindow.py