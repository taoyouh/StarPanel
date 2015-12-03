import threading
import time
import Star
import Tkinter
import Vector
from Drawing import InitLayout

def onUpdate():
    global starColl
    starColl.updateSpan(3000, 10)

def onDraw():
    InitLayout(c, starColl.getStars(), 400, 400, 0.6E-6)
    tk.update()

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
star1 = Star.Star(5.96E24, 6.73E6)
starColl.append(star1)

star2 = Star.Star(7.349E22, 1.73E6)
star2.setPos(Vector.Vector(3.84E8, 0))
star2.setV(Vector.Vector(0, 1022.1547))
starColl.append(star2)

star3 = Star.Star(7E18, 20000)
star3.setPos(Vector.Vector(-5E8, 0))
star3.setV(Vector.Vector(0, -700))
starColl.append(star3)

star4 = Star.Star(1000, 1)
star4.setPos(Vector.Vector(0, 2.5E7))
star4.setV(Vector.Vector(-5500, 0))
starColl.append(star4)

star5 = Star.Star(7.349E22, 1.73E6)
star5.setPos(Vector.Vector(0, 3.84E8))
star5.setV(Vector.Vector(-1022.1547, 0))
starColl.append(star5)

star6 = Star.Star(7.349E22, 1.73E6)
star6.setPos(Vector.Vector(0, -3.44E8))
star6.setV(Vector.Vector(1022.1547, 0))
starColl.append(star6)

#star7 = Star.Star(7.349E22, 20000)
#star7.setPos(Vector.Vector(3.04E8, 0))
#star7.setV(Vector.Vector(0, 1022.1547))
#starColl.append(star7)

starColl.calibrate()

tk = Tkinter.Tk()
c = Tkinter.Canvas(tk, width = 800, height = 800)
c.pack()

InitLayout(c, starColl.getStars(), 400, 400, 0.6E-6)
updateLoop = Loop(0, onUpdate)
updateLoop.start()
drawLoop = Loop(0.01, onDraw)
drawLoop.start()
raw_input()