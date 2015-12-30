# -*- coding: utf-8 -*-
import Star
from Tkinter import *
from tkMessageBox import *
import Vector

''' 将GUI界面封装成类'''

class GUI:
    def __init__(self, starPanel):
        self.__starPanel = starPanel#引入天体运行模块

        self.root = Tk()
        Label(self.root,text = " Welcome to star management system ",bg = "yellow").grid(row = 0,column = 0,rowspan = 2,columnspan = 3,sticky = N+S+W+E)
        self.b1 = Button(self.root,text = "add star",bg = "orange",command = self.Top1)#按钮“add star”与顶层窗口top1相连
        self.b2 = Button(self.root,text = "delete star",bg = "orange",command = self.Top2)#按钮“delete star”与顶层窗口top2相连
        self.b3 = Button(self.root,text = "display star",bg = "orange",command = self.Top3)#按钮“deletestar”与顶层窗口top3相连
        self.b5 = Button(self.root,text = "viewAngle",bg = "orange",command = self.Top4)#按钮“viewangle"与顶层窗口top4相连
        self.b6 = Button(self.root,text = "Lazy?Make a solar system!",bg = "orange",command = self.create_solarSystem)#创建太阳系的按钮
        self.b1.grid(row = 3,column = 0,sticky = N+S+W+E)#顺序布置按钮
        self.b2.grid(row = 4,column = 0,sticky = N+S+W+E)
        self.b3.grid(row = 5,column = 0,sticky = N+S+W+E)
        self.b5.grid(row = 6,column = 0,sticky = N+S+W+E)
        self.b6.grid(row = 2,column = 1,sticky = N+S)
        self.A1 = Button(self.root,text = "accelerate +",bg = "orange",command = self.accelearate)#加速、减速、放大、缩小提示文本
        self.A2 = Button(self.root,text = "slow -",bg = "orange",command = self.slow)
        self.A3 = Button(self.root,text = "magnify +",bg = "orange",command = self.magnify)#加速、减速、放大、缩小按钮
        self.A4 = Button(self.root,text = "shrinking -",bg = "orange",command = self.shrinking)
        self.A1.grid(row = 3,column = 2,sticky = N+S+W+E)#布置以上按钮
        self.A2.grid(row = 4,column = 2,sticky = N+S+W+E)
        self.A3.grid(row = 5,column = 2,sticky = N+S+W+E)
        self.A4.grid(row = 6,column = 2,sticky = N+S+W+E)

        self.c1 = Canvas(self.root, width = 800, height = 800, bg = "black")#引入画布
        self.c1.grid(row = 3, column = 1,rowspan = 4)#布置画布

        starPanel.setCanvas(self.c1)#将画布引入天体运行模块
        starPanel.startGraphic()#开启图形绘制线程

        self.root.protocol("WM_DELETE_WINDOW", self.__onDestroy)#按下X时停止图形绘制线程

        self.root.mainloop()

    
    def __onDestroy(self):
        '''控制主窗口关闭'''
        self.__starPanel.stopGraphic()
        self.__starPanel.stopUpdate()
        self.root.destroy()

    def accelearate(self):
        '''从天体运行模块中引入加速函数'''
        self.__starPanel.accelerate()

    def slow(self):
        '''从天体运行模块中引入减速函数'''
        self.__starPanel.deccelerate()

    def magnify(self):
        '''从天体运行模块中引入缩小函数'''
        self.__starPanel.zoomIn()

    def shrinking(self):
        '''从天体运行模块中引入放大函数'''
        self.__starPanel.zoomOut()

    def Top1(self):
        '''顶层窗口top1用于创建行星'''
        self.top1 = Toplevel()#创建顶层窗口top1
        self.top1.geometry("350x350")#创建顶层窗口top1
        self.top1.title("AddStar")
        Label(self.top1,text = "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ").grid(row = 0,column = 0,columnspan = 3,sticky = W+S)
        Label(self.top1,text = "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ").grid(row = 2,column = 0,columnspan = 3,sticky = W+S)
        Label(self.top1,text = "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ").grid(row = 4,column = 0,columnspan = 3,sticky = W+S)
        Label(self.top1,text = "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ").grid(row = 6,column = 0,columnspan = 3,sticky = W+S)
        Label(self.top1,text = "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ").grid(row = 8,column = 0,columnspan = 3,sticky = W+S)
        Label(self.top1,text = "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ").grid(row = 10,column = 0,columnspan = 3,sticky = W+S)
        Label(self.top1,text = "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ").grid(row = 12,column = 0,columnspan = 3,sticky = W+S)
        Label(self.top1,text = "          *  ").grid(row = 1,column = 0,sticky = N+S+W+E)
        Label(self.top1,text = "          *  ").grid(row = 3,column = 0,sticky = N+S+W+E)
        Label(self.top1,text = "          *  ").grid(row = 5,column = 0,sticky = N+S+W+E)
        Label(self.top1,text = "          *  ").grid(row = 7,column = 0,sticky = N+S+W+E)
        Label(self.top1,text = "          *  ").grid(row = 9,column = 0,sticky = N+S+W+E)
        Label(self.top1,text = "          *  ").grid(row = 11,column = 0,sticky = N+S+W+E)
        Label(self.top1,text = "name",bg = "yellow").grid(row = 1,column = 1,sticky = N+S+W+E)#质量、速度、位置、半径、颜色等提示标签
        Label(self.top1,text = "mass",bg = "yellow").grid(row = 3,column = 1,sticky = N+S+W+E)
        Label(self.top1,text = "position",bg = "yellow").grid(row = 5,column = 1,sticky = N+S+W+E)
        Label(self.top1,text = "velocity",bg = "yellow").grid(row = 7,column = 1,sticky = N+S+W+E)
        Label(self.top1,text = "radium",bg = "yellow").grid(row = 9,column = 1,sticky = N+S+W+E)
        Label(self.top1,text = "color",bg = "yellow").grid(row = 11,column = 1,sticky = N+S+W+E)
        self.top1_v_n = StringVar()#监测名字输入的变量
        self.top1_v_m = StringVar()#监测质量输入的变量
        self.top1_v_p = StringVar()#监测位置输入的变量
        self.top1_v_v = StringVar()#监测速度输入的变量
        self.top1_v_r = StringVar()#监测半径输入的变量
        self.top1_v_c = StringVar()#监测颜色输入的变量
        Entry(self.top1,textvariable = self.top1_v_n).grid(row = 1,column = 2)#布置输入框
        Entry(self.top1,textvariable = self.top1_v_m).grid(row = 3,column = 2)
        Entry(self.top1,textvariable = self.top1_v_p).grid(row = 5,column = 2)
        Entry(self.top1,textvariable = self.top1_v_v).grid(row = 7,column = 2)
        Entry(self.top1,textvariable = self.top1_v_r).grid(row = 9,column = 2)
        Entry(self.top1,textvariable = self.top1_v_c).grid(row = 11,column = 2)
        Button(self.top1,text = "Set",command = self.creatStar).grid(row = 13,column = 2,sticky = W+E+N+S)

    def Top2(self):
        '''顶层窗口top2用于删除行星'''
        self.top2 = Toplevel()
        self.top2.title("DeleteStar")
        Label(self.top2,text = "- - - - - - - - - - - - - - - - - - - - - -").pack()
        Label(self.top2,text = "Enter the number of star you want to delete").pack()
        Label(self.top2,text = "- - - - - - - - - - - - - - - - - - - - - -").pack()
        self.top2_name = StringVar()#用于监测删除行星序号的变量
        Entry(self.top2,textvariable = self.top2_name).pack()#输入删除行星序号的输入框
        Label(self.top2,text = "- - - - - - - - - - - - - - - - - - - - - -").pack()
        Button(self.top2,text = "delete",command = self.deleteYourStar).pack()#与删除行星函数关联的按钮


    def Top3(self):
        '''顶层窗口top3用于显示现有行星列表'''
        self.top3 = Toplevel()
        self.top3.title("DisplayStar")
        Label(self.top3,text = "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -").grid(row = 0,column = 0,sticky = N+S+W+E)
        b4 = Button(self.top3,text = "showYourStar",command = self.showYourStar)
        b4.grid(row = 1,column = 0,sticky = N+S)
        Label(self.top3,text = "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -").grid(row = 2,column = 0,sticky = N+S+W+E)
        self.e1 = Text(self.top3)#用于显示行星的文本框
        self.e1.grid()

    def creatStar(self):
        '''创建行星的函数'''
        try:
            mass = eval(self.top1_v_m.get())#获得系列参数
            r = eval(self.top1_v_r.get())
            list_p = self.top1_v_p.get().split(",")
            list_v = self.top1_v_v.get().split(",")
            x_p = eval(list_p[0])
            y_p = eval(list_p[1])
            x_v = eval(list_v[0])
            y_v = eval(list_v[1])
            self.star1 = Star.Star(mass,r)#创建新的star对象并设置参数
            self.star1.setColor(self.top1_v_c.get())
            self.star1.setPos(Vector.Vector(x_p,y_p))
            self.star1.setV(Vector.Vector(x_v,y_v))
            starColl = self.__starPanel.getStarColl()#将新的star对象添加进starColl列表中
            starColl.append(self.star1)
            self.__starPanel.startGraphic()#重新开始绘制线程
            self.clear_top1()
            showinfo("Success","A star has been created")#显示行星已经被创建的信息

        except:
            showwarning("Error","enter failed")#错误输入时弹出窗口报错
            self.clear_top1()#清空输入框中的信息以便重新输入

    def showYourStar(self):
         '''显示行星列表函数'''
         s = self.__starPanel.getStarColl().getStars()
         i = 0
         line = 1.0
         while i < len(s):
             self.e1.insert(line, str(s[i]) +"\n")
             i = i + 1
             line = line + 1

    def clear_top1(self):
         '''清空输入框以便下一次输入的函数'''
         self.top1_v_c.set("")
         self.top1_v_m.set("")
         self.top1_v_r.set("") 
         self.top1_v_n.set("")
         self.top1_v_v.set("")
         self.top1_v_p.set("")

    def clear_top2(self):
         '''同上'''
         self.top2_name.set("")

    def deleteYourStar(self):
        '''删除行星的函数'''
        try:
            s = self.__starPanel.getStarColl().getStars()
            n = eval(self.top2_name.get())
            if n <= len(s):
                self.__starPanel.stopUpdate()#停止控制计算的线程以便删除行星
                self.__starPanel.stopGraphic()#停止控制绘制的线程以便删除行星
                del s[n]
                self.__starPanel.startGraphic()#重开绘制线程
                self.top2_name.set("")
            else:
                showwarning("Error","out of range")
                self.top2_name.set("")
        except:
            showwarning("Error","enter failed")
            self.clear_top2()

    def Top4(self):
        '''转换视角的顶层窗口'''
        top4 = Toplevel()
        top4.title("changeView")
        self.top4_view = StringVar()#监测转换视角的目标行星序号的变量
        Label(top4,text = "- - - - - - - - - - - - - - - - - - - - - -").grid(row = 0 ,column = 0)
        Label(top4,text = "choose the order of star you want to chase").grid(row = 1,column = 0)
        Entry(top4,textvariable = self.top4_view).grid(row = 2,column = 0)#输入行星序号的输入框
        Label(top4,text = "- - - - - - - - - - - - - - - - - - - - - -").grid(row = 3 ,column = 0)
        Button(top4,text = "Go", command = self.Top4_changeView).grid(row = 4,column = 0,sticky = W+E)

    def Top4_changeView(self):
        '''用于转换视角的函数'''
        try:
            c = eval(self.top4_view.get()) - 1
            if (c+1) <= len(self.__starPanel.getStarColl().getStars()):
                self.__starPanel.follow(c)
                self.top4_view.set("")
            else:
                showwarning("Error","out of range")
        except:
            showwarning("Error","enter error")
            self.top4_view.set("")

    def create_solarSystem(self):
        '''用于创建太阳系的函数'''
        import StarPanel
        if len(self.__starPanel.getStarColl().getStars()) == 0:
            StarPanel.makeASolarSystem(self.__starPanel)#可以直接在画布上创建一个太阳系噢！！
            self.__starPanel.startGraphic()#重新开启绘制线程
        else:
            showwarning("Error","there are stars in your canvas")
