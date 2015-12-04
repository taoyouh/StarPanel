import threading
import time
import Star
import Tkinter
import Vector
from Drawing import InitLayout

updateSpan = 100
scale = 7E-11

def onUpdate():
    global starColl
    global updateSpan
    starColl.updateSpan(updateSpan, updateSpan)

def onDraw():
    global c
    global starColl
    global scale
    global tk
    InitLayout(c, starColl.getStars(), 400, 400, scale)
    tk.update()

def canvas_clicked(event):
    global scale
    scale *= 10

def canvas_rightClicked(event):
    global scale
    scale *= 0.1

def canvas_doubleClicked(event):
    global updateSpan
    updateSpan *= 10

def canvas_tripleClicked(event):
    global updateSpan
    updateSpan *= 0.1

class Loop(threading.Thread):
    def __init__(self, interval, action):
        self.__interval = interval
        self.__action = action
        threading.Thread.__init__(self)

    def run(self):
        while 1:
            self.__action()
            time.sleep(self.__interval)

starColl = Star.StarCollection()
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

tk = Tkinter.Tk()
c = Tkinter.Canvas(tk, width = 800, height = 800)
c.pack()

InitLayout(c, starColl.getStars(), 400, 400, 1E-10)
c.bind("<Button-1>", canvas_clicked)
c.bind("<Button-3>", canvas_rightClicked)
c.bind("<Double-Button-1>", canvas_doubleClicked)
c.bind("<Triple-Button-1>", canvas_tripleClicked)
updateLoop = Loop(0, onUpdate)
updateLoop.start()
drawLoop = Loop(0.01, onDraw)
drawLoop.start()
raw_input()