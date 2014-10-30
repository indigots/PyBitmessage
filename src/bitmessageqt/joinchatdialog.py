# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'joinchatdialog.ui'
#
# Created: Tue Oct 28 23:02:57 2014
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

class Ui_JoinChatDialog(object):
    def setupUi(self, JoinChatDialog):
        JoinChatDialog.setObjectName(_fromUtf8("JoinChatDialog"))
        JoinChatDialog.resize(400, 147)
        JoinChatDialog.setModal(False)
        self.formLayout_2 = QtGui.QFormLayout(JoinChatDialog)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.joinWithLabel = QtGui.QLabel(JoinChatDialog)
        self.joinWithLabel.setObjectName(_fromUtf8("joinWithLabel"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.joinWithLabel)
        self.joinAddressCombo = QtGui.QComboBox(JoinChatDialog)
        self.joinAddressCombo.setObjectName(_fromUtf8("joinAddressCombo"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.joinAddressCombo)
        self.nickLabel = QtGui.QLabel(JoinChatDialog)
        self.nickLabel.setObjectName(_fromUtf8("nickLabel"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.nickLabel)
        self.nickLine = QtGui.QLineEdit(JoinChatDialog)
        self.nickLine.setObjectName(_fromUtf8("nickLine"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.nickLine)
        self.passLabel = QtGui.QLabel(JoinChatDialog)
        self.passLabel.setObjectName(_fromUtf8("passLabel"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.passLabel)
        self.passLine = QtGui.QLineEdit(JoinChatDialog)
        self.passLine.setObjectName(_fromUtf8("passLine"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.passLine)
        self.buttonBox = QtGui.QDialogButtonBox(JoinChatDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.buttonBox)

        self.retranslateUi(JoinChatDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), JoinChatDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), JoinChatDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(JoinChatDialog)

    def retranslateUi(self, JoinChatDialog):
        JoinChatDialog.setWindowTitle(_translate("JoinChatDialog", "Join Chat", None))
        self.joinWithLabel.setText(_translate("JoinChatDialog", "Address to Join with:", None))
        self.nickLabel.setText(_translate("JoinChatDialog", "Nick:", None))
        self.nickLine.setText(_translate("JoinChatDialog", "newbie1", None))
        self.passLabel.setText(_translate("JoinChatDialog", "Passphrase:", None))

