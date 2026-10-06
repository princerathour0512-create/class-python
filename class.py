# n=[int(x) for x in 
#    ["10","20","30"] ]
# print(n)    
# n = [int(x)**2 for x in ["10", "20", "30"]]

# print(n)
# input
# www.chatgpt.com
# chat.com, localhost
# abesit.edu.in
# output
# ['www.chatgpt.com', 'chat.com', 'abesit.edu.in']

# d=["www.chatgpt.com", "chat.com", "localhost", "abesit.edu.in"]
# normal=[x.lower().replace("www.", '') for x in d if"." in x]
# print(normal)

# n = [10, 15, 20, 25, 30, 35, 40]

# even = [x for x in n if x % 2 == 0]

# print(even)




"""
for the string s= "coorporate resource centre",write a single python statement for each of the following :
(i)count the number of times 'e' occurs 
(ii) convert the string to uppercase
(iii) obtain a list of all words 
(iv) replace 


"""
# s = "coorporate research centre "
# print(s.count('e')) 
# print(s.upper())
# print(s.split())




"""
write a python program for that :
(i)accepts n numbers from the user and store them in a list
(ii)uses a function that returns maximum and minimum and avearage as a tuple,
(iii)bulids a list of only even numbers using list comprehension


"""

# # Accept n numbers from the user
# n = int(input("Enter the number of elements: "))

# numbers = []

# for i in range(n):
#     num = int(input("Enter number: "))
#     numbers.append(num)


# # Function to find maximum, minimum and average
# def calculate(numbers):
#     maximum = max(numbers)
#     minimum = min(numbers)
#     average = sum(numbers) / len(numbers)

#     return maximum, minimum, average


# # Function call
# result = calculate(numbers)

# print("Maximum =", result[0])
# print("Minimum =", result[1])
# print("Average =", result[2])


# # List comprehension to create list of even numbers
# even_numbers = [x for x in numbers if x % 2 == 0]

# print("Even numbers =", even_numbers)
"""wap that takes a no. as input and prints the lcm of the particular no."""
# Program to find LCM of two numbers

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# greater = max(a, b)

# while True:
#     if greater % a == 0 and greater % b == 0:
#         lcm = greater
#         break
#     greater += 1

# print("LCM =", lcm) 
# file= open("demo.txt", "r")
# data=file.read()
# file.seek(0)
# data1=file.readline()
# file.seek(0)
# data2=file.readlines(10)
# file.seek(0)
# print(data)
# print(data1)
# print(data2)
# lst=[1,2,3,4]
# d={"name":"a"}
# file= open("demo.txt", "w")
# file.write(str(lst))
# msg= ["hello\n", "we\n", "are\n", "learning\n", "python\n"]
# file= open("demo.txt", "w")
# file.writelines(msg)
"""wap to create a file that stores the count of vowels coming from a function with name 
count_vowel that takes a string and count the number of vowels in it and returns the count
 to the main program and then store the count in a file"""
# def count_vowel(s):
#     vowels = "aeiouAEIOU"
#     count = 0
#     for char in s:
#         if char in vowels:
#             count += 1
#     return count

# # Example usage
# s = "Hello, World!"
# vowel_count = count_vowel(s)

# # Store the count in a file
# with open("vowel_count.txt", "w") as file:
#     file.write(str(vowel_count))
# with open("demo.txt", "r") as file:
#     count = file.read()
#     # print("Number of vowels:", count)
# count=count.replace("hello","hello prince")
# with open("demo.txt", "w") as file:
#     file.write(count)
# with open("demo.txt", "r") as file:
#     count = file.read()

# count = count.replace("hello", "hello prince")

# with open("demo.txt", "w") as file:
#     file.write(count)
"""create a file with name merge.txt that takes the content of two separate file that stores 
the merge content into merge.txt"""
# with open("file1.txt", "r") as file1:
#     data1 = file1.read()

# with open("file2.txt", "r") as file2:
#     data2 = file2.read()

# with open("merge.txt", "w") as merge:
#     merge.write(data1)
#     merge.write(data2)
# with open ("file1.txt","r") as source:
#     data= source.read()
# with open ("file2.txt","w") as destination:
#     destination.write(data)
# import os
# if os.path.exists("merge.txt"):

#     os.remove("merge.txt")
#     print("File deleted successfully.")
# else:
#     print("File does not exist.")
"""craete a number guess game that takes input from user with limit of 5 chances if user guesses 
a higher no. or a lower no. then the actual no. provide a suitable warning and if the no. guess
 is correct then show a bin message and if the attempts are over then show a game over."""
import random

actual_no = random.randint(1, 100)

for attempt in range(1, 6):
    guess = int(input("Guess the number (1-100): "))

    if guess > actual_no:
        print("Warning: Your guess is HIGHER than the actual number.")

    elif guess < actual_no:
        print("Warning: Your guess is LOWER than the actual number.")

    else:
        print("🎉 Congratulations! You guessed the correct number!")
        print("You won the game!")
        break

else:
    print("Game Over!")
    print("The actual number was:", actual_no)