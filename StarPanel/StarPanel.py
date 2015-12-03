import Star
import Tkinter
import Vector
starColl = Star.StarCollection()
star1 = Star.Star(5.96E24, 20000)
starColl.append(star1)

star2 = Star.Star(7.349E22, 20000)
star2.setPos(Vector.Vector(3.84E8, 0))
star2.setV(Vector.Vector(0, 1022.1547))
starColl.append(star2)

star3 = Star.Star(7E22, 20000)
star3.setPos(Vector.Vector(-5E8, 0))
star3.setV(Vector.Vector(0, -700))
starColl.append(star3)

star4 = Star.Star(1000, 2000)
star4.setPos(Vector.Vector(0, 5E7))
star4.setV(Vector.Vector(1000, 0))
starColl.append(star4)
starColl.calibrate()

tk = Tkinter.Tk()
c = Tkinter.Canvas(tk, width = 400, height = 400)
c.pack()

from Drawing import InitLayout
while 1:
    InitLayout(c, starColl.getStars(), 200, 200, 0.3E-6)
    tk.update()
    starColl.updateSpan(1000, 10)
raw_input()