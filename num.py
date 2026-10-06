# num = input("Enter a number: ")

# sum = 0

# for digit in num:
#     sum += int(digit)

# print("Sum =", sum)
# num = int(input("Enter a number: "))

# sum = 0

# while num > 0:
#     digit = num % 10
#     sum += digit
#     num = num // 10

# print("Sum =", sum)
# 67 
"""cerate a dictionary with name library and add name of 5 books as keys and the
 department they are associated with and print only the keys without using any 
 inbuild methods"""

# library = {
#     "Python": "Computer Science",
#     "Physics": "Science",
#     "Mathematics": "Mathematics",
#     "English": "Humanities",
#     "Chemistry": "Science"
# }

# for book in library:
#     print(book)
"""create a dictionary with name movies that stores name of the movie as key and the year of release as value and print only the values without using the index base method """
# movies = {
#     "Movie1": 2020,
#     "Movie2": 2019,
#     "Movie3": 2021,
#     "Movie4": 2018,
#     "Movie5": 2022
# }
# for year in movies.values():
#     print(year)
"""create a function with name password that takes the input as string and returns the strength 
of that password """
# def password(p):
#     strength = 0

#     if len(p) >= 8:
#         strength += 3   

#     if any(c.isupper() for c in p):
#         strength += 1

#     if any(c.islower() for c in p):
#         strength += 1

#     if any(c.isdigit() for c in p):
#         strength += 1

#     if any(not c.isalnum() for c in p):
#     strength += 1

#     if strength <= 2:
#         return "Weak"
#     elif strength <= 4:
#         return "Medium"
#     else:
#         return "Strong"


# p = input("Enter your password: ")
# print("Password Strength:", password(p))

"""create a function that check whether the given no. is armstrong or not """
def armstrong(n):
    original = n
    sum = 0 
    while n > 0:
        digit = n % 10
        sum += digit ** 3
        n = n // 10
    if sum == original:
        return "Armstrong"
    else:
        return "Not Armstrong"

num = int(input("Enter a number: "))

print(armstrong(num))


        