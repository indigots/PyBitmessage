# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'createchatdialog.ui'
#
# Created: Wed Oct 29 21:50:34 2014
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_CreateChatDialog(object):
    def setupUi(self, CreateChatDialog):
        CreateChatDialog.setObjectName(_fromUtf8("CreateChatDialog"))
        CreateChatDialog.resize(349, 148)
        self.formLayout_2 = QtGui.QFormLayout(CreateChatDialog)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.subjectLabel = QtGui.QLabel(CreateChatDialog)
        self.subjectLabel.setObjectName(_fromUtf8("subjectLabel"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.subjectLabel)
        self.nickLabel = QtGui.QLabel(CreateChatDialog)
        self.nickLabel.setObjectName(_fromUtf8("nickLabel"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.nickLabel)
        self.passLabel = QtGui.QLabel(CreateChatDialog)
        self.passLabel.setObjectName(_fromUtf8("passLabel"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.passLabel)
        self.buttonBox = QtGui.QDialogButtonBox(CreateChatDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.FieldRole, self.buttonBox)
        self.nickLine = QtGui.QLineEdit(CreateChatDialog)
        self.nickLine.setObjectName(_fromUtf8("nickLine"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.nickLine)
        self.passLine = QtGui.QLineEdit(CreateChatDialog)
        self.passLine.setObjectName(_fromUtf8("passLine"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.passLine)
        self.subjectLine = QtGui.QLineEdit(CreateChatDialog)
        self.subjectLine.setObjectName(_fromUtf8("subjectLine"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.subjectLine)

        self.retranslateUi(CreateChatDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), CreateChatDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), CreateChatDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(CreateChatDialog)

    def retranslateUi(self, CreateChatDialog):
        CreateChatDialog.setWindowTitle(_translate("CreateChatDialog", "Create Chat", None))
        self.subjectLabel.setText(_translate("CreateChatDialog", "Subject:", None))
        self.nickLabel.setText(_translate("CreateChatDialog", "Nick:", None))
        self.passLabel.setText(_translate("CreateChatDialog", "Passphrase:", None))
        self.nickLine.setText(_translate("CreateChatDialog", "newbie1", None))

