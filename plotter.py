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
    title.grid(row=0,column=3,columnspan = 1,sticky=EW)

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
    funConsigne.configure(font=('Courrier',20),bg = myColor3)
    funConsigne.grid(row=5,column = 0,columnspan=7,sticky=W)
   
    return fen
    
def main():
    windowInit().mainloop()

main()
