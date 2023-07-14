# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1258, 748)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(-10, 0, 1271, 741))
        self.stackedWidget.setMaximumSize(QtCore.QSize(666666, 16777215))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(210, 140, 821, 101))
        self.label.setStyleSheet("font: 30pt \"Microsoft YaHei UI\";")
        self.label.setObjectName("label")
        self.pushButton = PrimaryPushButton(self.page)
        self.pushButton.setGeometry(QtCore.QRect(520, 370, 191, 91))
        self.pushButton.setStyleSheet("font: 18pt \"Dubai\";")
        self.pushButton.setObjectName("pushButton")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setGeometry(QtCore.QRect(160, 250, 101, 31))
        self.label_2.setStyleSheet("font: 16pt \"Microsoft YaHei UI\";")
        self.label_2.setObjectName("label_2")
        self.comboBox = ComboBox(self.page_2)
        self.comboBox.setGeometry(QtCore.QRect(160, 310, 291, 31))
        self.comboBox.setStyleSheet("font: 14pt \"Microsoft YaHei UI\";")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_3 = QtWidgets.QLabel(self.page_2)
        self.label_3.setGeometry(QtCore.QRect(610, 240, 201, 191))
        self.label_3.setStyleSheet("border-image: url(:/image/bitbug_favicon2.ico);\n"
"border-radius:10px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.page_2)
        self.label_4.setGeometry(QtCore.QRect(820, 260, 221, 71))
        self.label_4.setStyleSheet("font: 25pt \"Microsoft YaHei UI\";\n"
"color: rgb(118, 118, 118);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.page_2)
        self.label_5.setGeometry(QtCore.QRect(820, 310, 481, 131))
        self.label_5.setStyleSheet("font: 25pt \"Microsoft YaHei UI\";\n"
"")
        self.label_5.setObjectName("label_5")
        self.pushButton_2 = PrimaryPushButton(self.page_2)
        self.pushButton_2.setGeometry(QtCore.QRect(1080, 660, 111, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = PrimaryPushButton(self.page_2)
        self.pushButton_3.setGeometry(QtCore.QRect(160, 360, 51, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_7 = QtWidgets.QLabel(self.page_3)
        self.label_7.setGeometry(QtCore.QRect(140, 340, 421, 16))
        self.label_7.setStyleSheet("color: rgb(130, 130, 130);")
        self.label_7.setObjectName("label_7")
        self.label_13 = QtWidgets.QLabel(self.page_3)
        self.label_13.setGeometry(QtCore.QRect(120, 120, 291, 111))
        self.label_13.setStyleSheet("font: 20pt \"Microsoft YaHei UI\";")
        self.label_13.setObjectName("label_13")
        self.label_8 = QtWidgets.QLabel(self.page_3)
        self.label_8.setGeometry(QtCore.QRect(110, 290, 31, 31))
        self.label_8.setStyleSheet("border-image: url(:/image/resource/image/_fluent_folderr.png);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(self.page_3)
        self.label_10.setGeometry(QtCore.QRect(150, 290, 201, 31))
        self.label_10.setStyleSheet("font: 16pt \"Microsoft YaHei UI\";")
        self.label_10.setObjectName("label_10")
        self.comboBox_2 = ComboBox(self.page_3)
        self.comboBox_2.setGeometry(QtCore.QRect(350, 290, 191, 41))
        self.comboBox_2.setObjectName("comboBox_2")
        self.pushButton_7 = PrimaryPushButton(self.page_3)
        self.pushButton_7.setGeometry(QtCore.QRect(550, 290, 41, 41))
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_9 = QtWidgets.QLabel(self.page_3)
        self.label_9.setGeometry(QtCore.QRect(110, 370, 31, 31))
        self.label_9.setStyleSheet("border-image: url(:/image/resource/image/book.png);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_12 = QtWidgets.QLabel(self.page_3)
        self.label_12.setGeometry(QtCore.QRect(150, 370, 151, 31))
        self.label_12.setStyleSheet("font: 16pt \"Microsoft YaHei UI\";")
        self.label_12.setObjectName("label_12")
        self.comboBox_3 = ComboBox(self.page_3)
        self.comboBox_3.setGeometry(QtCore.QRect(330, 370, 161, 41))
        self.comboBox_3.setObjectName("comboBox_3")
        self.pushButton_8 = PrimaryPushButton(self.page_3)
        self.pushButton_8.setGeometry(QtCore.QRect(500, 370, 41, 41))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = PrimaryPushButton(self.page_3)
        self.pushButton_9.setGeometry(QtCore.QRect(550, 370, 71, 41))
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_14 = QtWidgets.QLabel(self.page_3)
        self.label_14.setGeometry(QtCore.QRect(680, 160, 541, 281))
        self.label_14.setStyleSheet("font: 15pt \"Microsoft YaHei UI\";\n"
"")
        self.label_14.setObjectName("label_14")
        self.pushButton_5 = PrimaryPushButton(self.page_3)
        self.pushButton_5.setGeometry(QtCore.QRect(950, 660, 111, 51))
        self.pushButton_5.setStyleSheet("font:10pt \"Dubai\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_4 = PrimaryPushButton(self.page_3)
        self.pushButton_4.setGeometry(QtCore.QRect(1080, 660, 111, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.label_15 = QtWidgets.QLabel(self.page_4)
        self.label_15.setGeometry(QtCore.QRect(50, 150, 431, 381))
        self.label_15.setStyleSheet("font: 15pt \"Microsoft YaHei UI\";\n"
"")
        self.label_15.setObjectName("label_15")
        self.label_17 = QtWidgets.QLabel(self.page_4)
        self.label_17.setGeometry(QtCore.QRect(640, 180, 121, 31))
        self.label_17.setStyleSheet("font: 20pt \"Microsoft YaHei UI\";")
        self.label_17.setObjectName("label_17")
        self.label_11 = QtWidgets.QLabel(self.page_4)
        self.label_11.setGeometry(QtCore.QRect(630, 320, 421, 16))
        self.label_11.setStyleSheet("color: rgb(130, 130, 130);")
        self.label_11.setObjectName("label_11")
        self.label_20 = QtWidgets.QLabel(self.page_4)
        self.label_20.setGeometry(QtCore.QRect(690, 220, 91, 61))
        self.label_20.setStyleSheet("font: 15pt \"Microsoft YaHei UI\";\n"
"color: rgb(147, 147, 147);")
        self.label_20.setObjectName("label_20")
        self.label_19 = QtWidgets.QLabel(self.page_4)
        self.label_19.setGeometry(QtCore.QRect(650, 230, 31, 31))
        self.label_19.setStyleSheet("border-image: url(:/image/resource/image/ic_fluent_inprivate_account_24_regular.png);")
        self.label_19.setText("")
        self.label_19.setObjectName("label_19")
        self.comboBox_4 = ComboBox(self.page_4)
        self.comboBox_4.setGeometry(QtCore.QRect(640, 280, 201, 41))
        self.comboBox_4.setObjectName("comboBox_4")
        self.pushButton_10 = PrimaryPushButton(self.page_4)
        self.pushButton_10.setGeometry(QtCore.QRect(870, 280, 181, 41))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = HyperlinkButton(self.page_4)
        self.pushButton_11.setGeometry(QtCore.QRect(630, 340, 221, 31))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = HyperlinkButton(self.page_4)
        self.pushButton_12.setGeometry(QtCore.QRect(860, 340, 191, 31))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_6 = PrimaryPushButton(self.page_4)
        self.pushButton_6.setGeometry(QtCore.QRect(1080, 660, 111, 51))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_13 = PrimaryPushButton(self.page_4)
        self.pushButton_13.setGeometry(QtCore.QRect(950, 660, 111, 51))
        self.pushButton_13.setStyleSheet("font:10pt \"Dubai\";")
        self.pushButton_13.setObjectName("pushButton_13")
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.label_21 = QtWidgets.QLabel(self.page_5)
        self.label_21.setGeometry(QtCore.QRect(340, 170, 201, 31))
        self.label_21.setStyleSheet("font: 20pt \"Microsoft YaHei UI\";")
        self.label_21.setObjectName("label_21")
        self.lineEdit = LineEdit(self.page_5)
        self.lineEdit.setGeometry(QtCore.QRect(340, 230, 581, 51))
        self.lineEdit.setStyleSheet("font: 15pt \"Microsoft YaHei UI\";")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_15 = PrimaryPushButton(self.page_5)
        self.pushButton_15.setGeometry(QtCore.QRect(810, 320, 111, 51))
        self.pushButton_15.setObjectName("pushButton_15")
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.label_22 = QtWidgets.QLabel(self.page_6)
        self.label_22.setGeometry(QtCore.QRect(30, 270, 191, 191))
        self.label_22.setStyleSheet("border-image: url(:/image/bitbug_favicon2.ico);\n"
"border-radius:10px;")
        self.label_22.setText("")
        self.label_22.setObjectName("label_22")
        self.label_24 = QtWidgets.QLabel(self.page_6)
        self.label_24.setGeometry(QtCore.QRect(230, 260, 481, 131))
        self.label_24.setStyleSheet("font: 25pt \"Microsoft YaHei UI\";\n"
"")
        self.label_24.setObjectName("label_24")
        self.label_23 = QtWidgets.QLabel(self.page_6)
        self.label_23.setGeometry(QtCore.QRect(230, 360, 221, 71))
        self.label_23.setStyleSheet("font: 25pt \"Microsoft YaHei UI\";\n"
"color: rgb(118, 118, 118);")
        self.label_23.setObjectName("label_23")
        self.label_25 = QtWidgets.QLabel(self.page_6)
        self.label_25.setGeometry(QtCore.QRect(690, 150, 541, 331))
        self.label_25.setStyleSheet("font: 30pt \"Microsoft YaHei UI\";\n"
"color: rgb(147, 147, 147);")
        self.label_25.setObjectName("label_25")
        self.pushButton_16 = PrimaryPushButton(self.page_6)
        self.pushButton_16.setGeometry(QtCore.QRect(690, 390, 111, 61))
        self.pushButton_16.setObjectName("pushButton_16")
        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.page_7)
        self.stackedWidget_2.setGeometry(QtCore.QRect(60, 40, 1191, 651))
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_10 = QtWidgets.QWidget()
        self.page_10.setObjectName("page_10")
        self.stackedWidget_2.addWidget(self.page_10)
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setObjectName("page_8")
        self.pushButton_14 = PrimaryPushButton(self.page_8)
        self.pushButton_14.setGeometry(QtCore.QRect(860, 490, 171, 91))
        self.pushButton_14.setObjectName("pushButton_14")
        self.comboBox_5 = ComboBox(self.page_8)
        self.comboBox_5.setGeometry(QtCore.QRect(70, 500, 291, 71))
        self.comboBox_5.setStyleSheet("font: 14pt \"Microsoft YaHei UI\";")
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.pushButton_17 = QtWidgets.QPushButton(self.page_8)
        self.pushButton_17.setGeometry(QtCore.QRect(580, 600, 51, 41))
        self.pushButton_17.setStyleSheet("\n"
"QPushButton{\n"
"    \n"
"    \n"
"    background-color: rgb(255, 255, 255,20%);\n"
"    color:white;\n"
"    box-shadow: 1px 1px 3px rgba(165,0,5,1.3);font-size:16px;border-radius: 0px;font-family: 微软雅黑;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    image: url(:/image/resource/image/箭头下.png);\n"
"    \n"
"}\n"
"QPushButton:pressed{\n"
"    \n"
"}")
        self.pushButton_17.setText("")
        self.pushButton_17.setObjectName("pushButton_17")
        self.stackedWidget_2.addWidget(self.page_8)
        self.page_9 = QtWidgets.QWidget()
        self.page_9.setObjectName("page_9")
        self.pushButton_18 = QtWidgets.QPushButton(self.page_9)
        self.pushButton_18.setGeometry(QtCore.QRect(130, 70, 211, 221))
        self.pushButton_18.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"    \n"
"    image: url(:/image/resource/image/icon0ab8a4c5.png);\n"
"    background-color: rgb(170, 170, 170,10%);\n"
"}\n"
"QPushButton:hover {\n"
"    border: 15px solid rgb(152, 152, 152, 0%);\n"
"    background-color: rgb(170, 170, 170,40%);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color:rgb(152, 152, 152,50%);\n"
"    border-radius: 0px;    \n"
"}")
        self.pushButton_18.setText("")
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.page_9)
        self.pushButton_19.setGeometry(QtCore.QRect(400, 70, 191, 301))
        self.pushButton_19.setStyleSheet("QPushButton {\n"
"    \n"
"    font: 15pt \"Microsoft YaHei UI\";\n"
"    \n"
"    image: url(:/image/resource/image/icon3662e120.png);\n"
"    background-color: rgb(170, 170, 170,10%);\n"
"}\n"
"QPushButton:hover {\n"
"    border: 10px solid rgb(152, 152, 152, 0%);\n"
"    background-color: rgb(170, 170, 170,40%);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color:rgb(152, 152, 152,50%);\n"
"    border-radius: 0px;    \n"
"}")
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.page_9)
        self.pushButton_20.setGeometry(QtCore.QRect(620, 70, 341, 111))
        self.pushButton_20.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"    image: url(:/image/resource/image/Chrome.png);\n"
"    \n"
"    background-color: rgb(170, 170, 170,10%);\n"
"}\n"
"QPushButton:hover {\n"
"    border: 5px solid rgb(152, 152, 152, 0%);\n"
"    background-color: rgb(170, 170, 170,40%);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color:rgb(152, 152, 152,50%);\n"
"    border-radius: 0px;    \n"
"}")
        self.pushButton_20.setText("")
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.page_9)
        self.pushButton_21.setGeometry(QtCore.QRect(790, 360, 171, 171))
        self.pushButton_21.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"    \n"
"    image: url(:/image/resource/image/设置-01.png);\n"
"    background-color: rgb(170, 170, 170,10%);\n"
"}\n"
"QPushButton:hover {\n"
"    border: 40px solid rgb(152, 152, 152, 0%);\n"
"    background-color: rgb(170, 170, 170,40%);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color:rgb(152, 152, 152,50%);\n"
"    border-radius: 0px;    \n"
"}")
        self.pushButton_21.setText("")
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_22 = QtWidgets.QPushButton(self.page_9)
        self.pushButton_22.setGeometry(QtCore.QRect(130, 340, 211, 191))
        self.pushButton_22.setStyleSheet("QPushButton {\n"
"    \n"
"    background-color: rgb(170, 170, 170,10%);\n"
"}\n"
"QPushButton:hover {\n"
"    border: 40px solid rgb(152, 152, 152, 0%);\n"
"    background-color: rgb(170, 170, 170,40%);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color:rgb(152, 152, 152,50%);\n"
"    border-radius: 0px;    \n"
"}")
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_23 = QtWidgets.QPushButton(self.page_9)
        self.pushButton_23.setGeometry(QtCore.QRect(380, 410, 221, 121))
        self.pushButton_23.setStyleSheet("QPushButton {\n"
"    image: url(:/image/resource/image/icon2979dab5.png);\n"
"    background-color: rgb(170, 170, 170,10%);\n"
"}\n"
"QPushButton:hover {\n"
"    border: 5px solid rgb(152, 152, 152, 0%);\n"
"    background-color: rgb(170, 170, 170,40%);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color:rgb(152, 152, 152,50%);\n"
"    border-radius: 0px;    \n"
"}")
        self.pushButton_23.setText("")
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_24 = QtWidgets.QPushButton(self.page_9)
        self.pushButton_24.setGeometry(QtCore.QRect(620, 220, 151, 311))
        self.pushButton_24.setStyleSheet("QPushButton {\n"
"    \n"
"    background-color: rgb(170, 170, 170,10%);\n"
"}\n"
"QPushButton:hover {\n"
"    border: 40px solid rgb(152, 152, 152, 0%);\n"
"    background-color: rgb(170, 170, 170,40%);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color:rgb(152, 152, 152,50%);\n"
"    border-radius: 0px;    \n"
"}")
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_25 = QtWidgets.QPushButton(self.page_9)
        self.pushButton_25.setGeometry(QtCore.QRect(790, 220, 171, 101))
        self.pushButton_25.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"    image: url(:/image/resource/image/icon6144ed28.png);\n"
"    background-color: rgb(170, 170, 170,10%);\n"
"}\n"
"QPushButton:hover {\n"
"    border: 5px solid rgb(152, 152, 152, 0%);\n"
"    background-color: rgb(170, 170, 170,40%);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color:rgb(152, 152, 152,50%);\n"
"    border-radius: 0px;    \n"
"}")
        self.pushButton_25.setText("")
        self.pushButton_25.setObjectName("pushButton_25")
        self.label_6 = QtWidgets.QLabel(self.page_9)
        self.label_6.setGeometry(QtCore.QRect(40, 30, 101, 41))
        self.label_6.setStyleSheet("font: 20pt \"Microsoft YaHei UI\";")
        self.label_6.setObjectName("label_6")
        self.pushButton_26 = QtWidgets.QPushButton(self.page_9)
        self.pushButton_26.setGeometry(QtCore.QRect(570, 10, 41, 41))
        self.pushButton_26.setStyleSheet("\n"
"QPushButton{\n"
"    \n"
"    \n"
"    background-color: rgb(255, 255, 255,20%);\n"
"    color:white;\n"
"    box-shadow: 1px 1px 3px rgba(165,0,5,1.3);font-size:16px;border-radius: 0px;font-family: 微软雅黑;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    \n"
"    \n"
"    image: url(:/image/resource/image/箭头上.png);\n"
"    \n"
"}\n"
"QPushButton:pressed{\n"
"    \n"
"}")
        self.pushButton_26.setText("")
        self.pushButton_26.setObjectName("pushButton_26")
        self.stackedWidget_2.addWidget(self.page_9)
        self.stackedWidget.addWidget(self.page_7)


        self.retranslateUi(MainWindow)

        self.stackedWidget_2.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "You seem to need some settings to use it"))
        self.pushButton.setText(_translate("MainWindow", "START"))
        self.label_2.setText(_translate("MainWindow", "language"))
        self.comboBox.setItemText(0, _translate("MainWindow", "en-US, English"))
        self.comboBox.setItemText(1, _translate("MainWindow", "zh-CN, 简体中文(中国)"))
        self.comboBox.setItemText(2, _translate("MainWindow", "zh-TW, 繁体中文(中国台湾)"))
        self.comboBox.setItemText(3, _translate("MainWindow", "zh-HK, 繁体中文(中国香港)"))
        self.label_4.setText(_translate("MainWindow", "RETE STUDIO"))
        self.label_5.setText(_translate("MainWindow", "Yes MineCraft Launcher"))
        self.pushButton_2.setText(_translate("MainWindow", "Next"))
        self.pushButton_3.setText(_translate("MainWindow", "OK"))
        self.label_7.setText(_translate("MainWindow", "--------------------------------------------------------------------------"))
        self.label_13.setText(_translate("MainWindow", "Basic startup settings"))
        self.label_10.setText(_translate("MainWindow", ".minecraft directory"))
        self.pushButton_7.setText(_translate("MainWindow", "+"))
        self.label_12.setText(_translate("MainWindow", "JAVA runtime"))
        self.pushButton_8.setText(_translate("MainWindow", "+"))
        self.pushButton_9.setText(_translate("MainWindow", "search"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p>You need at least one. minecraft directory </p><p>to store your game core<br/></p><p>You need at least one Java runtime </p><p>to start your game core</p><p><br/></p><p>After completion, you can also modify </p><p>these settings in the global game settings</p></body></html>"))
        self.pushButton_5.setText(_translate("MainWindow", "Back"))
        self.pushButton_4.setText(_translate("MainWindow", "Next"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p>You need at least one account </p><p>to start the game</p><p><br/></p><p>Only Microsoft accounts can access </p><p>online servers</p><p><br/></p><p>Offline account cannot be verified </p><p>by the server</p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "account "))
        self.label_11.setText(_translate("MainWindow", "--------------------------------------------------------------------------"))
        self.label_20.setText(_translate("MainWindow", "account "))
        self.pushButton_10.setText(_translate("MainWindow", "Login Microsoft account"))
        self.pushButton_11.setText(_translate("MainWindow", "Don\'t have a Microsoft account?"))
        self.pushButton_12.setText(_translate("MainWindow", "Minecraft official website"))
        self.pushButton_6.setText(_translate("MainWindow", "Next"))
        self.pushButton_13.setText(_translate("MainWindow", "Back"))
        self.label_21.setText(_translate("MainWindow", "Offline account"))
        self.pushButton_15.setText(_translate("MainWindow", "increase"))
        self.label_24.setText(_translate("MainWindow", "Yes MineCraft Launcher"))
        self.label_23.setText(_translate("MainWindow", "RETE STUDIO"))
        self.label_25.setText(_translate("MainWindow", "<html><head/><body><p>Yes MineCraft Launcher</p><p>We\'re ready! Let\'s get start!</p></body></html>"))
        self.pushButton_16.setText(_translate("MainWindow", "现在打开！"))
        self.pushButton_14.setText(_translate("MainWindow", "启动游戏\n"
"22w13oneblockatatime"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "22w13oneblockatatime"))
        self.pushButton_19.setText(_translate("MainWindow", "  \n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"YES Tips"))
        self.pushButton_22.setText(_translate("MainWindow", "敬请期待"))
        self.pushButton_24.setText(_translate("MainWindow", "敬请期待"))
        self.label_6.setText(_translate("MainWindow", "start"))
from qfluentwidgets import ComboBox, HyperlinkButton, LineEdit, PrimaryPushButton
import kjlk_rc
