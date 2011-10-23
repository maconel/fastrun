# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/add.ui'
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

class Ui_addForm(object):
    def setupUi(self, addForm):
        addForm.setObjectName(_fromUtf8("addForm"))
        addForm.resize(321, 115)
        addForm.setWindowTitle(QtGui.QApplication.translate("addForm", "Add", None, QtGui.QApplication.UnicodeUTF8))
        addForm.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.formLayout = QtGui.QFormLayout(addForm)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.name_label = QtGui.QLabel(addForm)
        self.name_label.setText(QtGui.QApplication.translate("addForm", "Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.name_label.setObjectName(_fromUtf8("name_label"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.name_label)
        self.name_edit = QtGui.QLineEdit(addForm)
        self.name_edit.setObjectName(_fromUtf8("name_edit"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.name_edit)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.ok_button = QtGui.QPushButton(addForm)
        self.ok_button.setText(QtGui.QApplication.translate("addForm", "&Ok", None, QtGui.QApplication.UnicodeUTF8))
        self.ok_button.setAutoDefault(True)
        self.ok_button.setDefault(True)
        self.ok_button.setObjectName(_fromUtf8("ok_button"))
        self.horizontalLayout.addWidget(self.ok_button)
        self.cancel_button = QtGui.QPushButton(addForm)
        self.cancel_button.setText(QtGui.QApplication.translate("addForm", "&Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel_button.setObjectName(_fromUtf8("cancel_button"))
        self.horizontalLayout.addWidget(self.cancel_button)
        self.formLayout.setLayout(5, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.path_edit = QtGui.QLineEdit(addForm)
        self.path_edit.setObjectName(_fromUtf8("path_edit"))
        self.horizontalLayout_2.addWidget(self.path_edit)
        self.browse_button = QtGui.QToolButton(addForm)
        self.browse_button.setText(QtGui.QApplication.translate("addForm", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.browse_button.setObjectName(_fromUtf8("browse_button"))
        self.horizontalLayout_2.addWidget(self.browse_button)
        self.formLayout.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.path_label = QtGui.QLabel(addForm)
        self.path_label.setText(QtGui.QApplication.translate("addForm", "Path:", None, QtGui.QApplication.UnicodeUTF8))
        self.path_label.setObjectName(_fromUtf8("path_label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.path_label)

        self.retranslateUi(addForm)
        QtCore.QObject.connect(self.cancel_button, QtCore.SIGNAL(_fromUtf8("clicked()")), addForm.close)
        QtCore.QMetaObject.connectSlotsByName(addForm)
        addForm.setTabOrder(self.path_edit, self.browse_button)
        addForm.setTabOrder(self.browse_button, self.name_edit)
        addForm.setTabOrder(self.name_edit, self.ok_button)
        addForm.setTabOrder(self.ok_button, self.cancel_button)

    def retranslateUi(self, addForm):
        pass

