# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'popup.ui'
#
# Created: Fri Apr 22 13:09:18 2016
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(324, 86)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 20, 241, 16))
        self.label.setObjectName("label")
        self.okidoki = QtWidgets.QPushButton(Dialog)
        self.okidoki.setGeometry(QtCore.QRect(110, 50, 83, 24))
        self.okidoki.setObjectName("okidoki")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Der Text wurde hinreichend gelöscht."))
        self.okidoki.setText(_translate("Dialog", "Okidoki!"))

