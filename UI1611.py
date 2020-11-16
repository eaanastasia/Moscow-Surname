# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI1611.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(789, 515)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(270, 10, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setItalic(True)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(True)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Кнопка"))
