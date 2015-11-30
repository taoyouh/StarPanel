class Star:
    def __init__(self, mass, r):
        from Vector import Vector
        self.__mass = mass
        self.__pos = Vector(0, 0)
        self.__v = Vector(0, 0)
        self.__r = r
        self.__color = "black"

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

class StarCollection:
    def __init__(self):
        self.__stars = []

    def append(self, star):
        self.__stars.append(star);

    def getStars(self):
        return self.__stars

    def updateSpan(self, tSpan):
        if float(tSpan) < 0:
            raise ArithmeticError()
        while tSpan > 100:
            self.__update(100)
            tSpan -= 100
        self.__update(tSpan)

    def __update(self, t):
        g = 6.67E-11
        import Vector
        n = len(self.__stars)
        for i in range(n):
            for j in range(i + 1, n):
                star1 = self.__stars[i]
                star2 = self.__stars[i + 1]
                rVec = star2.getPos() - star1.getPos()
                force = g * star1.getMass() * star2.getMass() / (rVec.abs() ** 2) * rVec.unitVec()
                star1.setV(star1.getV() + t / star1.getMass() * force)
                star2.setV(star2.getV() - t / star2.getMass() * force)
                star1.setPos(star1.getPos() + t * star1.getV())
                star2.setPos(star2.getPos() + t * star2.getV())

    def calibrate(self):
        from Vector import Vector
        totalP = Vector(0, 0)
        totalMass = 0
        for star in self.__stars:
            totalP += star.getMass() * star.getV()
            totalMass += star.getMass()
        for star in self.__stars:
            star.setV(star.getV() - 1 / totalMass * totalP)
