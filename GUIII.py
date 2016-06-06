from tkinter import *
from tkinter.ttk import *
from PIL import Image
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
    
    im = Image.open("dog.jpg")
    im.show()
    # multiply each pixel by 1.2
    #out = im.point(lambda i: i * 1.8)
    # split the image into individual bands
    source = im.split()
    
    R, G, B = 0, 1, 2

    # select regions where red is less than 100
    mask = source[R].point(lambda i: i < 100 and 255)

    # process the green band
    out = source[G].point(lambda i: i * 0.7)

    # paste the processed band back, but only where red was < 100
    source[G].paste(out, None, mask)

    # build a new multiband image
    im = Image.merge(im.mode, source)
    im.show()
    #out.show()
    root= Tk()
    apX=RRR(m=root)
    apX.mainloop()
#textd= Label(root,text="fuck this",width="30",heigh="5",bg="red",fg="black")
#textd.pack()
#root.mainloop()
