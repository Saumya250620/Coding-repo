# some changes are left after converting it to scientific calci

from tkinter import *


class sb:
    def __init__(self,root):
        self.f=Frame(root,height=400,width=500)
        self.f.propagate(0)
        self.f.pack()
        self.e=Entry(self.f,width=35,borderwidth=5)
        self.e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

        
        # define buttons
        self.c1 = Button(self.f,text="1",padx=40,pady=20,command=lambda: self.button_click(1))
        self.c2 = Button(self.f,text="2",padx=40,pady=20,command=lambda: self.button_click(2))
        self.c3 = Button(self.f,text="3",padx=40,pady=20,command=lambda: self.button_click(3))
        self.c4 = Button(self.f,text="4",padx=40,pady=20,command=lambda: self.button_click(4))
        self.c5 = Button(self.f,text="5",padx=40,pady=20,command=lambda: self.button_click(5))
        self.c6 = Button(self.f,text="6",padx=40,pady=20,command=lambda: self.button_click(6))
        self.c7 = Button(self.f,text="7",padx=40,pady=20,command=lambda: self.button_click(7))
        self.c8 = Button(self.f,text="8",padx=40,pady=20,command=lambda: self.button_click(8))
        self.c9 = Button(self.f,text="9",padx=40,pady=20,command=lambda: self.button_click(9))
        self.c0 = Button(self.f,text="0",padx=40,pady=20,command=lambda: self.button_click(0))
        
        self.add = Button(self.f,text="+",padx=40,pady=20,command = self.button_add)
        self.equal = Button(self.f,text="=",padx=40,pady=20,command = self.button_equal)
        self.clear = Button(self.f,text="Clear",padx=40,pady=20,command = self.button_clear)

        self.subtract = Button(self.f,text="-",padx=40,pady=20,command = self.button_subtract)
        self.multiply = Button(self.f,text="*",padx=40,pady=20,command = self.button_multiply)
        self.divide = Button(self.f,text="/",padx=40,pady=20,command = self.button_divide)

        self.divide = Button(self.f,text="/",padx=40,pady=20,command = self.button_divide)

        # put the buttons on the screen

        self.c1.grid(row=5,column=1)
        self.c2.grid(row=5,column=2)
        self.c3.grid(row=5,column=3)

        self.c4.grid(row=4,column=1)
        self.c5.grid(row=4,column=2)
        self.c6.grid(row=4,column=3)

        self.c7.grid(row=3,column=1)
        self.c8.grid(row=3,column=2)
        self.c9.grid(row=3,column=3)

        self.c0.grid(row=6,column=2)
        self.add.grid(row=5,column=4)
        self.equal.grid(row=6,column=3)
        self.clear.grid(row=2,column=1)

        self.subtract.grid(row=4,column=4)
        self.multiply.grid(row=3,column=4)
        self.divide.grid(row=2,column=4)

    def button_click(self,number):
        current=self.e.get()
        self.e.delete(0,END)
        self.e.insert(0,str(current) + str(number))

    def button_clear(self):
        self.e.delete(0,END)

    def button_add(self):
        first_number = self.e.get()
        global f_num
        global math
        math = "addition"
        f_num = int(first_number)
        self.e.delete(0,END)

    def button_equal(self):
        second_number = self.e.get()
        self.e.delete(0,END)

        if math == "addition":
            self.e.insert(0,f_num + int(second_number))

        if math == "subtraction":
            self.e.insert(0,f_num - int(second_number))

        if math == "multiplication":
            self.e.insert(0,f_num * int(second_number))

        if math == "division":
            self.e.insert(0,f_num / int(second_number))

        if math == "mod":
            self.e.insert(0,f_num % int(second_number))

    def button_subtract(self):
        first_number = self.e.get()
        global f_num
        global math
        math = "subtraction"
        f_num = int(first_number)
        self.e.delete(0,END)

    def button_multiply(self):
        first_number = self.e.get()
        global f_num
        global math
        math = "multiplication"
        f_num = int(first_number)
        self.e.delete(0,END)

    def button_divide(self):
        first_number = self.e.get()
        global f_num
        global math
        math = "division"
        f_num = int(first_number)
        self.e.delete(0,END)

    def button_mod(self):
        first_number = self.e.get()
        global f_num
        global math
        math = "mod"
        f_num = int(first_number)
        self.e.delete(0,END)
        

root = Tk()
s = sb(root)
root.title("Simple Calculator")
root.mainloop()
