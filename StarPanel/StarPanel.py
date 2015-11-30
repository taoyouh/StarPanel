import Vector
v1 = Vector.Vector(1,2)
v2 = Vector.Vector(2,3)
print v1 + v2
print v1 - v2
print 3 * v2
import Star
starPanel = Star.StarCollection()
star1 = Star.Star(5.965E24, 1)
star2 = Star.Star(7.349E22, 1)
star2.setPos(Vector.Vector(3.84E8, 0))
star2.setV(Vector.Vector(0, 1022.1547595867230318733181660255))
starPanel.append(star1)
starPanel.append(star2)
starPanel.calibrate()
while 1:
    starPanel.updateSpan(86400)
    print star1.getPos().abs(),
    print star2.getPos().abs(),
    print (star2.getPos() - star1.getPos()).abs(),
    raw_input()
