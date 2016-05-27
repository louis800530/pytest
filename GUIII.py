from tkinter import *
from tkinter.ttk import *

class RRR(Frame):
    def __init__(self, m=None):
        Frame.__init__(self,m)
        self.grid()
        self.createWidgets()
    def createWidgets(self):
        self.it=Label(self)
        self.it["text"] = "Input:"
        self.it.grid(row=0, column=0)
        self.ifd = Entry(self)
        self.ifd["width"] = 60
        self.ifd.grid(row=0, column=1,columnspan=6)

        self.ot = Label(self)
        self.ot["text"] = "Output:"
        self.ot.grid(row=1, column=0)
        self.ofd = Entry(self)
        self.ofd["width"] = 60
        self.ofd.grid(row=1, column=1,columnspan=6)
        
        self.nb = Button(self)
        self.nb["text"] = "New"
        self.nb.grid(row=2, column=0)
        self.nb["command"] = self.nm
        
        self.dt = Label(self)
        wr="something happened"
        self.dt["text"] = wr
        self.dt.grid(row=3, column=0,columnspan=7)
        
    def nm(self):
        self.dt["text"] = "New Button"

if __name__ == '__main__':
    root= Tk()
    apX=RRR(m=root)
    apX.mainloop()
#textd= Label(root,text="fuck this",width="30",heigh="5",bg="red",fg="black")
#textd.pack()
#root.mainloop()
