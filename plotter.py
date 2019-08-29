#!/usr/bin/env python

#tentative d'écriture d'un programme de plotting de fonctions à une variable 1D opérationnel
#Anatole Moureaux, aout 2019


import numpy as np
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

from tkinter import *


#initialisation de la fenêtre et de ses composantes
def windowInit():
    
    fen = Tk()
    fen.title("Plot (v1.0)")

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

    myColor1 = '#78f8ff'
    myColor2 = '#78cbff'
    myColor3 = '#75a1ff'
    myColor4 = '#7575ff'
    myColor5 = '#445CFF'

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
    frame1.grid_columnconfigure(2,weight=1)
    frame1.grid_columnconfigure(3,weight=1)

    frame1.grid_rowconfigure(0,pad=0)
    frame1.grid_rowconfigure(1,pad=0)
    frame1.grid_rowconfigure(2,pad=0)
    frame1.grid_rowconfigure(3,pad=0)
    frame1.grid_rowconfigure(4,pad=0)
    frame1.grid_rowconfigure(5,pad=20)
    frame1.grid_rowconfigure(6,pad=20)
    frame1.grid_rowconfigure(7,pad=20)
    frame1.grid_rowconfigure(8,pad=20)
    frame1.grid_rowconfigure(9,pad=20)
    frame1.grid_rowconfigure(10,pad=20)
    frame1.grid_rowconfigure(11,pad=20)
    frame1.grid_rowconfigure(12,pad=20)
    frame1.grid_rowconfigure(13,pad=20)
    frame1.grid_rowconfigure(14,pad=20)
    
    funConsigne = Label(frame1,text="Écrivez ici les données à afficher : ")
    funConsigne.configure(font=('Courrier',15),bg = myColor1)
    funConsigne.grid(row=0,column = 0,columnspan=4,sticky=EW)

    moreConsigne1 = Label(frame1,text="Les deux vecteurs doivent être de la même taille.",
            font = "Courrier 10 italic",
            bg = "white")
    moreConsigne1.grid(row=1,column = 0,columnspan=4,sticky=W)

    moreConsigne2 = Label(frame1,text="Le vecteur des abscisses doit être dans l'ordre croissant.",
            font = "Courrier 10 italic",
            bg= "white")
    moreConsigne2.grid(row=2,column = 0,columnspan=4,sticky=W)

    exemple = Label(frame1,text="EXEMPLE : 0.5;2.0;1.97;3.03",
            font = "Courrier 10 bold",
            bg = "white")
    exemple.grid(row=3,column = 0,columnspan=4,sticky=W)
   
    abslabel = Label(frame1,text="Abscisses : ")
    abslabel.configure(font=('Courrier',15),bg="white")
    abslabel.grid(row=4,column=1,columnspan=1,sticky=E)

    absexpr = Entry(frame1)
    absexpr.grid(row=4,column=2,columnspan=1,sticky=W)

    ordlabel = Label(frame1,text="Ordonnées : ")
    ordlabel.configure(font=('Courrier',15),bg="white")
    ordlabel.grid(row=5,column=1,columnspan=1,sticky=E)

    ordexpr = Entry(frame1)
    ordexpr.grid(row=5,column=2,columnspan=1,sticky=W)

    absconsigne = Label(frame1,text="Entrez les abscisses minimale et maximale : ")
    absconsigne.configure(font=('Courrier',15),bg=myColor2)
    absconsigne.grid(row=6,column=0,columnspan=4,sticky=EW)
    
    absminlabel = Label(frame1,text="abscisse minimale : ")
    absminlabel.configure(font=('Courrier',15),bg="white")
    absminlabel.grid(row=7,column=1,columnspan=1,sticky=E)

    absminexpr = Entry(frame1)
    absminexpr.grid(row=7,column=2,columnspan=1,sticky=W)

    absmaxlabel = Label(frame1,text="abscisse maximale : ")
    absmaxlabel.configure(font=('Courrier',15),bg="white")
    absmaxlabel.grid(row=8,column=1,columnspan=1,sticky=E)

    absmaxexpr = Entry(frame1)
    absmaxexpr.grid(row=8,column=2,columnspan=1,sticky=W)

    optconsigne = Label(frame1,text="Options supplémentaires : ")
    optconsigne.configure(font=('Courrier',15),bg=myColor3)
    optconsigne.grid(row=9,column=0,columnspan=4,sticky=EW)
    
    titlelabel = Label(frame1,text=("Titre : "))
    titlelabel.configure(font=('Courrier',15),bg="white")
    titlelabel.grid(row=10,column=1,columnspan=1,sticky=E)

    titleexpr = Entry(frame1)
    titleexpr.grid(row=10,column=2,columnspan=1,sticky=W)

    xlabel = Label(frame1,text=("Nom de l'axe x : "))
    xlabel.configure(font=('Courrier',15),bg="white")
    xlabel.grid(row=11,column=1,columnspan=1,sticky=E)

    xlabelexpr = Entry(frame1)
    xlabelexpr.grid(row=11,column=2,columnspan=1,sticky=W)

    ylabel = Label(frame1,text=("Nom de l'axe y : "))
    ylabel.configure(font=('Courrier',15),bg="white")
    ylabel.grid(row=12,column=1,columnspan=1,sticky=E)

    ylabelexpr = Entry(frame1)
    ylabelexpr.grid(row=12,column=2,columnspan=1,sticky=W)
    
    var = IntVar()
    gridcheckbutton = Checkbutton(frame1,text="Afficher la grille",highlightthickness=0,bd=0,variable=var)
    gridcheckbutton.configure(font=('Courrier',15),bg="white")
    gridcheckbutton.grid(row=13,column=1,columnspan=2,sticky=EW)
   
    frame2=Frame(fen,bg="white")
    frame2.pack(fill=BOTH,expand=1)

    fig = Figure(figsize=(15,8))
    a = fig.add_subplot(111)

    canvas = FigureCanvasTkAgg(fig,frame2)
    canvas.draw()
    canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)

    toolbar = NavigationToolbar2Tk(canvas, frame2)
    toolbar.update()
    canvas._tkcanvas.pack(side=TOP)
    
    def plotting():
        #TODO
        #temporairement
        #le but serait d'appeler une fonction externe avec l'ensemble des paramètres pour alléger le code
        a.plot([1,2,3,4,5,6],[5,3,6,7,2,1])
        a.set_title(titleexpr.get())
        a.set_ylabel(ylabelexpr.get())
        a.set_xlabel(xlabelexpr.get())
        if (absminexpr.get() != "") and (absmaxexpr.get() != "") : 
            #TODO gérer les ordonnées
            a.set_xlim([float(absminexpr.get()),float(absmaxexpr.get())])
        if var.get() == 1 :
            a.grid()
        elif var.get()==0 : 
            a.grid(False)
        #TODO ici, placer la ligne dans le traitement de condition adéquat et faire de même pour l'ordre des abscisses.
        moreConsigne1.configure(font="Courrier 10 italic bold",fg="red")
        canvas.draw()

    plot=Button(frame1,text="Plot !",command=plotting)
    plot.configure(font=('Courrier',15),bg = myColor4)
    plot.grid(row=14,column=1,columnspan=1,sticky=W)
        
    def clearall():
        #TODO
        #ici aussi il faudrait appeler une fonction externe avec un tableau d'entries par exemple
        absexpr.delete(0,'end')
        ordexpr.delete(0,'end')
        absminexpr.delete(0,'end')
        absmaxexpr.delete(0,'end')
        titleexpr.delete(0,'end')
        xlabelexpr.delete(0,'end')
        ylabelexpr.delete(0,'end')
        a.clear()
        canvas.draw()

    clearall=Button(frame1,text="Effacer tout",command=clearall)
    clearall.configure(font=('Courrier',15),bg=myColor4)
    clearall.grid(row=14,column=2,columnspan=1,sticky=E)

    return fen

#retourne un tableau contenant toutes les variables entrées dans la fenêtre
#def getData():

#renvoit le vecteur y
#def translate():
 
#plot y avec les variables adéquates
#def plot():
 
#retourne les variables sur la fenêtre
#def fetchData():

#comportement de la fenêtre
#windowBehavior():

def main():
    windowInit().mainloop()

main()
