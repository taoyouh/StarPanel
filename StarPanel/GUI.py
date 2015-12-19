import time
import Star
from Tkinter import *
import Vector

class GUI:
    def __init__(self, starPanel):
        self.__starPanel = starPanel

        self.root = Tk()
        Label(self.root,text = "Welcome to star management system",bg = "yellow").grid(row = 0,column = 0)
        self.b1 = Button(self.root,text = "add star")
        self.b2 = Button(self.root,text = "delete star")
        self.b3 = Button(self.root,text = "display star")
        self.b1.grid(row = 1,column = 0)
        self.b2.grid(row = 2,column = 0)
        self.b3.grid(row = 3,column = 0)
        Label(self.root,text = "accelerate").grid(row = 1,column = 1)
        Label(self.root,text = "slow").grid(row = 2,column = 1)
        Label(self.root,text = "magnify").grid(row = 3,column = 1)
        Label(self.root,text = "shrinking").grid(row = 4,column = 1)
        self.A1 = Button(self.root,text = "+",command = self.accelearate)
        self.A2 = Button(self.root,text = "-",command = self.slow)
        self.A3 = Button(self.root,text = "+",command = self.magnify)
        self.A4 = Button(self.root,text = "-",command = self.shrinking)
        self.A1.grid(row = 1,column = 2)
        self.A2.grid(row = 2,column = 2)
        self.A3.grid(row = 3,column = 2)
        self.A4.grid(row = 4,column = 2)
        self.v1 = StringVar()
        self.E1 = Entry(self.root,textvariable = self.v1)
        self.E1.grid(row = 4,column = 0)

        self.c1 = Canvas(self.root, width = 800, height = 800, bg = "black")
        self.c1.grid(row = 6, column = 0)

        starPanel.setCanvas(self.c1)
        starPanel.startGraphic()

        self.root.mainloop()

    def accelearate(self):
        self.__starPanel.accelerate()

    def slow(self):
        self.__starPanel.deccelerate()

    def magnify(self):
        self.__starPanel.zoomIn()

    def shrinking(self):
        self.__starPanel.zoomOut()