def get_push(self, url):
        warnings.filterwarnings('ignore')#忽略警告

        index = 'https://www.ptt.cc'
        www = url.replace('https://www.ptt.cc','')

        payload = { #滿18歲驗證 over18.php  f12>network index.html前有over18.php
        'from':www, #要進哪個版
        'yes':'yes' #預設回答
        }

        rs = requests.session()
        res = rs.post('https://www.ptt.cc/ask/over18', verify=False,data=payload)
        res = rs.get(url, verify=False)

        soup = BeautifulSoup(res.text,'lxml') #要分析物體包含在BeautifulSoup的物件當中
        arts = soup.find_all('div', 'push') #回傳結果是list 可以加上[任意數字] 來顯示list中的第幾筆資料 [].text 加上text可以省

        pushnum, downnum, arrnum = 0, 0, 0

        for art in arts:
            push = art.find('span', 'push-tag').getText()

            if push[0] == '推':
                pushnum = pushnum + 1
            elif push[0] == '噓':
                downnum = downnum + 1
            else:
                arrnum = arrnum + 1

        return pushnum , downnum, arrnum    

    def get_info(self, url, pushnum, downnum, arrnum):
        info = {'title': '',
                'link': url,
                'push': pushnum,
                'down': downnum,
                'allpush': pushnum + downnum + arrnum,
                'date': '',
                'author': '',
                'text': ''}

        warnings.filterwarnings('ignore')#忽略警告
        index = 'https://www.ptt.cc'
        www = url.replace('https://www.ptt.cc','')

        payload = { #滿18歲驗證 over18.php  f12>network index.html前有over18.php
        'from':www, #要進哪個版
        'yes':'yes' #預設回答
        }

        rs = requests.session()
        res = rs.post('https://www.ptt.cc/ask/over18', verify=False,data=payload)
        res = rs.get(url, verify=False)


        soup = BeautifulSoup(res.text,'lxml') #要分析物體包含在BeautifulSoup的物件當中
        art_info = soup.find_all('div', 'article-metaline') #回傳結果是list 可以加上[任意數字] 來顯示list中的第幾筆資料 [].text 加上text可以省

        info['author'] = art_info[0].getText()
        info['author'] = info['author'][2:]
        info['title'] = art_info[1].getText()
        info['title'] = info['title'][2:]
        info['date'] = art_info[2].getText()
        info['date'] = info['date'][2:]
        
        return info
        
    def get_high_art(self, url):
        warnings.filterwarnings('ignore')#忽略警告
        top_dict ={
                'title': '',
                'link': '',
                'push': 0,
                'down': 0,
                'allpush': 0,
                'date': '',
                'author': '',
                'text': ''}
        top = []
        for i in range(3):
            top.append(top_dict)

        needpage = 100
        num = needpage/20
        num = num + 2
        nowpage = 0

        NOT_EXIST = BeautifulSoup('<a>本文已被刪除</a>', 'lxml').a #find()沒找到title(回傳none)就顯示這條
        index = 'https://www.ptt.cc'
        www = url.replace('https://www.ptt.cc','')
        payload = { #滿18歲驗證 over18.php  f12>network index.html前有over18.php
        'from':www, #要進哪個版
        'yes':'yes' #預設回答
        }

        rs = requests.session()
        res = rs.post('https://www.ptt.cc/ask/over18', verify=False,data=payload)
        res = rs.get(url, verify=False)

        soup = BeautifulSoup(res.text,'lxml') #要分析物體包含在BeautifulSoup的物件當中
        articles = soup.find_all('div', 'r-ent')
        title = soup.find('a', 'board').getText()
        title = title[3:]

        next_link2 = soup.find('div', 'btn-group-paging').find_all('a', 'btn wide')[1].get('href')
        saveposts = list()
        
        top, nowpage = self.find_top3(articles, nowpage, needpage, top)
        while(nowpage < needpage):
            url = urllib.parse.urljoin(index, next_link2) # 合出前一頁的網址
            res = rs.post('https://www.ptt.cc/ask/over18', verify=False,data=payload)
            res = rs.get(url, verify=False)
            soup = BeautifulSoup(res.text,'lxml')
            articles = soup.find_all('div', 'r-ent') # 更新articles
            next_link2 = soup.find('div', 'btn-group-paging').find_all('a', 'btn wide')[1].get('href')
            top, nowpage = self.find_top3(articles, nowpage, needpage, top)
        
        return top, title

    def find_top3(self, articles, nowpage, needpage, top):
        index = 'https://www.ptt.cc'
        NOT_EXIST = BeautifulSoup('<a>本文已被刪除</a>', 'lxml').a
        for article in articles:
            if(nowpage < needpage):
                nowpage = nowpage + 1
                meta2 = article.find('div', 'title').find('a')or NOT_EXIST # A or B 前面空則B

                title2 = meta2.getText().strip()
                link2 = meta2.get('href')
                link2 = urllib.parse.urljoin(index, link2)

        #-----------找出推文前三多-------------------------------------------------------------     
                if title2[1] == '公':
                    thenum = -1
                elif title2[1] == '協':
                    thenum = -1
                elif title2[0] == 'F' and title2[5] == '協':
                    thenum = -1
                else:
                    pushnum, downnum, arrnum = self.get_push(link2)
                    thenum = pushnum + downnum + arrnum
            
                if thenum > top[0].get('allpush') :
                    top[2] = top[1]
                    top[1] = top[0]
                    top[0] = self.get_info(link2, pushnum, downnum, arrnum)

                elif thenum > top[1].get('allpush') :
                    top[2] = top[1]
                    top[1] = self.get_info(link2, pushnum, downnum, arrnum)

                elif thenum > top[2].get('allpush'):
                    top[2] = self.get_info(link2, pushnum, downnum, arrnum)
                print(nowpage)

        return top, nowpage

 def save_url(self):
        url_head = 'https://www.ptt.cc/bbs/'
        url_tail = '/index.html'
        url_1 = self.lineEdit.text()

        config = configparser.ConfigParser()
        if not config.has_section('URL'):
            config.add_section('URL')

        if(url_1 != ''):
            config.set('URL', 'url1', url_head + url_1 + url_tail)
            
        if not config.options('URL'):
            self.new_window = CheckWindow2()
            self.new_window.show()
        else:
            config.write(open('url.ini', 'w'))
            self.close()

