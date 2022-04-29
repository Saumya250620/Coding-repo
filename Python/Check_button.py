from tkinter import*
class sb:
    def __init__(self,root):
        self.f = Frame(root,height = 400, width = 500)
        self.f.propagate(0)
        self.f.pack()

        self.v1 = IntVar()
        self.v2 = IntVar()
        self.v3 = IntVar()
        self.v4 = IntVar()
        

        self.c1 = Checkbutton(self.f,text="C", bg = "yellow",
                              fg="green",
                              variable=self.v1,
                              command=self.display,
                              font=("Arial",15,"bold"))
        self.c2 = Checkbutton(self.f,text="C++", bg = "yellow",
                              fg="green",
                              variable=self.v2,
                              command=self.display,
                              font=("Arial",15,"bold"))
        self.c3 = Checkbutton(self.f,text="Java", bg = "yellow",
                              fg="green",
                              variable=self.v3,
                              command=self.display,
                              font=("Arial",15,"bold"))
        self.c4 = Checkbutton(self.f,text="Python", bg = "yellow",
                              fg="green",
                              variable=self.v4,
                              command=self.display,
                              font=("Arial",15,"bold"))

        

        self.c1.place(x= 50,y=150)
        self.c2.place(x= 50,y=200 )
        self.c3.place(x= 50,y=250 )
        self.c4.place(x= 50,y=300 )


    def display(self):
        sb1 = self.v1.get()
        sb2 = self.v2.get()
        sb3 = self.v3.get()
        sb4 = self.v4.get()

        st = " "
        if sb1 == 1:
            st+="C "     #Concatenation

        if sb2 ==1:
            st +="C++ "

        if sb3 ==1:
            st +="Java "

        if sb4 == 1:
            st +="Python "

        self.l1 = Label(self.f,text = str(st))
        

        self.l1.place(x = 50,y = 350)

        
root = Tk()
s = sb(root)
root.mainloop()
