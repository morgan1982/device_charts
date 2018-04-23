# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(871, 580)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.total_btn = QtGui.QPushButton(self.centralwidget)
        self.total_btn.setGeometry(QtCore.QRect(0, 100, 75, 23))
        self.total_btn.setObjectName(_fromUtf8("total_btn"))
        self.price_tedit_1 = QtGui.QTextEdit(self.centralwidget)
        self.price_tedit_1.setGeometry(QtCore.QRect(80, 0, 104, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.price_tedit_1.setPalette(palette)
        self.price_tedit_1.setFrameShadow(QtGui.QFrame.Raised)
        self.price_tedit_1.setObjectName(_fromUtf8("price_tedit_1"))
        self.price_tedit_2 = QtGui.QTextEdit(self.centralwidget)
        self.price_tedit_2.setGeometry(QtCore.QRect(80, 40, 104, 31))
        self.price_tedit_2.setObjectName(_fromUtf8("price_tedit_2"))
        self.price_tedit_4 = QtGui.QTextEdit(self.centralwidget)
        self.price_tedit_4.setGeometry(QtCore.QRect(80, 120, 104, 31))
        self.price_tedit_4.setObjectName(_fromUtf8("price_tedit_4"))
        self.price_tedit_3 = QtGui.QTextEdit(self.centralwidget)
        self.price_tedit_3.setGeometry(QtCore.QRect(80, 80, 104, 31))
        self.price_tedit_3.setObjectName(_fromUtf8("price_tedit_3"))
        self.price_tedit_5 = QtGui.QTextEdit(self.centralwidget)
        self.price_tedit_5.setGeometry(QtCore.QRect(80, 160, 104, 31))
        self.price_tedit_5.setObjectName(_fromUtf8("price_tedit_5"))
        self.part_spx = QtGui.QSpinBox(self.centralwidget)
        self.part_spx.setGeometry(QtCore.QRect(10, 0, 42, 22))
        self.part_spx.setObjectName(_fromUtf8("part_spx"))
        self.nr_chbox = QtGui.QCheckBox(self.centralwidget)
        self.nr_chbox.setGeometry(QtCore.QRect(10, 30, 70, 17))
        self.nr_chbox.setObjectName(_fromUtf8("nr_chbox"))
        self.lc_chbox = QtGui.QCheckBox(self.centralwidget)
        self.lc_chbox.setGeometry(QtCore.QRect(10, 50, 70, 17))
        self.lc_chbox.setObjectName(_fromUtf8("lc_chbox"))
        self.nr_lc_chbox = QtGui.QCheckBox(self.centralwidget)
        self.nr_lc_chbox.setGeometry(QtCore.QRect(10, 70, 70, 17))
        self.nr_lc_chbox.setObjectName(_fromUtf8("nr_lc_chbox"))
        self.total_lcd = QtGui.QLCDNumber(self.centralwidget)
        self.total_lcd.setGeometry(QtCore.QRect(110, 200, 71, 41))
        self.total_lcd.setObjectName(_fromUtf8("total_lcd"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 220, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.plt_widget = QtGui.QWidget(self.centralwidget)
        self.plt_widget.setGeometry(QtCore.QRect(200, 40, 651, 491))
        self.plt_widget.setObjectName(_fromUtf8("plt_widget"))
        self.dist_btn = QtGui.QPushButton(self.centralwidget)
        self.dist_btn.setGeometry(QtCore.QRect(30, 290, 75, 23))
        self.dist_btn.setObjectName(_fromUtf8("dist_btn"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 871, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.price_tedit_5.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.price_tedit_4.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.price_tedit_3.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.price_tedit_2.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.price_tedit_1.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.total_btn.setText(_translate("MainWindow", "get price", None))
        self.nr_chbox.setText(_translate("MainWindow", "nr", None))
        self.lc_chbox.setText(_translate("MainWindow", "lc", None))
        self.nr_lc_chbox.setText(_translate("MainWindow", "nr and lc", None))
        self.pushButton_2.setText(_translate("MainWindow", "clear", None))
        self.dist_btn.setText(_translate("MainWindow", "dist", None))

