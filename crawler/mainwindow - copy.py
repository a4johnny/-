# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1255, 691)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1144, 20, 101, 23))
        self.pushButton.setObjectName("pushButton")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 40, 1241, 611))
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.scrollArea = QtWidgets.QScrollArea(self.tab)
        self.scrollArea.setGeometry(QtCore.QRect(10, 10, 1211, 561))
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, -59, 1192, 618))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_3 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_3.setMinimumSize(QtCore.QSize(1100, 600))
        self.groupBox_3.setObjectName("groupBox_3")
        self.frame_1 = QtWidgets.QFrame(self.groupBox_3)
        self.frame_1.setGeometry(QtCore.QRect(10, 22, 1131, 186))
        self.frame_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_1.setObjectName("frame_1")
        self.textBrowser_1 = QtWidgets.QTextBrowser(self.frame_1)
        self.textBrowser_1.setGeometry(QtCore.QRect(20, 100, 591, 71))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        self.textBrowser_1.setFont(font)
        self.textBrowser_1.setObjectName("textBrowser_1")
        self.label_1 = QtWidgets.QLabel(self.frame_1)
        self.label_1.setGeometry(QtCore.QRect(130, 60, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.pushButton_1 = QtWidgets.QPushButton(self.frame_1)
        self.pushButton_1.setGeometry(QtCore.QRect(424, 52, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(14)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setObjectName("pushButton_1")
        self.label_2 = QtWidgets.QLabel(self.frame_1)
        self.label_2.setGeometry(QtCore.QRect(250, 60, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_1)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_1)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 491, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.graphicsView_5 = QtWidgets.QGraphicsView(self.frame_1)
        self.graphicsView_5.setGeometry(QtCore.QRect(640, 30, 481, 141))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        self.graphicsView_5.setFont(font)
        self.graphicsView_5.setObjectName("graphicsView_5")
        self.frame_2 = QtWidgets.QFrame(self.groupBox_3)
        self.frame_2.setGeometry(QtCore.QRect(10, 210, 1131, 186))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(240, 60, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.frame_2)
        self.textBrowser_2.setGeometry(QtCore.QRect(20, 100, 591, 71))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(20, 10, 491, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(20, 60, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.graphicsView_6 = QtWidgets.QGraphicsView(self.frame_2)
        self.graphicsView_6.setGeometry(QtCore.QRect(640, 30, 481, 141))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        self.graphicsView_6.setFont(font)
        self.graphicsView_6.setObjectName("graphicsView_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(424, 52, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(130, 60, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.frame_3 = QtWidgets.QFrame(self.groupBox_3)
        self.frame_3.setGeometry(QtCore.QRect(10, 400, 1131, 186))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_9 = QtWidgets.QLabel(self.frame_3)
        self.label_9.setGeometry(QtCore.QRect(240, 60, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.frame_3)
        self.textBrowser_3.setGeometry(QtCore.QRect(20, 100, 591, 71))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        self.textBrowser_3.setFont(font)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.label_10 = QtWidgets.QLabel(self.frame_3)
        self.label_10.setGeometry(QtCore.QRect(20, 10, 491, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame_3)
        self.label_11.setGeometry(QtCore.QRect(20, 60, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.graphicsView_7 = QtWidgets.QGraphicsView(self.frame_3)
        self.graphicsView_7.setGeometry(QtCore.QRect(640, 30, 481, 141))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        self.graphicsView_7.setFont(font)
        self.graphicsView_7.setObjectName("graphicsView_7")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_3.setGeometry(QtCore.QRect(424, 52, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_12 = QtWidgets.QLabel(self.frame_3)
        self.label_12.setGeometry(QtCore.QRect(130, 60, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.groupBox_3, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit.setGeometry(QtCore.QRect(80, 130, 121, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(260, 130, 121, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 60, 141, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(30, 30, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_27 = QtWidgets.QLabel(self.tab_2)
        self.label_27.setGeometry(QtCore.QRect(30, 100, 291, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(14)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.graphicsView_19 = QtWidgets.QGraphicsView(self.tab_2)
        self.graphicsView_19.setGeometry(QtCore.QRect(30, 180, 1131, 351))
        self.graphicsView_19.setObjectName("graphicsView_19")
        self.pushButton_17 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_17.setGeometry(QtCore.QRect(400, 90, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(14)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_18.setGeometry(QtCore.QRect(400, 130, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(14)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setObjectName("pushButton_18")
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(30, 140, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        self.label_14.setGeometry(QtCore.QRect(210, 140, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(14)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.tab_2)
        self.label_15.setGeometry(QtCore.QRect(320, 0, 831, 81))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.pushButton_19 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_19.setGeometry(QtCore.QRect(710, 130, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(14)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setObjectName("pushButton_19")
        self.label_24 = QtWidgets.QLabel(self.tab_2)
        self.label_24.setGeometry(QtCore.QRect(870, 140, 451, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(14)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.checkBox = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox.setGeometry(QtCore.QRect(560, 140, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(14)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_4)
        self.textBrowser.setGeometry(QtCore.QRect(70, 80, 281, 481))
        self.textBrowser.setObjectName("textBrowser")
        self.graphicsView = QtWidgets.QGraphicsView(self.tab_4)
        self.graphicsView.setGeometry(QtCore.QRect(370, 80, 751, 481))
        self.graphicsView.setObjectName("graphicsView")
        self.label_16 = QtWidgets.QLabel(self.tab_4)
        self.label_16.setGeometry(QtCore.QRect(70, 20, 821, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_4.setGeometry(QtCore.QRect(180, 20, 261, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_17 = QtWidgets.QLabel(self.tab_3)
        self.label_17.setGeometry(QtCore.QRect(20, 20, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.tab_3)
        self.label_18.setGeometry(QtCore.QRect(20, 60, 711, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_5.setGeometry(QtCore.QRect(490, 20, 121, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_19 = QtWidgets.QLabel(self.tab_3)
        self.label_19.setGeometry(QtCore.QRect(450, 20, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(12)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.tab_3)
        self.label_20.setGeometry(QtCore.QRect(20, 520, 1151, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(12)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.checkBox_2 = QtWidgets.QCheckBox(self.tab_3)
        self.checkBox_2.setGeometry(QtCore.QRect(20, 110, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(12)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_7.setGeometry(QtCore.QRect(300, 110, 381, 31))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_23 = QtWidgets.QLabel(self.tab_3)
        self.label_23.setGeometry(QtCore.QRect(190, 110, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(12)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.tabWidget.addTab(self.tab_3, "")
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(1060, 20, 75, 23))
        self.pushButton_16.setObjectName("pushButton_16")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(850, 20, 201, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(690, 20, 51, 21))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(610, 20, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(12)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(760, 20, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(12)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1255, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "熱門看板列表"))
        self.groupBox_3.setTitle(_translate("MainWindow", "看板名稱"))
        self.textBrowser_1.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Microsoft JhengHei\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'PMingLiU\'; font-size:12pt;\">推文1</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'PMingLiU\'; font-size:12pt;\">推文2</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'PMingLiU\'; font-size:12pt;\">推文3</span></p></body></html>"))
        self.label_1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">噓文數</span></p></body></html>"))
        self.pushButton_1.setText(_translate("MainWindow", "開啟文章"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">總推文數</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">推文數</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">[標題] 標題最多有20個字元標題最多有20個字元標題</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">總推文數</span></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Microsoft JhengHei\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'PMingLiU\'; font-size:12pt;\">推文1</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'PMingLiU\'; font-size:12pt;\">推文2</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'PMingLiU\'; font-size:12pt;\">推文3</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">[標題] 標題最多有20個字元標題最多有20個字元標題</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">推文數</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "開啟文章"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">噓文數</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">總推文數</span></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Microsoft JhengHei\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'PMingLiU\'; font-size:12pt;\">推文1</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'PMingLiU\'; font-size:12pt;\">推文2</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'PMingLiU\'; font-size:12pt;\">推文3</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">[標題] 標題最多有20個字元標題最多有20個字元標題</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">推文數</span></p></body></html>"))
        self.pushButton_3.setText(_translate("MainWindow", "開啟文章"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">噓文數</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "熱門選項"))
        self.lineEdit.setText(_translate("MainWindow", "2018-05-11"))
        self.lineEdit_2.setText(_translate("MainWindow", "2018-05-13"))
        self.lineEdit_3.setText(_translate("MainWindow", "兄弟"))
        self.label.setText(_translate("MainWindow", "輸入關鍵字"))
        self.label_27.setText(_translate("MainWindow", "輸入日期，格式:yyyy-mm-dd"))
        self.pushButton_17.setText(_translate("MainWindow", "發文頻率分析"))
        self.pushButton_18.setText(_translate("MainWindow", "關鍵字頻率分析"))
        self.label_13.setText(_translate("MainWindow", "開始"))
        self.label_14.setText(_translate("MainWindow", "結束"))
        self.label_15.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Microsoft JhengHei\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'PMingLiU\'; font-size:12pt;\">發文頻率分析:該版面在該段時間內，每天發出多少文章，以此做成序列，若要使用該功能不必填關鍵字。</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'PMingLiU\'; font-size:12pt;\">關鍵字頻率分析:輸入的關鍵字在該版面的文章每天出現多少次，以此做成序列，若要使用此功能必須要填入關鍵字。</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'PMingLiU\'; font-size:12pt;\">日期範例 : 2018-05-09 ~ 2018-05-11</span></p></body></html>"))
        self.pushButton_19.setText(_translate("MainWindow", "打開網址列表"))
        self.label_24.setText(_translate("MainWindow", "注:執行關鍵字分析後使用"))
        self.checkBox.setText(_translate("MainWindow", "打開情感分析"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "自定義分析"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p>說明:左方顯示最新的1000篇文章中，出現次數最多的字詞，右邊為跟據左方數據產生的文字雲</p><p>格式為:詞彙 出現次數</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "整版文字分析"))
        self.label_17.setText(_translate("MainWindow", "輸入自訂看板名稱"))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p>注意 : 要分析目前資料庫不支援的看板的話，因為要重新從爬蟲開始跑的緣故，可能會消耗大量時間</p></body></html>"))
        self.label_19.setText(_translate("MainWindow", "篇數"))
        self.label_20.setText(_translate("MainWindow", "資料庫最終更新時間:"))
        self.checkBox_2.setText(_translate("MainWindow", "使用自己的資料庫"))
        self.label_23.setText(_translate("MainWindow", "金鑰檔案位置"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "選項"))
        self.pushButton_16.setText(_translate("MainWindow", "refresh"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Baseball"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Steam"))
        self.lineEdit_6.setText(_translate("MainWindow", "100"))
        self.label_21.setText(_translate("MainWindow", "文章篇數"))
        self.label_22.setText(_translate("MainWindow", "切換看板"))

