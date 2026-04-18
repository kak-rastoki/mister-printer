# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(555, 810)
        MainWindow.setMinimumSize(QSize(555, 800))
        MainWindow.setMaximumSize(QSize(555, 810))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        font.setBold(False)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QMainWindow{\n"
"background-color:#7db8f0;\n"
"} \n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 60, 501, 131))
        self.groupBox.setStyleSheet(u"QGroupBox{\n"
"border:2px solid white;\n"
"border-radius:10px;\n"
"}")
        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(20, 70, 451, 41))
        self.comboBox.setStyleSheet(u"QComboBox {\n"
"   \n"
"    font-size: 13px; /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"\n"
"    background-color: #dae7f0;\n"
"    border-radius: 13px; /* \u0413\u0440\u0430\u043d\u0438\u0446\u044b */\n"
"    padding: 2px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"}\n"
"\n"
"\n"
"QComboBox::item:selected{\n"
"font-size:20pt;\n"
"color:white;\n"
"background-color: #64d4e3;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: #64d4e3; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"    color: #ffffff; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 20, 441, 50))
        font1 = QFont()
        font1.setFamilies([u"Arial Black"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(30, 200, 501, 130))
        self.groupBox_2.setStyleSheet(u"QGroupBox{\n"
"border:2px solid white;\n"
"border-radius:10px;\n"
"}")
        self.comboBox_2 = QComboBox(self.groupBox_2)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(20, 70, 451, 41))
        self.comboBox_2.setStyleSheet(u"QComboBox {\n"
"   \n"
"    font-size: 13px; /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"\n"
"    background-color: #dae7f0;\n"
"    border-radius: 13px; /* \u0413\u0440\u0430\u043d\u0438\u0446\u044b */\n"
"    padding: 2px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"}\n"
"\n"
"\n"
"QComboBox::item:selected{\n"
"font-size:20pt;\n"
"color:white;\n"
"background-color: #64d4e3;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: #64d4e3; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"    color: #ffffff; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 20, 441, 50))
        font2 = QFont()
        font2.setFamilies([u"Arial Black"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"")
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(30, 340, 501, 131))
        self.groupBox_3.setStyleSheet(u"QGroupBox{\n"
"border:2px solid white;\n"
"border-radius:10px;\n"
"}")
        self.comboBox_3 = QComboBox(self.groupBox_3)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(20, 70, 451, 41))
        self.comboBox_3.setStyleSheet(u"QComboBox {\n"
"   \n"
"    font-size: 13px; /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"\n"
"    background-color: #dae7f0;\n"
"    border-radius: 13px; /* \u0413\u0440\u0430\u043d\u0438\u0446\u044b */\n"
"    padding: 2px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"}\n"
"\n"
"\n"
"QComboBox::item:selected{\n"
"font-size:20pt;\n"
"color:white;\n"
"background-color: #64d4e3;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: #64d4e3; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"    color: #ffffff; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}")
        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(120, 20, 441, 50))
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"")
        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(30, 480, 501, 131))
        self.groupBox_4.setStyleSheet(u"QGroupBox{\n"
"border:2px solid white;\n"
"border-radius:10px;\n"
"}")
        self.comboBox_7 = QComboBox(self.groupBox_4)
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.setObjectName(u"comboBox_7")
        self.comboBox_7.setGeometry(QRect(20, 70, 451, 41))
        self.comboBox_7.setStyleSheet(u"QComboBox {\n"
"   \n"
"    font-size: 13px; /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"\n"
"    background-color: #dae7f0;\n"
"    border-radius: 13px; /* \u0413\u0440\u0430\u043d\u0438\u0446\u044b */\n"
"    padding: 2px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"}\n"
"\n"
"\n"
"QComboBox::item:selected{\n"
"font-size:20pt;\n"
"color:white;\n"
"background-color: #64d4e3;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: #64d4e3; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"    color: #ffffff; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}")
        self.label_7 = QLabel(self.groupBox_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(60, 20, 441, 50))
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 730, 501, 31))
        self.pushButton.setStyleSheet(u"QPushButton{border:2px solid #99c6f0;\n"
"background-color:white;\n"
"border-radius:10px;\n"
"width:100px;\n"
"height:100px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{border:2px solid blue;\n"
"background-color:#ededed;\n"
"\n"
"\n"
"\n"
"}")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(30, 620, 501, 101))
        self.textEdit.setStyleSheet(u"background-color: #dae7f0;;\n"
"border-radius:15px;")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(70, 0, 441, 50))
        font3 = QFont()
        font3.setFamilies([u"Arial Black"])
        font3.setPointSize(16)
        font3.setBold(True)
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"color:white;\n"
"text-shadow:2px 2px 4px rgba(0, 0, 0, 0.5);")
        self.label_4.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 555, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Mr. Printer", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 1. \u0418\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0444\u0435\u0441\u0441\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u043e\u0435 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u041e\u0444\u0438\u0441\u043d\u043e\u0435 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043c\u0430\u0448\u043d\u0435\u0435 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u0438\u0435", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043a \u0442\u044b \u043f\u043b\u0430\u043d\u0438\u0440\u0443\u0435\u0448\u044c \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u044c \u043f\u0440\u0438\u043d\u0442\u0435\u0440?", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 2. \u0426\u0432\u0435\u0442\u043d\u0430\u044f \u043f\u0435\u0447\u0430\u0442\u044c", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0414\u0430", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043b\u0430\u043d\u0438\u0440\u0443\u0435\u0442\u0441\u044f \u043f\u0435\u0447\u0430\u0442\u0430\u0442\u044c \u0447\u0442\u043e-\u0442\u043e \u0432 \u0446\u0432\u0435\u0442\u0435?", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 3. \u0411\u044e\u0434\u0436\u0435\u0442", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0414\u0430", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0411\u044e\u0434\u0436\u0435\u0442 \u043c\u0435\u043d\u044c\u0448\u0435 30 000?", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 4. \u041e\u0431\u044a\u0435\u043c \u043f\u0435\u0447\u0430\u0442\u0438", None))
        self.comboBox_7.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0414\u0430", None))
        self.comboBox_7.setItemText(1, QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))

        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043d\u043e\u0433\u043e \u043f\u043b\u0430\u043d\u0438\u0440\u0443\u0435\u0442\u0441\u044f \u043f\u0435\u0447\u0430\u0442\u0430\u0442\u044c?", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u041e\u0418\u0421\u041a ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Mr.Printer", None))
    # retranslateUi
