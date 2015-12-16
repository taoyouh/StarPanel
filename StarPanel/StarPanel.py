import threading
import time
import Star
from Tkinter import *
import Vector

updateSpan = 100
scale = 7E-11

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

class StarPanel:
    def __init__(self):
        import Drawing
        self.__starColl = Star.StarCollection()
        self.__updateSpan = 1000
        self.__scale = 7E-11
        self.__canvas = None
        self.__updateLoop = Loop(0, self.__onUpdate)
        self.__drawLoop = Loop(0.16, self.__onDraw)
        self.__drawing = Drawing.Drawing()


    def setCanvas(self, canvas):
        if not isinstance(canvas, Canvas):
            raise TypeError("The \"canvas\" should be a canvas. ")
        self.__canvas = canvas


    def startGraphic(self):
        self.__updateLoop.stop()
        self.__drawLoop.stop()

        self.__drawing.InitLayout(self.__canvas, self.__starColl.getStars(), 400, 400, self.__scale)
        self.__updateLoop = Loop(0, self.__onUpdate)
        self.__drawLoop = Loop(0.16, self.__onDraw)
        self.__updateLoop.start()
        self.__drawLoop.start()

    def getStarColl(self):
        return self.__starColl

    def __onUpdate(self):
        self.__starColl.updateSpan(self.__updateSpan, self.__updateSpan)

    def __onDraw(self):
        self.__drawing.updateLayout()

    def zoomIn(self):
        self.__scale *= 2
        self.__drawing.InitLayout(self.__canvas, self.__starColl.getStars(), 400, 400, self.__scale)

    def zoomOut(self):
        self.__scale *= 0.5
        InitLayout(self.__canvas, self.__starColl.getStars(), 400, 400, self.__scale)

    def accelerate(self):
        self.__updateSpan *= 2

    def deccelerate(self):
        self.__updateSpan *= 0.5

class Loop(threading.Thread):
    def __init__(self, interval, action):
        self.__interval = interval
        self.__action = action
        self.__running = True
        self.__lock = threading.Lock()
        threading.Thread.__init__(self)

    def run(self):
        self.__lock.acquire()
        while self.__running:
            self.__action()
            time.sleep(self.__interval)
        self.__lock.release()

    def stop(self):
        self.__running = False
        self.__lock.acquire()

starPanel = StarPanel()
starColl = starPanel.getStarColl()

sun = Star.Star(1.9891E30, 6.96E8)
sun.setColor("red")
starColl.append(sun)

mercury = Star.Star(3.3022E23, 2.44E6)
mercury.setPos(Vector.Vector(4.60E10, 0))
mercury.setV(Vector.Vector(0, 5.479E4))
mercury.setColor("blue")
starColl.append(mercury)

venus = Star.Star(4.8676E24, 6.052E6)
venus.setPos(Vector.Vector(1.07477E11, 0))
venus.setV(Vector.Vector(0, 3.527E4))
venus.setColor("orange")
starColl.append(venus)

earth = Star.Star(5.9742E24, 6.372797E6)
earth.setPos(Vector.Vector(1.47098074E11, 0))
earth.setV(Vector.Vector(0, 3.0296E4))
earth.setColor("navy")
starColl.append(earth)

moon = Star.Star(7.3477E22, 1.737E6)
moon.setPos(Vector.Vector(1.47461178E11, 0))
moon.setV(Vector.Vector(0, 3.1373E4))
moon.setColor("gray")
starColl.append(moon)

mars = Star.Star(6.4185E24, 3.389E6)
mars.setPos(Vector.Vector(2.0662E11, 0))
mars.setV(Vector.Vector(0, 2.651E4))
mars.setColor("darkred")
starColl.append(mars)

jupiter = Star.Star(1.8986E27, 6.9911E7)
jupiter.setPos(Vector.Vector(7.405736E11, 0))
jupiter.setV(Vector.Vector(0, 1.371E4))
jupiter.setColor("brown")
starColl.append(jupiter)

uranus = Star.Star(8.6810E25, 2.5559E7)
uranus.setPos(Vector.Vector(2.748938461E12, 0))
uranus.setV(Vector.Vector(0, 7.103E3))
uranus.setColor("lightblue")
starColl.append(uranus)

neptune = Star.Star(1.0243E26, 2.4767E7)
neptune.setPos(-Vector.Vector(4.452940833E12, 0))
neptune.setV(-Vector.Vector(0, 5.49154E3))
neptune.setColor("blue")
starColl.append(neptune)

pluto = Star.Star(1.305E22, 1.186E6)
pluto.setPos(Vector.Vector(4.437E12, 0))
pluto.setV(Vector.Vector(0, 6.103E3))
pluto.setColor("blue")
starColl.append(pluto)

starColl.calibrate()

gui = GUI(starPanel)
raw_input()