#!/usr/bin/env python

#@author : Anatole Moureaux
#@date : (V1.0) : August 2019

#Plot is Python-based GUI that can be used to quickly plot data (V1.0)
#(V1.0) The user can type 2 vectors (x and y) to plot them on the screen as red dots. 
#       Then the user can add more specific features on the graph, like axis labels, title, specific length for the x-axis etc.
#       The user can also add approximations and interpolation of several degrees
#Next features : handel more plots on the same graph
#                add automated/user-friendly legend generation 
#                add a comprehensive handling of explicit function of x


############################## modules ##############################
import numpy as np #array manipulation

import matplotlib #plot on Tkinter window integration
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

from tkinter import * #window 

import scipy.stats as stats #approximations and interpolations
from scipy.interpolate import CubicSpline as spline



############################## window initialization ##############################
def windowInit():
    
    fen = Tk()
    
    version = 1.0
    fen.title("Plot ("+version+")")

    #set the window on full screen on opening
    class FullScreenApp(object):
        def __init__(self, master, **kwargs):
            self.master=master
            pad=3
            self._geom='200x200+0+0'
            master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
            master.bind('<Escape>',self.toggle_geom)
        def toggle_geom(self,event):
            geom=self.master.winfo_geometry()
            print(geom,self._geom)
            self.master.geometry(self._geom)
            self._geom=geom
    app=FullScreenApp(fen)

    #some colors definition
    myColor1 = '#78f8ff'
    myColor2 = '#78cbff'
    myColor3 = '#75a1ff'
    myColor4 = '#7575ff'
    myColor5 = '#445CFF'

    #definition of the widgets
    frame0=Frame(fen)
    frame0.pack()
    
    title = Label(frame0,text="Plot")
    title.configure(font=('Courrier',30),bg=myColor1)
    title.pack(side=TOP,fill=X)

    greatbarre1=Label(frame0,text="                                                                                                                                                                                                                                                                                                                                                 ")
    greatbarre1.configure(bg=myColor2,font=('Courrier',20))
    greatbarre1.pack(side=TOP,fill=X)
    
    greatbarre2=Label(frame0,text="")
    greatbarre2.configure(bg=myColor3,font=('Courrier',10))
    greatbarre2.pack(side=TOP,fill=X)

    greatbarre3=Label(frame0,text="")
    greatbarre3.configure(bg=myColor4,font=('Courrier',5))
    greatbarre3.pack(side=TOP,fill=X)

    greatbarre4=Label(frame0,text="")
    greatbarre4.configure(bg=myColor5,font=('Courrier',2))
    greatbarre4.pack(side=TOP,fill=X)

    frame1=Frame(fen,bg="white")
    frame1.pack(side=LEFT,fill=BOTH,expand=1)

    frame1.grid_columnconfigure(0,weight=1)
    frame1.grid_columnconfigure(1,weight=1)

    frame1.grid_rowconfigure(0,pad=0)
    frame1.grid_rowconfigure(1,pad=0)
    frame1.grid_rowconfigure(2,pad=0)
    frame1.grid_rowconfigure(3,pad=0)
    frame1.grid_rowconfigure(4,pad=0)
    frame1.grid_rowconfigure(5,pad=0)
    frame1.grid_rowconfigure(6,pad=0)
    frame1.grid_rowconfigure(7,pad=0)
    frame1.grid_rowconfigure(8,pad=20)
    frame1.grid_rowconfigure(9,pad=0)
    frame1.grid_rowconfigure(10,pad=0)
    frame1.grid_rowconfigure(11,pad=20)
    frame1.grid_rowconfigure(12,pad=0)
    frame1.grid_rowconfigure(13,pad=0)
    frame1.grid_rowconfigure(14,pad=0)
    frame1.grid_rowconfigure(15,pad=20)
    frame1.grid_rowconfigure(16,pad=20)
    frame1.grid_rowconfigure(17,pad=20)
    frame1.grid_rowconfigure(18,pad=20)

    funConsigne = Label(frame1,text="Écrivez ici les données à afficher : ")
    funConsigne.configure(font=('Courrier',15),bg = myColor1)
    funConsigne.grid(row=0,column = 0,columnspan=2,sticky=EW)

    moreConsigne1 = Label(frame1,text="Les deux vecteurs doivent être de la même taille.",
            font = "Courrier 10 italic",
            bg = "white")
    moreConsigne1.grid(row=1,column = 0,columnspan=1,sticky=W)

    moreConsigne2 = Label(frame1,text="Le vecteur des abscisses doit être dans l'ordre croissant.",
            font = "Courrier 10 italic",
            bg= "white")
    moreConsigne2.grid(row=2,column = 0,columnspan=1,sticky=W)

    exemple = Label(frame1,text="EXEMPLE : 0.5;2.0;1.97;3.03",
            font = "Courrier 10 bold",
            bg = "white")
    exemple.grid(row=3,column = 0,columnspan=1,sticky=W)
   
    abslabel = Label(frame1,text="Abscisses : ")
    abslabel.configure(font=('Courrier',15),bg="white")
    abslabel.grid(row=4,column=0,columnspan=1,sticky=E)

    absexpr = Entry(frame1)
    absexpr.grid(row=4,column=1,columnspan=1,sticky=EW)

    ordlabel = Label(frame1,text="Ordonnées : ")
    ordlabel.configure(font=('Courrier',15),bg="white")
    ordlabel.grid(row=5,column=0,columnspan=1,sticky=E)

    ordexpr = Entry(frame1)
    ordexpr.grid(row=5,column=1,columnspan=1,sticky=EW)

    error1 = Label(frame1,text="Il semblerait que vous ayez entré un caractère non pris en charge.",
            font="Courrier 9 bold italic",
            bg="white",
            fg="white")
    error1.grid(row=6,column=0,columnspan=2,sticky=W)
    
    error2 = Label(frame1,text="Seuls les chiffres, les '.' et les ';' sont autorisés",
            font="Courrier 9 bold italic",
            bg="white",
            fg="white")
    error2.grid(row=7,column=0,columnspan=2,sticky=W)

    absconsigne = Label(frame1,text="Entrez les abscisses minimale et maximale : ")
    absconsigne.configure(font=('Courrier',15),bg=myColor2)
    absconsigne.grid(row=8,column=0,columnspan=2,sticky=EW)
    
    absminlabel = Label(frame1,text="abscisse minimale : ")
    absminlabel.configure(font=('Courrier',15),bg="white")
    absminlabel.grid(row=9,column=0,columnspan=1,sticky=E)

    absminexpr = Entry(frame1)
    absminexpr.grid(row=9,column=1,columnspan=1,sticky=W)

    absmaxlabel = Label(frame1,text="abscisse maximale : ")
    absmaxlabel.configure(font=('Courrier',15),bg="white")
    absmaxlabel.grid(row=10,column=0,columnspan=1,sticky=E)

    absmaxexpr = Entry(frame1)
    absmaxexpr.grid(row=10,column=1,columnspan=1,sticky=W)

    optconsigne = Label(frame1,text="Options supplémentaires : ")
    optconsigne.configure(font=('Courrier',15),bg=myColor3)
    optconsigne.grid(row=11,column=0,columnspan=2,sticky=EW)
    
    titlelabel = Label(frame1,text=("Titre : "))
    titlelabel.configure(font=('Courrier',15),bg="white")
    titlelabel.grid(row=12,column=0,columnspan=1,sticky=E)

    titleexpr = Entry(frame1)
    titleexpr.grid(row=12,column=1,columnspan=1,sticky=W)

    xlabel = Label(frame1,text=("Nom de l'axe x : "))
    xlabel.configure(font=('Courrier',15),bg="white")
    xlabel.grid(row=13,column=0,columnspan=1,sticky=E)

    xlabelexpr = Entry(frame1)
    xlabelexpr.grid(row=13,column=1,columnspan=1,sticky=W)

    ylabel = Label(frame1,text=("Nom de l'axe y : "))
    ylabel.configure(font=('Courrier',15),bg="white")
    ylabel.grid(row=14,column=0,columnspan=1,sticky=E)

    ylabelexpr = Entry(frame1)
    ylabelexpr.grid(row=14,column=1,columnspan=1,sticky=W)
    
    approxlabel = Label(frame1,text="Ajouter une approximation (degré) : ",
            font="Courrier 15",
            fg="black",
            bg="white")
    approxlabel.grid(row=15,column=0,columnspan=1,sticky=E)
    
    approxvariable = StringVar(frame1)
    approxvariable.set("/")
    approxmenu = OptionMenu(frame1,approxvariable,"/","0","1","2","3","4","5","6","7","8","9","10")
    approxmenu.config(font=('courrier',(10)),bg='white')
    approxmenu.grid(row=15,column=1,columnspan=1,sticky=W)
    
    interplabel = Label(frame1,text="Ajouter une interpolation : ",
            font="Courrier 15",
            fg="black",
            bg="white")
    interplabel.grid(row=16,column=0,columnspan=1,sticky=E)
    
    interpvariable = StringVar(frame1)
    interpvariable.set("aucune")
    interpmenu = OptionMenu(frame1,interpvariable,"aucune","linéaire par morceaux","splines cubiques", "degré n")
    interpmenu.config(font=('courrier',(10)),bg='white')
    interpmenu.grid(row=16,column=1,columnspan=1,sticky=W)

    var = IntVar()
    gridcheckbutton = Checkbutton(frame1,text="Afficher la grille",highlightthickness=0,bd=0,variable=var)

    gridcheckbutton.configure(font=('Courrier',15),bg="white")
    gridcheckbutton.grid(row=17,column=0,columnspan=2,sticky=EW)
   
    frame2=Frame(fen,bg="white")
    frame2.pack(fill=BOTH,expand=1)

    fig = Figure(figsize=(15,8))
    a = fig.add_subplot(111)


    #adding of the plot on the window
    canvas = FigureCanvasTkAgg(fig,frame2)
    canvas.draw()
    canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)

    #adding of the toolbar beneath the plot
    toolbar = NavigationToolbar2Tk(canvas, frame2)
    toolbar.update()
    canvas._tkcanvas.pack(side=TOP)
    

