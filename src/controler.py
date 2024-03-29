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
        self._addform = ui.AddForm(self)
        self._storage = storage.Storage()
        self._storage.load()
        self.on_search('')

    def uninit(self):
        self._storage.save()

    def showmainform(self):
        self._mainform.show()

    def search(self, cmd):
        return [item for item in self._storage.items if self.match(cmd.lower(), item.cmd)]

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
        print item.path
        #os.spawnv(os.P_NOWAIT, item.path, ())
        #os.system('start /B "%s"' % item.path)
        #os.system('cmd /c "%s"' % item.path)
        os.system('start /B cmd /c "%s"' % item.path)
        self._storage.raise_priority(item)

    def on_run(self):
        items = self._mainform.getselectitems()
        if len(items) > 0:
            self.run(items[0])
        else:
            if self._mainform.messagebox_notfound():
                self._addform.show(self._mainform.getcmd())

    def on_run_item(self, item):
        if item:
            self.run(item)

    def on_search(self, text):
        self._mainform.showresult(self.search(text))

    def on_add(self, name, path):
        self._storage.add(name, path)

def main():
    app = ui.QtGui.QApplication(sys.argv)
    controler = Controler()
    controler.showmainform()
    sys.exit(app.exec_())
