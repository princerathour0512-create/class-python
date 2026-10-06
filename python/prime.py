num = int(input("Enter a number: "))

# if num <= 1:
#     print("Not a prime number")
# else:
#     for i in range(2, num):
#         if num % i == 0:
#             print("Not a prime number")
#             break
#     else:
#         print("Prime number")
import math
is_prime = True
if num <= 1:
    is_prime = False
else:
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print("Prime number")
else:
    print("Not a prime number")