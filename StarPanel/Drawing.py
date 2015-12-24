#coding = utf-8class Drawing:    def __init__(self):        self.__canvasElementList = []        self.__canvas = None        self.__posList = []        self.__scale = None        self.__starList = []        self.__number = -1        self.__x0 = 400        self.__y0 = 400        import threading        self.__lock = threading.Lock()    def InitLayout(self, canvas, starList, originX, originY, scale, number) :        self.__lock.acquire()        import Vector        import Star        import Tkinter        self.__starList = starList        self.__canvas = canvas        self.__scale = scale        colorList = []        self.__number = number        if self.__number == -1 :            for item in self.__canvasElementList:                canvas.delete(item[0])            self.__canvasElementList = []            for star in starList:                pos = star.getPos()                x = pos.getX()                y = pos.getY()                self.__posList = self.__posList + [x,y]                r = max((star.getR(), 1 / scale))                color = star.getColor()                id = canvas.create_oval(originX + (pos.getX() - r) * scale, \                                      originY + (pos.getY() - r) * scale, \                                      originX + (pos.getX() + r) * scale, \                                      originY + (pos.getY() + r) * scale, \                                      width = 0, fill=color)                self.__canvasElementList.append((id, star ))        else :            for item in self.__canvasElementList:                canvas.delete(item[0])            self.__canvasElementList = []            for star in self.__starList :                pos = star.getPos()                x = pos.getX()                y = pos.getY()                self.__posList = self.__posList + [x,y]            x1 = self.__posList[self.__number*2]            y1 = self.__posList[self.__number*2 + 1]            for num in range(len(self.__starList)) :                self.__posList[num*2] = self.__posList[num*2] - x1 + 400                self.__posList[num*2 + 1] = self.__posList[num*2 + 1] - y1 + 400            for num1 in range(len(self.__starList)) :                star = self.__starList[num1]                color = star.getColor()                r = max((star.getR(),1 / scale))                id = canvas.create_oval(originX + (self.__posList[num1*2] - r) * scale, \                                           originY + (self.__posList[num1*2 + 1] - r) * scale, \                                           originX + (self.__posList[num1*2] + r) * scale, \                                           originY + (self.__posList[num1*2 + 1] + r) * scale,\                                           width = 0,fill = color)                self.__canvasElementList.append((id,star))        self.__lock.release()            def updateLayout(self):        self.__lock.acquire()        import Tkinter        import Vector        import Star        p = []        self.__x0 = 400        self.__y0 = 400        if self.__number == -1 :            for num in range(len(self.__canvasElementList)):                star = self.__starList[num]                pos = star.getPos()                x = self.__posList[2*num]                y = self.__posList[2*num + 1]                self.__canvas.move(self.__canvasElementList[num][0],(pos.getX() - x)*self.__scale,(pos.getY() - y)*self.__scale)                p = p + [pos.getX(),pos.getY()]        else:            xn = self.__posList[2*self.__number]             yn = self.__posList[2*self.__number + 1]             for num1 in range(len(self.__canvasElementList)) :                self.__posList[2*num1] = self.__posList[2*num1] - xn + self.__x0                self.__posList[2*num1 + 1] = self.__posList[2*num1 + 1] - yn + self.__y0                for num2 in range(len(self.__canvasElementList)) :                star = self.__starList[num2]                pos = star.getPos()                          p = p + [pos.getX(),pos.getY()]            xm = p[self.__number*2]             ym = p[self.__number*2 + 1]             for num3 in range(len(self.__canvasElementList)) :                p[2*num3] = p[num3*2] - xm + self.__x0                p[2*num3 + 1] = p[num3*2 + 1] - ym + self.__y0            for num4 in range(len(self.__canvasElementList)) :                x1 = p[num4*2]                y1 = p[num4*2 + 1]                x2 = self.__posList[num4*2]                y2 = self.__posList[num4*2 + 1]                self.__canvas.move(self.__canvasElementList[num4][0],(x1 - x2 )*self.__scale,( y1 - y2 )*self.__scale)        self.__posList = p          self.__lock.release()