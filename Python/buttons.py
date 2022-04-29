from tkinter import *


class sb:
    def __init__(self,root):
        self.f=Frame(root,height=400,width=500)
        self.f.propagate(0)
        self.f.pack()
        self.c1 = Button(self.f, text = "Click me!",command=self.display,
                  fg="dark blue",bg="pink")
        #myButton = Button(root, text = "Click me!",state=DISABLED)
        self.c1.place(x=100,y=60)

    def display(self):
        self.l1 = Label(self.f,text="Look! I clicked a Button!!")
        self.l1.place(x=50,y=150)


root = Tk()
s = sb(root)
root.mainloop()
