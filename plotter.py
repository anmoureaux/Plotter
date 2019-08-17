#!/usr/bin/env python

#tentative d'écriture d'un programme de plotting de fonctions à une variable 1D opérationnel
#Anatole Moureaux, aout 2019


import numpy as np
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

    
    fen.columnconfigure(0)
    fen.columnconfigure(1)
    fen.columnconfigure(2)
    fen.columnconfigure(3)
    fen.columnconfigure(4)
    fen.columnconfigure(5)
    fen.columnconfigure(6)

    fen.rowconfigure(0,pad=0)
    fen.rowconfigure(1,pad=0)
    fen.rowconfigure(2,pad=0)
    fen.rowconfigure(3,pad=0)
    fen.rowconfigure(4,pad=0)
    fen.rowconfigure(5,pad=20)
    fen.rowconfigure(6,pad=20)
    fen.rowconfigure(7,pad=20)
    fen.rowconfigure(8,pad=20)
    fen.rowconfigure(9,pad=20)
    fen.rowconfigure(10,pad=20)
    fen.rowconfigure(11,pad=20)
    fen.rowconfigure(12,pad=20)
    fen.rowconfigure(13,pad=20)
    fen.rowconfigure(14,pad=20)

    myColor1 = '#78f8ff'
    myColor2 = '#78cbff'
    myColor3 = '#75a1ff'
    myColor4 = '#7575ff'
    myColor5 = '#445CFF'
    
    barre1 = Label(fen,text="")
    barre1.configure(bg=myColor1,font=('Courrier',30))
    barre1.grid(row=0,column=0,columnspan=3,sticky=EW)
    barre2 = Label(fen,text="")
    barre2.configure(bg=myColor1,font=('Courrier',30))
    barre2.grid(row=0,column=3,columnspan=4,sticky=EW)

    title = Label(fen,text="Plot")
    title.configure(font=('Courrier',30),bg=myColor1)
    title.grid(row=0,column=0,columnspan = 7,sticky=EW)

    greatbarre1=Label(fen,text="")
    greatbarre1.configure(bg=myColor2,font=('Courrier',20))
    greatbarre1.grid(row=1,column=0,columnspan=7,sticky=EW)
    greatbarre2=Label(fen,text="                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               ")
    greatbarre2.configure(bg=myColor3,font=('Courrier',10))
    greatbarre2.grid(row=2,column=0,columnspan=7,sticky=EW)

    greatbarre3=Label(fen,text="")
    greatbarre3.configure(bg=myColor4,font=('Courrier',5))
    greatbarre3.grid(row=3,column=0,columnspan=7,sticky=EW)

    greatbarre4=Label(fen,text="")
    greatbarre4.configure(bg=myColor5,font=('Courrier',2))
    greatbarre4.grid(row=4,column=0,columnspan=7,sticky=EW)

    funConsigne = Label(fen,text="Écrivez ici la fonction à afficher (sous le format y=f(x)) : ")
    funConsigne.configure(font=('Courrier',20),bg = myColor2)
    funConsigne.grid(row=5,column = 0,columnspan=2,sticky=EW)
   
    ylabel = Label(fen,text="f(x) = ")
    ylabel.configure(font=('Courrier',20))
    ylabel.grid(row=6,column=0,columnspan=1,sticky=W)

    funexpr = Entry(fen)
    funexpr.grid(row=6,column=1,columnspan=1,sticky=EW)

    absconsigne = Label(fen,text="Entrez les abscisses minimale et maximale : ")
    absconsigne.configure(font=('Courrier',20),bg=myColor3)
    absconsigne.grid(row=7,column=0,columnspan=2,sticky=EW)
    
    absminlabel = Label(fen,text="abscisse minimale : ")
    absminlabel.configure(font=('Courrier',20))
    absminlabel.grid(row=8,column=0,columnspan=1,sticky=W)

    absminexpr = Entry(fen)
    absminexpr.grid(row=8,column=1,columnspan=1,sticky=EW)

    absmaxlabel = Label(fen,text="abscisse maximale : ")
    absmaxlabel.configure(font=('Courrier',20))
    absmaxlabel.grid(row=9,column=0,columnspan=1,sticky=W)

    absmaxexpr = Entry(fen)
    absmaxexpr.grid(row=9,column=1,columnspan=1,sticky=EW)

    optconsigne = Label(fen,text="Options supplémentaires : ")
    optconsigne.configure(font=('Courrier',20),bg=myColor4)
    optconsigne.grid(row=10,column=0,columnspan=2,sticky=EW)
    
    titlelabel = Label(fen,text=("Titre : "))
    titlelabel.configure(font=('Courrier',20))
    titlelabel.grid(row=11,column=0,columnspan=1,sticky=W)

    titleexpr = Entry(fen)
    titleexpr.grid(row=11,column=1,columnspan=1,sticky=EW)

    xlabel = Label(fen,text=("Nom de l'axe x : "))
    xlabel.configure(font=('Courrier',20))
    xlabel.grid(row=12,column=0,columnspan=1,sticky=W)

    xlabelexpr = Entry(fen)
    xlabelexpr.grid(row=12,column=1,columnspan=1,sticky=EW)

    ylabel = Label(fen,text=("Nom de l'axe y : "))
    ylabel.configure(font=('Courrier',20))
    ylabel.grid(row=13,column=0,columnspan=1,sticky=W)

    ylabelexpr = Entry(fen)
    ylabelexpr.grid(row=13,column=1,columnspan=1,sticky=EW)
    
    return fen
    
def main():
    windowInit().mainloop()

main()
