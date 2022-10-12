# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'validationView_reemplazoLHarUi.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 500)
        self.actionEspa_ol = QAction(MainWindow)
        self.actionEspa_ol.setObjectName(u"actionEspa_ol")
        self.actionEnglish = QAction(MainWindow)
        self.actionEnglish.setObjectName(u"actionEnglish")
        self.actionDeutsch = QAction(MainWindow)
        self.actionDeutsch.setObjectName(u"actionDeutsch")
        self.actionItaliane = QAction(MainWindow)
        self.actionItaliane.setObjectName(u"actionItaliane")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(140, 300, 320, 40))
        self.lineEdit.setStyleSheet(u"border-radius: 10px;")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 600, 500))
        self.frame.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 240, 391, 61))
        font = QFont()
        font.setFamilies([u"Arial Rounded MT Bold"])
        font.setPointSize(20)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(250, 360, 100, 40))
        font1 = QFont()
        font1.setFamilies([u"Arial Rounded MT Bold"])
        font1.setPointSize(10)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(66, 66, 66);\n"
"color: rgb(255, 255, 255);")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(50, 60, 501, 161))
        self.frame_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"image: url(:/automata/automata.png);\n"
"border-radius: 10px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.pushButtonEspanol = QPushButton(self.frame)
        self.pushButtonEspanol.setObjectName(u"pushButtonEspanol")
        self.pushButtonEspanol.setGeometry(QRect(0, 0, 100, 30))
        self.pushButtonEspanol.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButtonEnglish = QPushButton(self.frame)
        self.pushButtonEnglish.setObjectName(u"pushButtonEnglish")
        self.pushButtonEnglish.setGeometry(QRect(100, 0, 100, 30))
        self.pushButtonEnglish.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButtonDeutsch = QPushButton(self.frame)
        self.pushButtonDeutsch.setObjectName(u"pushButtonDeutsch")
        self.pushButtonDeutsch.setGeometry(QRect(200, 0, 100, 30))
        self.pushButtonDeutsch.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButtonItaliane = QPushButton(self.frame)
        self.pushButtonItaliane.setObjectName(u"pushButtonItaliane")
        self.pushButtonItaliane.setGeometry(QRect(300, 0, 100, 30))
        self.pushButtonItaliane.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.frame.raise_()
        self.lineEdit.raise_()

        self.retranslateUi(MainWindow)
        self.pushButtonItaliane.clicked.connect(self.pushButtonItaliane.click)
        self.pushButtonDeutsch.clicked.connect(self.pushButtonDeutsch.click)
        self.pushButtonEnglish.clicked.connect(self.pushButtonEnglish.click)
        self.pushButtonEspanol.clicked.connect(self.pushButtonEspanol.click)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionEspa_ol.setText(QCoreApplication.translate("MainWindow", u"Espa\u00f1ol", None))
        self.actionEnglish.setText(QCoreApplication.translate("MainWindow", u"English", None))
        self.actionDeutsch.setText(QCoreApplication.translate("MainWindow", u"Deutsch", None))
        self.actionItaliane.setText(QCoreApplication.translate("MainWindow", u"Italiane", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Ingrese la(s) palabra(s)", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Comprobar", None))
        self.pushButtonEspanol.setText(QCoreApplication.translate("MainWindow", u"Espa\u00f1ol", None))
        self.pushButtonEnglish.setText(QCoreApplication.translate("MainWindow", u"English", None))
        self.pushButtonDeutsch.setText(QCoreApplication.translate("MainWindow", u"Deutsch", None))
        self.pushButtonItaliane.setText(QCoreApplication.translate("MainWindow", u"Italiane", None))
    # retranslateUi

