import lecture1, pickle
f = open("emp.dat","wb")
n = int(input("Enter the number of employees"))
for i in range(n):
    eid = int(input("Ënter the employee id of employee = "))
    name =input("Enter the name of employee = ")
    sal = float(input("Enter the salary of employee = "))
    e = lecture1.lecture1(eid,name,sal)
    pickle.dump(e,f)
f.close()
