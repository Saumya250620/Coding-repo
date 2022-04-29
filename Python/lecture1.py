'''
def cc(l):
    t = 0
    for i in l:
        t = t + l
        avg = t/len(l)
        return t,avg

t, a = cc([10,20,30])           #[10,20,'d']        #[]
print(t)
print(a)
'''

class Emp:
    def __init__(self,eid,name,sal):
        self.eid= eid
        self.name = name
        self.sal = sal
        
    def display(self):
        
        print("Employee id", self.eid)
        print("Employee Name", self.name)
        print("Employee Salary", self.sal)
