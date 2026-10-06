# create a function which multiply and takes two parameter and returns the multiplication of two numbers
# def multiply(a, b):
#     return a * b    
# x = int(input("Enter first number: "))
# y = int(input("Enter second number: "))
# result = multiply(x, y)     
# print("Multiplication of", x, "and", y, "is:", result)

"""create a fuction with name power that takes two aruments (base,exponent) and print the poower of the number"""
# def power(base, exponent):
#     return base ** exponent
# x = int(input("Enter base number: "))
# y = int(input("Enter exponent number: "))
# result = power(x, y)
# print(x, "raised to the power of", y, "is:", result)    


  
"""create a calculator function which takes three parameters (num1, num2, operation) and perform the operation based on the operator passed as parameter"""
# def calculator(num1, num2, operation):
#     if operation == '+':
#         return num1 + num2
#     elif operation == '-':
#         return num1 - num2
#     elif operation == '*':
#         return num1 * num2
#     elif operation == '/':
#         if num2 != 0:
#             return num1 / num2
#         else:
#             return "Error: Division by zero"
#     else:
#         return "Error: Invalid operation"
    
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# operation = input("Enter operation (+, -, *, /): ")
# result = calculator(num1, num2, operation)
# print("Result:", result)    
 
# def total(*args):
#     return sum(args)
# print(total())  
# n = input("Enter the numbers to add")
# l =list(map(int, n.split()))

# print(total(*l))
"""create a function with name and username then takes argument and string and returns the output in the given format"""
# def greet(name, username):
#     return f"Hello, {name}! Your username is {username}."
# name=input("Enter your name: ")
# username=input("Enter your username: ")
# result=greet(name, username)
# print(result)

"""create a function which takes a number as argument and check whether the number is even or odd and return the result"""
# def check_number(a):
#     if a%2==0:
#         return "Even"
#     else:
#         return "Odd"
# x=int(input("Enter a number: "))
# result=check_number(x)
# print("The number", x, "is", result)    
# def demo():
#     print("start")
#     yield 1
#     print("stop")
#     yield 2

# x= demo()
# print(next(x))
# print(next(x))
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
# n=int(input("Enter a number to find its factorial: "))
# result=factorial(n)
# print("The factorial of", n, "is:", result)



"""--------------""""""LEMDA FUCTION""""""-------------"""
# var=lambda a, b: a + b
# x=int(input("Enter first number: "))
# y=int(input("Enter second number: "))
# result=var(x, y)
# print("The sum of", x, "and", y, "is:", result)
"""create a function the name discount that takes the price of the product and applies the discount of 10 % if amount is greater that ₹1000 """

# def discount(price):
#     if price > 1000:
#         price = price - (price * 10 / 100)
#     return price
# price = float(input("Enter the price: "))
# print("Final price:", discount(price))

"""create a function with membership that takes the age and duration of the membership and if the age is greater than 18 and duration is more than 1 year, then apply a discount of 5% on the final amount if greater than ₹1000"""
def membership(age, duration, amount):
    if age>18 and duration>1 and amount>1000:
        amount=amount-(amount*5/100)
    return amount
age=int(input("Enter your age: "))
duration=int(input("Enter the duration of membership in years: "))
amount=float(input("Enter the amount: "))
print("Final amount:", membership(age, duration, amount))



