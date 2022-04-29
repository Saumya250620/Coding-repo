from tkinter import *
import math


class sb:
    def __init__(self,root):
        self.f=Frame(root,height=400,width=500)
        self.f.propagate(0)
        self.f.pack()
        self.e=Entry(self.f,width=50,borderwidth=5,relief=RIDGE)
        self.e.grid(row=0,column=0,columnspan=5,padx=10,pady=15)

        
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
        self.equal = Button(self.f,text="=",padx=91,pady=20,command = self.button_equal)
        self.clear = Button(self.f,text="C",padx=40,pady=20,command = self.button_clear)

        self.subtract = Button(self.f,text="-",padx=40,pady=20,command = self.button_subtract)
        self.multiply = Button(self.f,text="*",padx=40,pady=20,command = self.button_multiply)
        self.divide = Button(self.f,text="/",padx=40,pady=20,command = self.button_divide)

        self.mod = Button(self.f,text="mod",padx=40,pady=20,command = self.button_mod)
        self.exp = Button(self.f,text="e",padx=91,pady=20,command = self.button_exp)
        self.Bksp = Button(self.f,text="Bksp",padx=40,pady=20,command = self.button_Bksp)

        self.sin = Button(self.f,text="sin",padx=40,pady=20,command = self.button_sin)
        self.cos = Button(self.f,text="cos",padx=40,pady=20,command = self.button_cos)
        self.tan = Button(self.f,text="tan",padx=40,pady=20,command = self.button_tan)

        self.factorial = Button(self.f,text="x!",padx=40,pady=20,command = self.button_factorial)
        self.inverse = Button(self.f,text="1/x",padx=40,pady=20,command = self.button_inverse)
        self.pi = Button(self.f,text="pi",padx=40,pady=20,command = self.button_pi())

        self.log = Button(self.f,text="lg",padx=40,pady=20,command = self.button_log)
        self.power = Button(self.f,text="^",padx=40,pady=20,command = self.button_power)
        self.sqrt = Button(self.f,text="sqrt",padx=40,pady=20,command = self.button_sqrt)

        self.deg = Button(self.f,text="deg",padx=40,pady=20,command = self.button_deg)
        self.ln = Button(self.f,text="ln",padx=40,pady=20,command = self.button_ln)

        self.openBracket = Button(self.f,text="(",padx=40,pady=20,command = self.button_openBracket)
        self.closeBracket = Button(self.f,text=")",padx=40,pady=20,command = self.button_closeBracket)
        self.decimal = Button(self.f,text=".",padx=40,pady=20,command = self.button_decimal)

        # put the buttons on the screen

        self.c1.grid(row=6,column=1)
        self.c2.grid(row=6,column=2)
        self.c3.grid(row=6,column=3)

        self.c4.grid(row=5,column=1)
        self.c5.grid(row=5,column=2)
        self.c6.grid(row=5,column=3)

        self.c7.grid(row=4,column=1)
        self.c8.grid(row=4,column=2)
        self.c9.grid(row=4,column=3)

        self.c0.grid(row=7,column=2)
        self.add.grid(row=6,column=4)
        self.equal.grid(row=7,column=3,columnspan=2)
        self.clear.grid(row=3,column=1)

        self.subtract.grid(row=5,column=4)
        self.multiply.grid(row=4,column=4)
        self.divide.grid(row=3,column=4)

        self.mod.grid(row=3,column=3)
        self.exp.grid(row=7,column=0,columnspan=2)
        self.Bksp.grid(row=3,column=2)

        self.sin.grid(row=2,column=2)
        self.cos.grid(row=2,column=3)
        self.tan.grid(row=2,column=4)

        self.factorial.grid(row=4,column=0)
        self.inverse.grid(row=5,column=0)
        self.pi.grid(row=6,column=0)

        self.log.grid(row=1,column=0)
        self.power.grid(row=2,column=0)
        self.sqrt.grid(row=3,column=0)

        self.deg.grid(row=2,column=1)
        self.ln.grid(row=1,column=1)

        self.openBracket.grid(row=1,column=2)
        self.closeBracket.grid(row=1,column=3)
        self.decimal.grid(row=1,column=4)


    #def display(self,value):
        #self.l1.delete(0,END)
        #self.l1.insert(0,value)

    def button_click(self,number):
        current=self.e.get()
        self.e.delete(0,END)
        self.e.insert(0,str(current) + str(number))

    def button_clear(self):
        self.e.delete(0,END)

    def button_add(self):
        first_number = self.e.get()
        global f_num
        global cal
        cal = "addition"
        f_num = float(first_number)
        self.e.delete(0,END)

    def button_equal(self):
        second_number = self.e.get()
        self.e.delete(0,END)
        result=''

        if cal == "addition":
            self.e.insert(0,f_num + int(second_number))

        if cal == "subtraction":
            self.e.insert(0,f_num - int(second_number))

        if cal == "multiplication":
            self.e.insert(0,f_num * int(second_number))

        if cal == "division":
            self.e.insert(0,f_num / int(second_number))

        if cal == "mod":
            self.e.insert(0,f_num % int(second_number))

        if cal == "tan":
            result=math.tan(math.radians(float(second_number)))
            self.e.insert(0,result)

        if cal == "cos":
            result=str(math.cos(math.radians(float(second_number))))
            self.e.insert(0,result)

        if cal == "sin":
            result=str(math.sin(math.radians(float(second_number))))
            self.e.insert(0,result)

        if cal == "exp":
            result = math.e
            self.e.insert(0,result)

    def button_subtract(self):
        first_number = self.e.get()
        global f_num
        global cal
        cal = "subtraction"
        f_num = int(first_number)
        self.e.delete(0,END)

    def button_multiply(self):
        first_number = self.e.get()
        global f_num
        global cal
        cal = "multiplication"
        f_num = int(first_number)
        self.e.delete(0,END)

    def button_divide(self):
        first_number = self.e.get()
        global f_num
        global cal
        cal = "division"
        f_num = int(first_number)
        self.e.delete(0,END)

    def button_mod(self):
        first_number = self.e.get()
        global f_num
        global cal
        cal = "mod"
        f_num = float(first_number)
        self.e.delete(0,END)

    def button_exp(self):
        first_number = self.e.get()
        global f_num
        global cal
        cal = "exp"
        f_num = first_number
        self.e.delete(0,END)
        return

    def button_Bksp(self):
        first_number=self.e.get()
        length=len(first_number)-1
        self.e.delete(length,END)

    def button_sin(self):
        first_number = self.e.get()
        global f_num
        global cal
        cal = "sin"
        f_num = float(first_number)
        self.e.delete(0,END)

    def button_cos(self):
        first_number = self.e.get()
        global f_num
        global cal
        cal = "cos"
        f_num = float(first_number)
        self.e.delete(0,END)

    def button_tan(self):
        first_number = self.e.get()
        global f_num
        global cal
        cal = "tan"
        f_num = first_number
        self.e.delete(0,END)

    def button_factorial(self):
        return

    def button_inverse(self):
        return

    def button_pi(self):
        return

        #first_number = self.e.get()
        #self.current=math.pi
        #self.display(self.current)

    def button_log(self):
        return

    def button_power(self):
        return

    def button_sqrt(self):
        return

    def button_deg(self):
        return

    def button_ln(self):
        return

    def button_openBracket(self):
        return

    def button_closeBracket(self):
        return

    def button_decimal(self):
        return

root = Tk()
s = sb(root)
root.title("Simple Calculator")
root.iconbitmap('calculator_DRg_icon.ico')
root.mainloop()
