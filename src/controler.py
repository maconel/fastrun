# -*- coding: utf-8 -*-

import sys

import ui

class Controler:
    def __init__(self):
        self.mainform = ui.MainForm(self)

    def on_run(self):
        print self.mainform.ui.cmd_edit.text()
        self.mainform.ui.cmd_edit.setFocus()
        self.mainform.ui.cmd_edit.selectAll()

def main():
    app = ui.QtGui.QApplication(sys.argv)
    controler = Controler()
    controler.mainform.show()
    sys.exit(app.exec_())
