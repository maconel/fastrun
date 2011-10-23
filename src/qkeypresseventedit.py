# -*- coding: utf-8 -*-
import sys
import os

from PyQt4 import QtGui
from PyQt4 import QtCore

class QKeyPressEventEdit(QtGui.QLineEdit):
    def __init__(self, parent):
        super(QKeyPressEventEdit, self).__init__(parent)

    def keyPressEvent(self, keyEvent):
        super(QKeyPressEventEdit, self).keyPressEvent(keyEvent)
        self.emit(QtCore.SIGNAL('keyPressEvent(QKeyEvent)'), keyEvent)
