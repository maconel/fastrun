# -*- coding: utf-8 -*-
import sys

from PyQt4 import QtGui
from PyQt4 import QtCore

from ui_main import Ui_mainForm

class MainForm(QtGui.QWidget):
    def __init__(self, event_handler):
        super(MainForm, self).__init__(None)
        self.ui = Ui_mainForm()
        self.ui.setupUi(self)
        self._event_handler = event_handler

        QtCore.QObject.connect(self.ui.run_button, QtCore.SIGNAL("clicked()"), self._event_handler.on_run)
