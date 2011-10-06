# -*- coding: utf-8 -*-

import sys
import os

import ui
import storage

class Controler(object):
    def __init__(self):
        self.init()

    def init(self):
        self._mainform = ui.MainForm(self)
        self._storage = storage.Storage()
        self._storage.load()
        self.on_search('')

    def uninit(self):
        self._storage.save()

    def showmainform(self):
        self._mainform.show()

    def search(self, cmd):
        return [item for item in self._storage.items if self.match(cmd, item.cmd)]

    def match(self, cmd, allcmd):
        if len(cmd) == 0:
            return True

        for subcmd in allcmd:
            start = -1
            for c in cmd:
                start = subcmd.find(c, start + 1)
                if start == -1:
                    #Not match.
                    break
            else:
                #Match, next subcmd.
                return True

        return False

    def run(self, item):
        #os.spawnv(os.P_NOWAIT, item.path, ())
        os.system('start /B %s' % item.path)

    def on_run(self, item):
        self.run(item)

    def on_search(self, text):
        self._mainform.showresult(self.search(text))

def main():
    app = ui.QtGui.QApplication(sys.argv)
    controler = Controler()
    controler.showmainform()
    sys.exit(app.exec_())
