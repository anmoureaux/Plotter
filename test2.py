import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.configure(background="white")
myFrame=tk.Frame(root,bg="white",width=1000,height=1000)
myFrame.pack()

can = tk.Canvas(root,bg="white",width=1000,height=1000)
can.pack()

photo1=ImageTk.PhotoImage(file="button1v3.png")
photo2=ImageTk.PhotoImage(file="button2v3.png")

class HoverButton(tk.Button):
    def __init__(self, master, **kw):
        tk.Button.__init__(self,master=master,compound="center",image=photo1,bg="white",activebackground="white",relief=tk.FLAT,**kw)
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
    def on_enter(self,e):
        self['image'] = photo2

    def on_leave(self,e):
        self['image'] = photo1
        self['background'] = "white"

classButton = HoverButton(myFrame,text="Classy Button")
classButton.grid()

root.mainloop()
