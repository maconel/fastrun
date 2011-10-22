# -*- coding: utf-8 -*-
from __future__ import with_statement
import os
import sys

import pinyinlib

datafilepath = r'..\data\data.txt'

#name  |path                  |cmd0  :cmd1      :cmd2     |priority
#记事本|c:\windows\notepad.exe|记事本:notepad.ex:jishibene|18
class Item(object):
    def __init__(self, name, path, cmd, priority):
        self.name = name
        self.path = path
        self.cmd = cmd
        self.priority = priority

class Storage(object):
    def __init__(self):
        self.items = []

    def load(self):
        self.items = []
        with file(os.path.join(curfilepath(), datafilepath), 'rt') as f:
            lineno = 0
            for line in f:
                fields = line.rstrip('\r\n').split('|')
                if len(fields) != 4:
                    continue
                self.items.append(Item(fields[0], fields[1], fields[2].lower().split(':'), int(fields[3])))
                lineno += 1

    def raise_priority(self, item):
        item.priority += 1
        self.items.sort(key=lambda(item):item.priority, reverse=True)
        with file(os.path.join(curfilepath(), datafilepath), 'wt') as f:
            for item in self.items:
                f.write(self.item_to_str(item))
                f.write('\n')

    def item_to_str(self, item):
        return '|'.join((item.name, item.path, ':'.join(item.cmd), '%04d' % item.priority))

    def add(self, name, path):
        pinyinlist = pinyinlib.wordlist_to_pinyin(name)
        item = Item(name, path, ':'.join((name, os.path.basename(path), ':'.join(pinyinlist))), 0)

        self.items.append(item)
        with file(os.path.join(curfilepath(), datafilepath), 'at') as f:
            f.write(self.item_to_str(item))
            f.write('\n')

def curfilepath():
    return os.path.dirname(os.path.abspath(os.path.join(os.getcwd(), __file__)))