def set_url(self):
        #網址存在url.ini中，檢查其是否存在，不存在或空白就打開CheckWindow()視窗
        #現在關於這方面的功能沒有完成，之後會修改
        if not os.path.exists('url.ini'):
            self.new_window = CheckWindow()
            self.new_window.show()
        elif (os.stat('url.ini').st_size == 0):
            self.new_window = CheckWindow()
            self.new_window.show()


def get_borad_list(self):
        #把ini中的url存到url_list
        config = configparser.ConfigParser()
        config.read('url.ini')
        board_list = config.options('URL')
        url_list = []
        for i in board_list:
            url_list.append(config.get('URL', i))
        
        return url_list

#未檢測到.ini檔的通知視窗
class CheckWindow(QDialog, Ui_Dialog):
    def __init__(self, parent = None):
        super(CheckWindow, self).__init__(parent, QtCore.Qt.WindowStaysOnTopHint)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.board_list_window)

    def board_list_window(self):
        self.new_window = BoardList()
        self.new_window.show()
        self.close()

class CheckWindow2(QDialog, Ui_Dialog2):
    def __init__(self, parent = None):
        super(CheckWindow2, self).__init__(parent, QtCore.Qt.WindowStaysOnTopHint)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.terminate_window)

    def terminate_window(self):
        self.close()

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
                    texti = texti + ar +'\n'
                    if(n == 3):
                        break
        return texti

    def art_timeseries(self):
        start = self.lineEdit.text() #從lineEdit物件得到時間字串
        end = self.lineEdit_2.text()
        start = datetime.strptime(start, '%Y-%m-%d') #轉換字串到datetime物件
        end = datetime.strptime(end, '%Y-%m-%d')
        #start = datetime.strptime('2018-05-09', '%Y-%m-%d')
        #end = datetime.strptime('2018-05-11', '%Y-%m-%d')
        start = pytz.timezone('Asia/Taipei').localize(start) #手動設定時區
        end = pytz.timezone('Asia/Taipei').localize(end) 

        #where功能可以限制資料庫取得資料的範圍，用法參照下面，datetime物件也可以接受大於小於運算子的運算
        #direction參數是sort的順序，遞增或遞減
        art_ref = self.db.collection(u'Steam')
        query = art_ref.where(u'date', u'>', start).where(u'date', u'<', end).order_by(u'date', direction=firestore.Query.DESCENDING)
        results = query.get()

        dt_range = pd.date_range(start = start, end = end) #根據上方的起始結束日期產生一條以天為單位的日期
        ts = pd.Series(np.zeros(1), index = dt_range) #產生時間序列物件(其實就是單行的dataframe)
        for doc in results:
            content = doc.to_dict() #JSON轉換成字典
            content['date'] = content['date'].replace(tzinfo = pytz.utc).astimezone(pytz.timezone('Asia/Taipei')) #設定符合本地時區
            dt_index = datetime.strftime(content['date'], '%Y-%m-%d') #為了對time series物件進行操作，把datetime物件轉換成字串
            #print('{} => {}'.format(content['title'], content['date']))
            ts[dt_index] = ts[dt_index] + 1 #用上方產生的index對time series進行操作(符合日期的話，數量+1)
        #print(ts)
        self.ts_plot(ts)
    
    def ts_plot(self, ts):
        #為了能在qt的圖片顯示物件上可以顯示matplotlib的物件，matplotlib提供了FigureCanvas作為兩者之間的銜接橋梁
        figure = Figure(figsize=(self.graphicsView_19.width()/100 - 0.1, self.graphicsView_19.height()/100 - 0.1)) 
        matplotlib.rcParams['timezone'] = 'Asia/Taipei' #讓圖片正確顯示本地的時間，使用本地的時區
        axes = figure.gca()
        colors = ['#CB1B45', '#005CAF', '#86C166']
        if isinstance(ts, pd.Series): #檢查傳進來的資料型態是Series或者是Dataframe，這會影響到如何繪圖
            ts.plot(ax = axes, grid = True, title = 'number of occurrence', color = '#005CAF')
        else:
            ts.plot(ax = axes, grid = True, title = 'number of occurrence', color = colors)
        canvas = FigureCanvas(figure) #轉換物件型態
        graphicscene = QtWidgets.QGraphicsScene() 
        graphicscene.addWidget(canvas) #將canvas加入QGraphicsScene物件，這樣就可以在graphicsView物件上顯示
        self.graphicsView_19.setScene(graphicscene)
        self.graphicsView_19.show()

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

    def word_timeseries(self):
        board_name = str(self.comboBox.currentText())
        keyword = self.lineEdit_3.text() #取關鍵字
        start = self.lineEdit.text() #取起始時間
        end = self.lineEdit_2.text() #取結束時間
        start = datetime.strptime(start, '%Y-%m-%d') #字串轉成datetime物件
        end = datetime.strptime(end, '%Y-%m-%d')
        start = pytz.timezone('Asia/Taipei').localize(start) #設定本地時區
        end = pytz.timezone('Asia/Taipei').localize(end)

        art_ref = self.db.collection(board_name) #從資料庫取得資料，取得的範圍在兩個日期之間
        query = art_ref.where(u'date', u'>=', start).where(u'date', u'<=', end)
        results = query.get()

        dt_range = pd.date_range(start = start, end = end) #產生timeseries物件
        ts = pd.Series(np.zeros(1), index = dt_range)
        if(self.checkBox.isChecked()): #查看是否啟用情感分析
            df = self.word_timeseries_generate_senti(ts, results, keyword) 
            self.ts_plot(df) #呼叫繪圖函數將timeseries視覺化
        else:
            ts = self.word_timeseries_generate(ts, results, keyword)
            self.ts_plot(ts)
        self.pushButton_19.clicked.connect(self.text_url_window)

    def word_timeseries_generate(self, ts, results, keyword):
        self.text_exist_url = ''
        for doc in results:
            content = doc.to_dict() #將JSON轉成字典
            content['date'] = content['date'].replace(tzinfo = pytz.utc).astimezone(pytz.timezone('Asia/Taipei')) #手動設定時區
            dt_index = datetime.strftime(content['date'], '%Y-%m-%d') #為了可以操作timeseries將datetime物件轉換成string來存取timeseries
            text = self.word_add(content) #將所有要分析的文字加總
            reg = re.compile('(?=' + keyword +')') #使用正則表達式的話可以搜尋重複的字串 ex: ababa 找 aba 結果:2，直接使用find只能找到1
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
            reg = re.compile('(?=' + keyword +')') #使用正則表達式的話可以搜尋重複的字串 ex: ababa 找 aba 結果:2，直接使用find只能找到1
            length = len(reg.findall(text)) #統計關鍵字在該文章中出現的次數
            if(length > 0):
                self.text_exist_url =  self.text_exist_url + content['link'] + '\n' + '作者: {0: <35} 出現次數: {1: <5}'.format(content['author'], length) + '\n'  
                len_posi, len_nega = self.senti_analyze(content, keyword)
                df['positive'][dt_index] = df['positive'][dt_index] + len_posi #根據情感分析的結果將次數加上去
                df['negative'][dt_index] = df['negative'][dt_index] + len_nega
                df['number of occurrence'][dt_index] = df['number of occurrence'][dt_index] + length #將次數加到本日出現的次數中
        print(df)
        return df

    def senti_analyze(self, content, keyword):
        #針對內含關鍵字的推文、內文、噓文、箭頭文作情感分析
        #snowNLP套件的情感分析: 對每個句子打分，分數在0~1之間，越靠近1的表示越正面，靠近0的表示負面
        posi_num = 0
        nega_num = 0

        reg = re.compile('(?=' + keyword +')') #找內文
        length = len(reg.findall(content['context']))
        if(length > 0):
            s = SnowNLP(content['context'])
            if(s.sentiments > 0.5):
                posi_num = posi_num + 1
            else:
                nega_num = nega_num + 1

        for sentence in content['pushtext']:
            reg = re.compile('(?=' + keyword +')') #找推文
            length = len(reg.findall(sentence))
            if(length > 0):
                s = SnowNLP(sentence)
                if(s.sentiments > 0.5):
                    posi_num = posi_num + 1
                else:
                    nega_num = nega_num + 1

        for sentence in content['downtext']:
            reg = re.compile('(?=' + keyword +')') #找噓文
            length = len(reg.findall(sentence))
            if(length > 0):
                s = SnowNLP(sentence)
                if(s.sentiments > 0.5):
                    posi_num = posi_num + 1
                else:
                    nega_num = nega_num + 1
        
        for sentence in content['arrtext']:
            reg = re.compile('(?=' + keyword +')') #找箭頭
            length = len(reg.findall(sentence))
            if(length > 0):
                s = SnowNLP(sentence)
                if(s.sentiments > 0.5):
                    posi_num = posi_num + 1
                else:
                    nega_num = nega_num + 1
        return posi_num, nega_num