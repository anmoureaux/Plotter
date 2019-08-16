#!/usr/bin/env python

#tentative d'écriture d'un programme de plotting de polynômes à une variable 1D opérationnel

import numpy as np
import matplotlib.pyplot as plt
from tkinter import *

def main():

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
     
    barre1 = Label(fen,text="")
    barre1.configure(bg="cyan",font=('Courrier',30))
    barre1.grid(row=0,column=0,columnspan=3,sticky=EW)
    barre2 = Label(fen,text="")
    barre2.configure(bg="cyan",font=('Courrier',30))
    barre2.grid(row=0,column=3,columnspan=4,sticky=EW)

    title = Label(fen,text="Plot")
    title.configure(font=('Courrier',30),bg='cyan')
    title.grid(row=0,column=3,columnspan = 1,sticky=EW)    
    greatbarre1=Label(fen,text="")
    greatbarre1.configure(bg="blue",font=('Courrier',20))
    greatbarre1.grid(row=1,column=0,columnspan=7,sticky=EW)
    greatbarre2=Label(fen,text="                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               ")
    greatbarre2.configure(bg="black",font=('Courrier',10))
    greatbarre2.grid(row=2,column=0,columnspan=7,sticky=EW)
    
    fen.mainloop()

main()
