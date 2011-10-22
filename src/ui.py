# -*- coding: utf-8 -*-
import sys
import os

from PyQt4 import QtGui
from PyQt4 import QtCore

from ui_main import Ui_mainForm
from ui_add import Ui_addForm
import storage

class MainForm(QtGui.QWidget):
    def __init__(self, event_handler):
        super(MainForm, self).__init__(None)
        self.ui = Ui_mainForm()
        self.ui.setupUi(self)
        self._event_handler = event_handler
        self._result_model = QtGui.QStandardItemModel()

        self.ui.result_listview.setModel(self._result_model)

        QtCore.QObject.connect(self.ui.run_button, QtCore.SIGNAL("clicked()"), self._on_run_button_clicked)
        QtCore.QObject.connect(self.ui.cmd_edit, QtCore.SIGNAL("textChanged(QString)"), self._on_cmd_edit_textchanged)
        QtCore.QObject.connect(self.ui.result_listview, QtCore.SIGNAL("doubleClicked(QModelIndex)"), self._on_result_listview_doubleclicked)

    def getcmd(self):
        return unicode(self.ui.cmd_edit.text()).encode('utf-8')

    def showresult(self, itemlist):
        self._result_model.clear()
        for item in itemlist:
            standardItem = QtGui.QStandardItem(item.name.decode('utf-8'))
            standardItem.setEditable(False)
            standardItem.setData(item)
            self._result_model.appendRow(standardItem)
        if len(itemlist) > 0:
            self.ui.result_listview.selectionModel().select(self._result_model.index(0, 0), QtGui.QItemSelectionModel.Select)

    def getselectitems(self):
        return [self._result_model.itemFromIndex(i).data().toPyObject()
                for i in self.ui.result_listview.selectedIndexes()]

    def getallitems(self):
        return [self._result_model.itemFromIndex(self._result_model.index(i, 0)).data().toPyObject()
                for i in xrange(0, self._result_model.rowCount())]

    def messagebox_notfound(self):
        return QtGui.QMessageBox.Yes == QtGui.QMessageBox.question(self, u'提示', u'没找到，是否添加?', QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

    def _on_run_button_clicked(self):
        self._event_handler.on_run()

        self.ui.cmd_edit.selectAll()
        self.ui.cmd_edit.setFocus()

    def _on_cmd_edit_textchanged(self, text):
        self._event_handler.on_search(unicode(text).encode('utf-8'))

    def _on_result_listview_doubleclicked(self, index):
        self._event_handler.on_run_item(self._result_model.itemFromIndex(index).data().toPyObject())

        self.ui.cmd_edit.selectAll()
        self.ui.cmd_edit.setFocus()


class AddForm(QtGui.QWidget):
    def __init__(self, event_handler):
        super(AddForm, self).__init__(None)
        self.ui = Ui_addForm()
        self.ui.setupUi(self)
        self._event_handler = event_handler
        self._is_name_modified = False

        QtCore.QObject.connect(self.ui.ok_button, QtCore.SIGNAL("clicked()"), self._on_ok_button_clicked)
        QtCore.QObject.connect(self.ui.browse_button, QtCore.SIGNAL("clicked()"), self._on_browse_button_clicked)
        QtCore.QObject.connect(self.ui.name_edit, QtCore.SIGNAL("textChanged(QString)"), self._on_name_edit_textchanged)

    def show(self, name=''):
        self._is_name_modified = False if len(name)==0 else True
        self.ui.path_edit.clear()
        self.ui.name_edit.setText(name.decode('utf-8'))
        super(AddForm, self).show()

    def _on_ok_button_clicked(self):
        self._event_handler.on_add(unicode(self.ui.name_edit.text()).encode('utf-8'), unicode(self.ui.path_edit.text()).encode('utf-8'))
        self.close()

    def _on_browse_button_clicked(self):
        file_dialog = QtGui.QFileDialog()
        filepath = unicode(file_dialog.getOpenFileName())
        if len(filepath) != 0:
            filename = os.path.basename(filepath)
            self.ui.path_edit.setText(filepath)
            if not self._is_name_modified:
                self.ui.name_edit.setText(filename)

    def _on_name_edit_textchanged(self):
        self._is_name_modified = True
