# -*- coding: utf-8 -*-
import sys

from PyQt4 import QtGui
from PyQt4 import QtCore

from ui_main import Ui_mainForm
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
        QtCore.QObject.connect(self.ui.result_listview, QtCore.SIGNAL("doubleClicked(QModelIndex)"), self._on_cmd_edit_textchanged)

    def getcmd(self):
        return unicode(self.ui.cmd_edit.text()).encode('utf-8')

    def showresult(self, itemlist):
        self._result_model.clear()
        for item in itemlist:
            standardItem = QtGui.QStandardItem(item.name.decode('utf-8'))
            standardItem.setEditable(False)
            standardItem.setData(item)
            self._result_model.appendRow(standardItem)

    def _on_run_button_clicked(self):
        indexs = self.ui.result_listview.selectedIndexes()
        if len(indexs) == 0:
            #Not found.
            pass
        else:
            self._event_handler.on_run(self._result_model.itemFromIndex(indexs[0]).data().toPyObject())

        self.ui.cmd_edit.selectAll()
        self.ui.cmd_edit.setFocus()

    def _on_cmd_edit_textchanged(self, text):
        self._event_handler.on_search(unicode(text).encode('utf-8'))

    def _on_cmd_edit_textchanged(self, index):
        self._event_handler.on_run(self._result_model.itemFromIndex(index).data().toPyObject())

        self.ui.cmd_edit.selectAll()
        self.ui.cmd_edit.setFocus()
