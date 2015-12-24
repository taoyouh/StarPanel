#coding = utf-8
import time
class Star:
    def __init__(self, mass, r):
        from Vector import Vector
        self.__mass = mass
        self.__pos = Vector(0, 0)
        self.__v = Vector(0, 0)
        self.__r = r
        self.__color = "black"
        self.__name = "star"

    def setName(self, value):
        if not isinstance(value, str):
            raise TypeError("Name should be string. ")
        self.__name = value

    def getName(self):
        return self.__name

    def getMass(self):
        return self.__mass

    def getPos(self):
        return self.__pos

    def setPos(self,pos):
        self.__pos = pos

    def getV(self):
        return self.__v

    def setV(self, v):
        self.__v = v

    def getR(self):
        return self.__r

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def __repr__(self):
        return ("%s(Mass = %s, Color = %s, Velocity = %s, Position = %s)" % \
                (self.getName(), str(self.getMass()), self.getColor(), str(self.getV()), str(self.getPos())))

class StarCollection:
    def __init__(self):
        self.__stars = []
        self.__interval = 0.0

    def append(self, star):
        self.__stars.append(star);

    def getStars(self):
        return self.__stars

    def updateSpan(self, tSpan):
        n = len(self.__stars)
        interval = tSpan
        for i in range(n):
            for j in range(i + 1, n):
                star1 = self.__stars[i]
                star2 = self.__stars[j]
                interval = min(interval, (star2.getPos() - star1.getPos()).abs() /(star2.getV() - star1.getV()).abs() / 10)
        if float(tSpan) < 0:
            raise ArithmeticError()
        if float(interval) < 0:
            raise ArithmeticError()
        while tSpan > interval:
            self.__update(interval)
            tSpan -= interval
        self.__update(tSpan)
        self.__interval = interval

    def __update(self, t):
        t = float(t)
        g = 6.67E-11
        import Vector
        n = len(self.__stars)
        for i in range(n):
            for j in range(i + 1, n):
                star1 = self.__stars[i]
                star2 = self.__stars[j]
                rVec = star2.getPos() - star1.getPos()
                force = g * star1.getMass() * star2.getMass() / (rVec.abs() ** 2) * rVec.unitVec()
                star1.setV(star1.getV() + t / star1.getMass() * force)
                star2.setV(star2.getV() - t / star2.getMass() * force)
        for star in self.__stars:
            star.setPos(star.getPos() + t * star.getV())

    def calibrate(self):
        '''
        在不改变天体间相对速度的情况下，使系统总动量为0。
        说人话就是不要让所有的天体往一边飘。
        '''
        from Vector import Vector
        totalP = Vector(0, 0)
        totalMass = 0
        for star in self.__stars:
            totalP += star.getMass() * star.getV()
            totalMass += star.getMass()
        for star in self.__stars:
            star.setV(star.getV() - 1 / totalMass * totalP)

    def getInterval(self):
        return self.__interval