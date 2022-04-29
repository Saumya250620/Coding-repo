'''
Suppose you want to develop a program to play a lottery.
The program randomly generates a two-digit number,
prompts the user to enter a two-digit number,
and determines whether the user wins according to the following rules:

1. If the user's input matches the lottery in the exact order,
the award is Rs 1,000,00.

2. If all the digits in the user's input match all the digits in the lottery number,
the award is Rs 50,000.

3. If one digit in the user's input matches a digit in the lottery number,
the award is Rs 10,000.

'''
import random
RN = random.randint(10,99)
RN1 = RN %10
RN2 = RN // 10
while (RN1 == RN2):
    RN = random.randint(10,99)
print("random generated number = ",RN)
number = int(input("Enter a two-digit number = "))
print ("Your enter number is : ",number)
N = number
N1 = N %10
N2 = N // 10
sum = (RN1*10)+RN2
if number == RN:
    print("You won Rs 1,000,00")
elif N == sum:
    print ("You have won Rs 50,000")
elif (N1==RN1) or (N1 == RN2) or (N2 == RN1) or (N2 == RN2):
    print ("You have won Rs 10,000")
else:
    print("Try again")
