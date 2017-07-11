import Tkinter as tk
from collections import defaultdict
import threading

class App(object):

    def __init__(self):
        self.keys = defaultdict(bool)
        self.change = False
        self.root = tk.Tk()
        self.root.geometry('200x800')
        self.text = tk.Text(self.root, state='disabled', font='System 14 bold')
        self.text.pack(expand=True, fill='both')
        self.root.bind('<KeyPress>', self.onKeyPress)
        self.root.bind('<KeyRelease>', self.onKeyRelease)
        self.poll()
        self.root.mainloop()

    def onKeyPress(self, event):
        self.keys[event.char] = True
        self.change = True

    def onKeyRelease(self, event):
        self.keys[event.char] = False
        if event.char in ['w', 'e', 'f', ' ']:
            self.change = True

    def poll(self):
        self.root.after(1000/60, self.poll)
        if self.change:
            self.text.configure(state='normal')
            if self.string():
                self.text.insert('end', '%s\n' % self.string())
            self.text.configure(state='disabled')
            self.text.see(tk.END)
            self.change = False

        self.keys['n'] = False
        self.keys['h'] = False
        self.keys['u'] = False
        self.keys['i'] = False
        self.keys['k'] = False

    def string(self):
        x = 0
        y = 0
        if self.keys['f']:
            x += 1
        if self.keys['w']:
            x -= 1
        if self.keys[' ']:
            y -= 1
        if self.keys['e']:
            y += 1

        if x == -1 and y == -1:
            cmd = u'\u2196'
        if x == 0 and y == -1:
            cmd = u'\u2191'
        if x == 1 and y == -1:
            cmd = u'\u2197'
        if x == -1 and y == 0:
            cmd = u'\u2190'
        if x == 0 and y == 0:
            cmd = u''
        if x == 1 and y == 0:
            cmd = u'\u2192'
        if x == -1 and y == 1:
            cmd = u'\u2199'
        if x == 0 and y == 1:
            cmd = u'\u2193'
        if x == 1 and y == 1:
            cmd = u'\u2198'

        if self.keys['n']:
            cmd += 'P'
        if self.keys['h']:
            cmd += 'K'
        if self.keys['u']:
            cmd += 'S'
        if self.keys['i']:
            cmd += 'H'
        if self.keys['k']:
            cmd += 'D'

        return cmd

    def start(self):
        self.poll()
        self.root.mainloop()

app = App()
app.start()
