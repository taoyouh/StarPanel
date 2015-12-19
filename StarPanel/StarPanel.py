import threading
import time
import Star
from Tkinter import *
import Vector
from GUI import GUI

from datetime import datetime
from datetime import timedelta
class StarPanel:
    def __init__(self):
        import Drawing
        self.__starColl = Star.StarCollection()
        self.__updateSpan = 100000
        self.__scale = 7E-11
        self.__canvas = None
        self.__drawInterval = 0.016
        self.__updateInterval = 0.001
        self.__updateLoop = Loop(self.__updateInterval, self.__onUpdate)
        self.__drawLoop = Loop(self.__drawInterval, self.__onDraw)
        self.__drawing = Drawing.Drawing()
        self.__drawTime1 = datetime.now()
        self.__drawTime2 = datetime.now()
        self.__updateTime1 = datetime.now()
        self.__updateTime2 = datetime.now()


    def setCanvas(self, canvas):
        if not isinstance(canvas, Canvas):
            raise TypeError("The \"canvas\" should be a canvas. ")
        self.__canvas = canvas


    def startGraphic(self):
        self.__drawLoop.stop()
        self.__drawing.InitLayout(self.__canvas, self.__starColl.getStars(), 400, 400, self.__scale)
        self.__drawLoop = Loop(self.__drawInterval, self.__onDraw)
        self.__drawLoop.start()
        self.startUpdate()

    def stopGraphic(self):
        self.__drawLoop.stop()

    def startUpdate(self):
        self.__updateLoop.stop()
        self.__updateLoop = Loop(self.__updateInterval, self.__onUpdate)
        self.__updateLoop.start()
        
    def stopUpdate(self):
        self.__updateLoop.stop()

    def getStarColl(self):
        return self.__starColl

    def __onUpdate(self):
        self.__updateTime1 = self.__updateTime2
        self.__updateTime2 = datetime.now()
        self.__updateSpan = self.__starColl.updateSpan(self.__updateSpan)

    def getTimeScale(self):
        return self.__updateSpan / (self.__updateTime2 - self.__updateTime1).total_seconds()

    def __onDraw(self):
        self.__drawTime1 = self.__drawTime2
        self.__drawTime2 = datetime.now()
        self.__drawing.updateLayout()

    def getFPS(self):
        return int(1 / (self.__drawTime2 - self.__drawTime1).total_seconds())

    def zoomIn(self):
        self.__scale *= 2
        self.__drawing.InitLayout(self.__canvas, self.__starColl.getStars(), 400, 400, self.__scale)

    def zoomOut(self):
        self.__scale *= 0.5
        self.__drawing.InitLayout(self.__canvas, self.__starColl.getStars(), 400, 400, self.__scale)

    def accelerate(self):
        self.__updateInterval *= 0.5
        self.startUpdate()

    def deccelerate(self):
        self.__updateInterval *= 2
        self.startUpdate()

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

def makeASolarSystem(starPanel):
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