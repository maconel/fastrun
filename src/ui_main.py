# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main.ui'
#
# Created: Sun Oct 23 17:38:03 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_mainForm(object):
    def setupUi(self, mainForm):
        mainForm.setObjectName(_fromUtf8("mainForm"))
        mainForm.resize(400, 300)
        mainForm.setWindowTitle(QtGui.QApplication.translate("mainForm", "fastrun", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(mainForm)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.cmd_edit = QKeyPressEventEdit(mainForm)
        self.cmd_edit.setAcceptDrops(False)
        self.cmd_edit.setFrame(True)
        self.cmd_edit.setObjectName(_fromUtf8("cmd_edit"))
        self.horizontalLayout.addWidget(self.cmd_edit)
        self.run_button = QtGui.QPushButton(mainForm)
        self.run_button.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.run_button.sizePolicy().hasHeightForWidth())
        self.run_button.setSizePolicy(sizePolicy)
        self.run_button.setMinimumSize(QtCore.QSize(0, 0))
        self.run_button.setBaseSize(QtCore.QSize(0, 0))
        self.run_button.setText(QtGui.QApplication.translate("mainForm", "run", None, QtGui.QApplication.UnicodeUTF8))
        self.run_button.setIconSize(QtCore.QSize(16, 16))
        self.run_button.setAutoDefault(False)
        self.run_button.setDefault(False)
        self.run_button.setObjectName(_fromUtf8("run_button"))
        self.horizontalLayout.addWidget(self.run_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.result_listview = QtGui.QListView(mainForm)
        self.result_listview.setObjectName(_fromUtf8("result_listview"))
        self.verticalLayout.addWidget(self.result_listview)

        self.retranslateUi(mainForm)
        QtCore.QMetaObject.connectSlotsByName(mainForm)
        mainForm.setTabOrder(self.cmd_edit, self.run_button)
        mainForm.setTabOrder(self.run_button, self.result_listview)

    def retranslateUi(self, mainForm):
        pass

from qkeypresseventedit import QKeyPressEventEdit
