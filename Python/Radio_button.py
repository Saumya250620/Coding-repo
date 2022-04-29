from tkinter import*
class sb:
    def __init__(self,root):
        self.f = Frame(root,height = 400, width = 500)
        self.f.propagate(0)
        self.f.pack()

        self.v1 = IntVar()
        

        self.c1 = Radiobutton(self.f,text="10th", bg = "yellow",
                              fg="green",
                              variable=self.v1,value = 1,
                              command=self.display,
                              font=("Arial",15,"bold"))
        self.c2 = Radiobutton(self.f,text="12th", bg = "yellow",
                              fg="green",value =2,
                              variable=self.v1,
                              command=self.display,
                              font=("Arial",15,"bold"))
        self.c3 = Radiobutton(self.f,text="Graduation", bg = "yellow",
                              fg="green",value = 3,
                              variable=self.v1,
                              command=self.display,
                              font=("Arial",15,"bold"))
        self.c4 = Radiobutton(self.f,text="PG", bg = "yellow",
                              fg="green", value = 4,
                              variable=self.v1,
                              command=self.display,
                              font=("Arial",15,"bold"))

        

        self.c1.place(x= 50,y=150)
        self.c2.place(x= 50,y=200)
        self.c3.place(x= 50,y=250)
        self.c4.place(x= 50,y=300)


    def display(self):
        sb1 = self.v1.get()

        st = " "
        if sb1 == 1:
            st+="10th"     #Concatenation

        if sb1 ==2:
            st +="12th"

        if sb1 ==3:
            st +="Graduation"

        if sb1 == 4:
            st +="PG"

        self.l1 = Label(self.f,text = str(st))
        

        self.l1.place(x = 100,y = 60)

        
root = Tk()
s = sb(root)
root.mainloop()
