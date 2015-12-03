def starList() :
    print "You will be ordered to input some orders ."
    star_number = input("Please input the number you want<The first is fixed star>: ")
    n = 1
    starList = []
    while n <= star_number :
        seril = input("Please input the seril<1 - end>: ")
        star_mass = input("Please input the mass: ")
        star_radius = input("Please input the radius: ")
        starList = starList + [[seril,star_mass,star_radius]]
        n = n + 1
    return starList

list = []
can = None

def InitLayout(canvas, starList, originX, originY, scale) :
    import Vector
    import Star
    import Tkinter
    global list
    global can
    can = canvas
    for item in list:
        canvas.delete(item[0])
    list = []
    for star in starList:
        pos = star.getPos()
        r = max((star.getR(), 1 / scale))
        color = star.getColor()
        id = canvas.create_oval(originX + (pos.getX() - r) * scale, \
                                originY + (pos.getY() - r) * scale, \
                                originX + (pos.getX() + r) * scale, \
                                originY + (pos.getY() + r) * scale, fill=color)
        list.append((id, star ))
        



def UpdateLayout():
    import Tkinter
    import Vector
    import Star
    global list
    global can
    can = canvas
    for item in list:
        n = 0
        star = starList[n]
        pos = star.getPos()
        canvas.move(item[0],pos.getX,pos.getY)
        n = n + 1
