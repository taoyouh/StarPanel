class Vector:
    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def abs(self):
        return (self.__x ** 2 + self.__y ** 2) ** 0.5

    def unitVec(self):
        abs = self.abs()
        if abs == 0:
            return Vector(0, 0)
        else:
            return Vector(self.getX() / abs, self.getY() / abs)

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("A vector can only be added with another vector. ")
        return Vector(self.__x + other.getX(), self.__y + other.getY())

    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("A vector can only be substracted by another vector. ")
        return Vector(self.__x - other.getX(), self.__y - other.getY())

    def __rmul__(self, other):
        return Vector(self.getX() * other, self.getY() * other)

    def __repr__(self):
        return "Vector(" + str(self.__x) + " , " + str(self.__y) + ")"

