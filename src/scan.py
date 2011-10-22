# -*- coding: utf-8 -*-

import os
import storage

scan_path_recurse = (
        r'$userprofile\AppData\Roaming\Microsoft\Windows\Start Menu',
        r'c:\ProgramData\Microsoft\Windows\Start Menu',
        r'$userprofile\desktop',
        r'd:\\',
        )
scan_path_nonrecurse = (
        r'$windir',
        r'$windir\system32',
        )

scan_ext = set([
        '.exe',
        '.lnk',
        '.bak',
        ])

stor = storage.Storage()

def unique(seq):
    return list(set(seq))

def isscaned(filename):
    return os.path.splitext(filename)[1].lower() in scan_ext

def scandir(path, recurse):
    filelist = []
    path = path.decode('utf-8')
    try:
        dl = os.listdir(path)
    except:
        dl = []
    for d in dl:
        fullpath = os.path.join(path, d)
        if os.path.isdir(fullpath):
            if recurse:
                filelist += scandir(fullpath.encode('utf-8'), recurse)
        elif os.path.isfile(fullpath):
            if isscaned(fullpath):
                filelist.append(fullpath.encode('utf-8'))
                print filelist[-1]
    return filelist

def addfile(filename):
    name = os.path.basename(filename)
    stor.add(name, filename)

def scan():
    filelist = []
    for path in scan_path_recurse:
        filelist += scandir(os.path.expandvars(path), True)
    for path in scan_path_nonrecurse:
        filelist += scandir(os.path.expandvars(path), False)
    filelist = unique(filelist)
    for i in filelist:
        addfile(i)

if __name__ == '__main__':
    scan()
