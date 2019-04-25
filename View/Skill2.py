from tkinter import *
import tkinter.messagebox
from View.ToolTip import *
from Model.PC import *

class Skill2():
    def __init__(self, master, fr, player):
        self.root = master
        self.fr = fr
        self.ui = Frame(self.root, )
        # self.ui.pack(fill=BOTH, expand=True)

        self.player = player

        self.zhiye = StringVar()
        self.zhiye.set(self.player.zhiye)
        zhiyelabel = Label(self.ui, textvariable=self.zhiye, width=100, height=2)
        zhiyelabel.pack()

        jump_back = Button(self.ui, text="back",  command = lambda: self.jumpback(self.fr))
        jump_back.pack()

    def raise_up(self):
        self.zhiye.set(self.player.zhiye)
        self.ui.pack(fill=BOTH, expand=True)

    def jumpback(self, controller):
        self.ui.pack_forget()
        self.fr.pack(fill=BOTH, expand=True)