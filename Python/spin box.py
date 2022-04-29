from tkinter import*
class sb:
    def __init__(self,root):
        self.f = Frame(root,height = 400, width = 500)
        self.f.propagate(0)
        self.f.pack()

        self.v1 = IntVar()
        self.v2 = StringVar()

        self.s1 = Spinbox(self.f,from_=5, to = 15, bg = "yellow",textvariable=self.v1,font=("Arial",15,"bold"),width = 20)

        self.s2 = Spinbox(self.f,values=("Punjab","Delhi","UP"),
                     bg = "blue", textvariable = self.v2,
                     width = 20, font=("Arial",15,"bold"))

        self.s1.place(x= 50,y=150)
        self.s2.place(x= 50,y=200 )

        
        self.b = Button(self.f,text="Submit",command = self.display)

        self.b.place(x=50, y=250)


    def display(self):
        sb1 = self.s1.get()
        sb2 = self.s2.get()

        self.l1 = Label(self.f,text = str(sb1))
        self.l2 = Label(self.f,text = str(sb2))

        self.l1.place(x = 50,y = 300)
        self.l2.place(x = 50,y = 350)

        
root = Tk()
s = sb(root)
root.mainloop()
