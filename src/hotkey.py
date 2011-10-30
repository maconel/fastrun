# -*- coding: utf-8 -*-

from ctypes import *
from ctypes.wintypes import *
import threading
import time

WM_HOTKEY = 0x0312
MOD_NONE = 0x0000
MOD_ALT = 0x0001
MOD_CONTROL = 0x0002
MOD_SHIFT = 0x0004
MOD_WIN = 0x0008

_keeprun = False

#{hotkeyid: callback, ...}
hotkey_callback_map = {}

#[{'modifiers':modifiers, 'vk':vk, 'callback':callback), ...]
register_queue = []

#[{'callback':callback}, ...]
unregister_queue = []

# Define the Windows DLLs, constants and types that we need.
user32 = windll.user32

class MSG(Structure):
    _fields_ = [('hwnd', c_int),
    ('message', c_uint),
    ('wParam', c_int),
    ('lParam', c_int),
    ('time', c_int),
    ('pt', POINT)]

def register(modifiers, vk, callback):
    global _keeprun
    register_queue.append({'modifiers':modifiers, 'vk':vk, 'callback':callback})
    if not _keeprun:
        _keeprun = True
        _start()

def unregister(callback):
    unregister_queue.append({'callback':callback})

def _start():
    threading.Thread(target=_run).start()

def _run():
    global _keeprun

    msg = MSG()
    while _keeprun:
        for register in register_queue:
            hotkeyid = 1 if len(hotkey_callback_map) == 0 else hotkey_callback_map.keys()[-1] + 1
            if user32.RegisterHotKey(None, hotkeyid, register['modifiers'], register['vk']):
                hotkey_callback_map[hotkeyid] = register['callback']

        for unregister in unregister_queue:
            for i in hotkey_callback_map:
                if hotkey_callback_map[i] == unregister['callback']:
                    hotkey_callback_map.pop(i)
                    break

        if len(hotkey_callback_map) == 0:
            _keeprun = False
            return

        if user32.PeekMessageW(byref(msg), None, 0, 0, True):
            if msg.message == WM_HOTKEY:
                hotkey_callback_map[msg.wParam]()
            windll.user32.PostQuitMessage(0)
            user32.TranslateMessage(byref(msg))

        time.sleep(0.05)

if __name__ == '__main__':
    import os
    def onhotkey():
        if 'q' == raw_input(':'):
            unregister(onhotkey)

    register(MOD_NONE, 0xC0, onhotkey)
    while True:
        time.sleep(1)
        print '_keeprun=%s len(hotkey_callback_map)=%d' % ('True' if _keeprun else 'False', len(hotkey_callback_map))
