# -*- coding: utf-8 -*-
from __future__ import with_statement
import os
import sys

import pinyinlib

#name  |path                  |cmd0  :cmd1    :cmd2
#记事本|c:\windows\notepad.exe|记事本:notepad.ex:jishibene
class Item(object):
    def __init__(self, name, path, cmd):
        self.name = name
        self.path = path
        self.cmd = cmd

    def __repr__(self):
        return ('name=%s|path=%s|cmd=%s' % (self.name, self.path, ':'.join(self.cmd))).decode('utf-8').encode(sys.getfilesystemencoding())

class Storage(object):
    def __init__(self):
        self.items = []

    def load(self):
        with file(os.path.join(curfilepath(), '..\data\data.txt'), 'rt') as f:
            for line in f:
                fields = line.rstrip('\r\n').split('|')
                if len(fields) != 3:
                    continue
                self.items.append(Item(fields[0], fields[1], fields[2].split(':')))

    def add(self, name, path):
        pinyinlist = pinyinlib.wordlist_to_pinyin(name)
        item = Item(name, path, ':'.join((name, os.path.basename(path), ':'.join(pinyinlist))))

        self.items.append(item)
        with file(os.path.join(curfilepath(), '..\data\data.txt'), 'at') as f:
            f.write('\n')
            f.write('|'.join((item.name, item.path, item.cmd)))

def curfilepath():
    return os.path.dirname(os.path.abspath(os.path.join(os.getcwd(), __file__)))