############################## user's vector expression translation to numpy array ##############################
    def vector(string):
        error1.configure(fg="white")
        error2.configure(fg="white")
        count = 0
        for i in range(0,len(string)):
            if(string[i] != ';') and (string[i].isdigit() == False) and (string[i] != '.'):
                error1.configure(fg="red")
                error2.configure(fg="red")
            if(string[i] == ';'):
                count=count+1
        x=np.zeros(count+1)
        current=0
        startindex=0
        count2=0
        for i in range(0,len(string)):
            if(string[i] == ';'):
                x[current]=float(string[startindex:i])
                current=current+1
                startindex=i+1
                count2=count2+1
                if count2==count:
                    x[current]=float(string[i+1:])
        return x


############################## get to know if the vector is sorted ##############################
    def isSorted(x):
        return np.all(x[:-1]<x[1:])


############################## plotting function ##############################
    def plotting():
        a.clear()
        canvas.draw()
        if(absexpr.get() != "") and (ordexpr.get() != ""):
            x = vector(absexpr.get())
            y = vector(ordexpr.get())
            if len(x) != len(y) or isSorted(x)== False :
                if len(x) != len(y) :
                    moreConsigne1.configure(font="Courrier 10 italic bold",fg="red")
                if isSorted(x) == False : 
                    moreConsigne2.configure(font="Courrier 10 italic bold",fg="red")
            if len(x) == len(y) or isSorted(x) == True :
                if len(x) == len(y) :
                    moreConsigne1.configure(font="Courrier 10 italic",fg="black")
                if isSorted(x) == True :
                    moreConsigne2.configure(font="Courrier 10 italic",fg="black")
            if len(x) == len(y) and isSorted(x) == True:
                moreConsigne1.configure(font="Courrier 10 italic",fg="black")
                moreConsigne2.configure(font="Courrier 10 italic",fg="black")
                error1.configure(fg="white")
                error2.configure(fg="white")
                a.plot(x,y,'or')
                a.set_title(titleexpr.get())
                a.set_ylabel(ylabelexpr.get())
                a.set_xlabel(xlabelexpr.get())
                if (absminexpr.get() != "") and (absmaxexpr.get() != "") : 
                    a.set_xlim([float(absminexpr.get()),float(absmaxexpr.get())])
                if var.get() == 1 :
                    a.grid()
                elif var.get()==0 : 
                    a.grid(False)
                canvas.draw()
                if(approxvariable.get()!="/"):
                    deg = int(approxvariable.get())
                    xabs=np.linspace(x[0],x[-1],1000)
                    z = np.polyfit(x, y, deg)
                    a.plot(xabs,np.polyval(z,xabs),'b--')
                    canvas.draw()
                if(interpvariable.get()!="aucune"):
                    if(interpvariable.get()=="linéaire par morceaux"):
                        a.plot(x,y,'b--')
                        canvas.draw()
                    if(interpvariable.get()=="splines cubiques"):
                        xabs=np.linspace(x[0],x[-1],1000)
                        u = spline(x,y)(xabs)
                        a.plot(xabs,u,'b--')
                        canvas.draw()
                    if(interpvariable.get()=="degré n"):
                        xabs=np.linspace(x[0],x[-1],1000)
                        u = np.polyfit(x,y,len(x)-1)
                        a.plot(xabs,np.polyval(u,xabs),'--b')
                        canvas.draw()

    plot=Button(frame1,text="Plot !",command=plotting)
    plot.configure(font=('Courrier',15),bg = myColor4)
    plot.grid(row=18,column=0,columnspan=1,sticky=EW)

############################## clearing function ##############################
    def clearall():
        absexpr.delete(0,'end')
        ordexpr.delete(0,'end')
        absminexpr.delete(0,'end')
        absmaxexpr.delete(0,'end')
        titleexpr.delete(0,'end')
        xlabelexpr.delete(0,'end')
        ylabelexpr.delete(0,'end')
        error1.configure(fg="white")
        error2.configure(fg="white")
        moreConsigne1.configure(font="Courrier 10 italic",fg="black")
        moreConsigne2.configure(font="Courrier 10 italic",fg="black")
        approxvariable.set("/")
        interpvariable.set("aucune")
        a.clear()
        canvas.draw()

    clearall=Button(frame1,text="Effacer tout",command=clearall)
    clearall.configure(font=('Courrier',15),bg=myColor4)
    clearall.grid(row=18,column=1,columnspan=1,sticky=EW)

    return fen

############################################################
def main():
    windowInit().mainloop()

main()
