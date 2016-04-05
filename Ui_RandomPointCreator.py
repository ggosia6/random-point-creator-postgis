# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file Ui_RandomPointCreator.ui
# Created with: PyQt4 UI code generator 4.4.4
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_RandomPointCreator(object):
    def setupUi(self, RandomPointCreator):
        RandomPointCreator.setObjectName("RandomPointCreator")
        RandomPointCreator.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(RandomPointCreator)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(RandomPointCreator)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), RandomPointCreator.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), RandomPointCreator.reject)
        QtCore.QMetaObject.connectSlotsByName(RandomPointCreator)

    def retranslateUi(self, RandomPointCreator):
        RandomPointCreator.setWindowTitle(QtGui.QApplication.translate("RandomPointCreator", "RandomPointCreator", None, QtGui.QApplication.UnicodeUTF8))
