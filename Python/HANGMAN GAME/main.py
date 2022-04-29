import random
from wordlist import word_list
from hangman_art import stages
from tkinter import *
from tkinter import messagebox


class form:
    def __init__(self, root):
        #self.b1 = ""
        self.count = 5
        self.f = Frame(root, height=500, width=500, bg="white")
        self.f.propagate(0)
        self.f.pack()
        self.word = random.choice(word_list)
        print(self.word)
        self.length = len(self.word)
        self.a = []
        for i in range(self.length):
            self.a += "_"

        self.l = Label(self.f, text="HaNgMaN", font=("Arial", 25), bd=10, bg="light blue", fg="black")
        self.l.place(x=150, y=10)
        
        self.l1 = Label(self.f, text=self.a, font=("Arial,500"))
        self.l3 = Label(self.f, text="Take a guess!", font=("Arial,50"))
        self.l3.place(x=40, y=100)

        self.l2 = Label(self.f, text=stages[6], font=("Arial,500"))
        self.l2.place(x=50, y=150)

        self.name_var = StringVar()
        self.e1 = Entry(self.f, width=20,
                        font=("Arial,15"), textvariable=self.name_var)
        self.e1.place(x=200, y=100)
        self.b = Button(self.f, text="CHECK", width=15, height=2, command=lambda: self.display())

        self.b.place(x=50, y=350)

    def display(self):

        self.text = (self.name_var.get())
        self.name_var.set("")
        if (len(self.text) == 1):
            if (self.text in self.word):
                self.change(self.text)
            else:

                self.l2["text"] = stages[self.count]
                self.l2.place(x=50, y=150)
                self.count = self.count - 1
        else:

            messagebox.showerror("hangman", "error")

        if (self.count == -1):
            messagebox.showinfo("result", "lose")
            root.destroy()
            return 0

    def change(self, t):

        for i in range(self.length):       

            if t == self.word[i]:
                self.a[i] = t

        self.l1["text"] = self.a
        self.l1.place(x=300, y=200)
        if "_" not in self.a:
            messagebox.showinfo("result", "win")
            root.destroy()
            return 0


root = Tk()
root.title('Hangman')
root.iconbitmap('001-hangman-game.ico')
b = form(root)
root.mainloop()
