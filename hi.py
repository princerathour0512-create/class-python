# print(2**3+10-20)
"""elecrticity bill calculator
elcricity charges are as follows:
first 100 units - 5 per unit
next 100 units - 7 per unit
beyond 200 units - 10 per unit
wap to calculatethe bill amount for a given number of units consumed"""

n=int(input("Enter the number of units consumed: "))
if n<=100:
    bill=n*5
elif n<=200:
    bill=100*5+(n-100)*7
else:
    bill=100*5+100*7+(n-200)*10
print("The electricity bill amount is:",bill)
""" student result evaluation
a student passes if they score>=40 in each subject and the average score is >=50
wap that takes marks of 3 subjects and prints whether the student has passed or failed"""
marks1=int(input("Enter marks for subject 1: "))
marks2=int(input("Enter marks for subject 2: "))
marks3=int(input("Enter marks for subject 3: "))    
average=(marks1+marks2+marks3)/3
if marks1>=40 and marks2>=40 and marks3>=40 and average>=50:
    print("The student has passed.")
else:
    print("The student has failed.")