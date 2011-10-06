# -*- coding: utf-8 -*-

import sys

import ui
import storage

class Controler(object):
    def __init__(self):
        self.init()

    def init(self):
        self._mainform = ui.MainForm(self)
        self._storage = storage.Storage()
        self._storage.load()

    def uninit(self):
        self._storage.save()

    def show(self):
        self._mainform.show()

    def search(self, cmd):
        return [item for item in self._storage.items if self.match(cmd, item.cmd)]

    def match(self, cmd, allcmd):
        if len(cmd) == 0:
            return True

        for subcmd in allcmd:
            start = 0
            for c in cmd:
                start = subcmd.find(c, start)
                if start == -1:
                    #Not match.
                    break
            else:
                #Match, next subcmd.
                return True

        return False

    def on_run(self):
        pass

    def on_cmd_edit_textchanged(self, text):
        self._mainform.showresult(self.search(text))

def main():
    app = ui.QtGui.QApplication(sys.argv)
    controler = Controler()
    controler.show()
    sys.exit(app.exec_())
