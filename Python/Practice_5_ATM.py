x = int(input("Enter your current balance = "))

y=float(input("Enter cash for withdrawal = "))
#y=format(x,".2f")
sum=0.0
if(y%5==0):
    if(x>=y):
        print("Transaction Successful")
        sum = x - y - 0.50
        print("current amount",sum)
    else:
        print("Invalid amount")
else:
    print("Withdrawal denied")
    exit(0)
