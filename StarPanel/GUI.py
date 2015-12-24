import time
import Star
from Tkinter import *
from tkMessageBox import *
import Vector

class GUI:
    def __init__(self, starPanel):
        self.__starPanel = starPanel

        self.root = Tk()
        Label(self.root,text = "Welcome to star management system",bg = "yellow").grid(row = 0,column = 0)
        self.b1 = Button(self.root,text = "add star",command = self.Top1)
        self.b2 = Button(self.root,text = "delete star",command = self.Top2)
        self.b3 = Button(self.root,text = "display star",command = self.Top3)
        self.b5 = Button(self.root,text = "viewAngle",command = self.Top4)
        self.b1.grid(row = 1,column = 0)
        self.b2.grid(row = 2,column = 0)
        self.b3.grid(row = 3,column = 0)
        self.b5.grid(row = 4,column = 0)
        Label(self.root,text = "accelerate").grid(row = 1,column = 1)
        Label(self.root,text = "slow").grid(row = 2,column = 1)
        Label(self.root,text = "magnify").grid(row = 3,column = 1)
        Label(self.root,text = "shrinking").grid(row = 4,column = 1)
        self.A1 = Button(self.root,text = "+",command = self.accelearate)
        self.A2 = Button(self.root,text = "-",command = self.slow)
        self.A3 = Button(self.root,text = "+",command = self.magnify)
        self.A4 = Button(self.root,text = "-",command = self.shrinking)
        self.A1.grid(row = 1,column = 2)
        self.A2.grid(row = 2,column = 2)
        self.A3.grid(row = 3,column = 2)
        self.A4.grid(row = 4,column = 2)

        self.c1 = Canvas(self.root, width = 800, height = 800, bg = "black")
        self.c1.grid(row = 6, column = 0)

        starPanel.setCanvas(self.c1)
        starPanel.startGraphic()

        self.root.protocol("WM_DELETE_WINDOW", self.__onDestroy)

        self.root.mainloop()

    def __onDestroy(self):
        self.__starPanel.stopGraphic()
        self.__starPanel.stopUpdate()
        self.root.destroy()

    def accelearate(self):
        self.__starPanel.accelerate()

    def slow(self):
        self.__starPanel.deccelerate()

    def magnify(self):
        self.__starPanel.zoomIn()

    def shrinking(self):
        self.__starPanel.zoomOut()

    def Top1(self):
        self.top1 = Toplevel()
        self.top1.geometry("200x200")
        self.top1.title("AddStar")
        Label(self.top1,text = "name",bg = "yellow").grid(row = 0,column = 0)
        Label(self.top1,text = "mass",bg = "yellow").grid(row = 1,column = 0)
        Label(self.top1,text = "position",bg = "yellow").grid(row = 2,column = 0)
        Label(self.top1,text = "velocity",bg = "yellow").grid(row = 3,column = 0)
        Label(self.top1,text = "radium",bg = "yellow").grid(row = 4,column = 0)
        Label(self.top1,text = "color",bg = "yellow").grid(row = 5,column = 0)
        self.top1_v_n = StringVar()
        self.top1_v_m = StringVar()
        self.top1_v_p = StringVar()
        self.top1_v_v = StringVar()
        self.top1_v_r = StringVar()
        self.top1_v_c = StringVar()
        Entry(self.top1,textvariable = self.top1_v_n).grid(row = 0,column = 1)
        Entry(self.top1,textvariable = self.top1_v_m).grid(row = 1,column = 1)
        Entry(self.top1,textvariable = self.top1_v_p).grid(row = 2,column = 1)
        Entry(self.top1,textvariable = self.top1_v_v).grid(row = 3,column = 1)
        Entry(self.top1,textvariable = self.top1_v_r).grid(row = 4,column = 1)
        Entry(self.top1,textvariable = self.top1_v_c).grid(row = 5,column = 1)
        Button(self.top1,text = "Set",command = self.creatStar).grid(row = 6,column = 1,sticky = W+E)

    def Top2(self):
        self.top2 = Toplevel()
        self.top2.title("DeleteStar")
        Label(self.top2,text = "Enter the number of star you want to delete").pack()
        self.top2_name = StringVar()
        Entry(self.top2,textvariable = self.top2_name).pack()
        Button(self.top2,text = "delete",command = self.deleteYourStar).pack()


    def Top3(self):
        self.top3 = Toplevel()
        self.top3.title("DisplayStar")
        self.top3.geometry("600x600")
        b4 = Button(self.top3,text = "showYourStar",command = self.showYourStar)
        b4.pack()
        self.e1 = Text(self.top3)
        self.e1.pack()

    def creatStar(self):
        try:
            mass = eval(self.top1_v_m.get())
            r = eval(self.top1_v_r.get())
            self.star1 = Star.Star(mass,r)
            self.star1.setColor(self.top1_v_c.get())
            list_p = self.top1_v_p.get().split(",")
            list_v = self.top1_v_v.get().split(",")
            x_p = eval(list_p[0])
            y_p = eval(list_p[1])
            x_v = eval(list_v[0])
            y_v = eval(list_v[1])
            self.star1.setPos(Vector.Vector(x_p,y_p))
            self.star1.setV(Vector.Vector(x_v,y_v))
            starColl = self.__starPanel.getStarColl()
            starColl.append(self.star1)
            self.__starPanel.startGraphic()
            self.clear()
            showinfo("Success","A star has been created")

        except:
            showwarning("Error","enter failed")
            self.clear()

    def showYourStar(self):
         s = self.__starPanel.getStarColl().getStars()
         i = 0
         line = 1.0
         while i < len(s):
             self.e1.insert(line, str(s[i]) +"\n")
             i = i + 1
             line = line + 1

    def clear_top1(self):
         self.top1_v_c.set("")
         self.top1_v_m.set("")
         self.top1_v_r.set("") 
         self.top1_v_n.set("")
         self.top1_v_v.set("")
         self.top1_v_p.set("")

    def clear_top2(self):
         self.top2_name.set("")

    def deleteYourStar(self):
        try:
            s = self.__starPanel.getStarColl().getStars()
            n = eval(self.top2_name.get())
            self.__starPanel.stopUpdate()
            self.__starPanel.stopGraphic()
            del s[n]
            self.__starPanel.startGraphic()
        except:
            showwarning("Error","enter failed")
            self.clear_top2()

    def Top4(self):
        top4 = Toplevel()
        top4.title("changeView")
        self.top4_view = StringVar()
        Label(top4,text = "choose the order of star you want to chase").grid(row = 0,column = 0)
        Entry(top4,textvariable = self.top4_view).grid(row = 0,column = 1)
        Button(top4,text = "Go", command = self.Top4_changeView).grid(row = 1,column = 0,sticky = W+E)

    def Top4_changeView(self):
        self.__starPanel.follow(eval(self.top4_view.get()))
        
