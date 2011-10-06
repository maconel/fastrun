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

        QtCore.QObject.connect(self.ui.run_button, QtCore.SIGNAL("clicked()"), self._event_handler.on_run)
        QtCore.QObject.connect(self.ui.cmd_edit, QtCore.SIGNAL("textChanged(QString)"), self._event_handler.on_cmd_edit_textchanged)

    def getcmd(self):
        return unicode(self.ui.cmd_edit.text()).encode('utf-8')

    def showresult(self, itemlist):
        self._result_model.clear()
        for item in itemlist:
            standardItem = QtGui.QStandardItem(item.name.decode('utf-8'))
            standardItem.setEditable(False)
            self._result_model.appendRow(standardItem)

    def on_cmd_edit_textchanged(self, text):
        self._event_handler.on_cmd_edit_textchanged(unicode(text).encode('utf-8'))
