from tkinter import*
class sb:
    def __init__(self,root):
        self.t = Text(root,width=70, height=13,wrap=NONE)
        for i in range(50):
            self.t.insert(END,"This is some text i am using. ")

        self.t.pack(side = TOP, fill= X)

        self.s1 = Scrollbar(root,
                            orient=HORIZONTAL,
                            command=self.t.xview)
        self.t.configure(xscrollcommand= self.s1.set)
        self.s1.pack(side=BOTTOM, fill= X)
root = Tk()
s = sb(root)
root.mainloop()
