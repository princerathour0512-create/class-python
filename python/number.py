# # # # tem=int(input("enter tyemperature"))
# # # # if tem<10:
# # # #     print("temperature is cold")
# # # # elif tem>10 and tem<30:
# # # #     print("temperature is humid")
# # # # else:
# # # #     print("temper
# # # num=input("enter the number")
# # # lst=list(map(int,num.split()))
# # # # even_count=0
# # # # odd_count=0
# # # # for i in lst:
# # # #     if i%2==0:
# # # #         even_count += 1
# # # #     else:
# # # #         odd_count += 1
# # # # print("even count is",even_count)   
# # # # print("odd count is",odd_count)   
# # # largest=lst[0]
# # # # print("largest number is",largest)
# # # for i in lst:
# # #     if i>largest:
# # #         largest=i
# # # print("largest number is",largest)
# # word=input("enter the word:")
# # char=input("enter the character:")
# # count=0
# # for i in word:
# #     if i==char:
# #         count += 1
# # print("count of character is",count)
# # word=input("enter the word:")
# # palimdrome=word[::-1]
# # if word==palimdrome:
# #     print("word is palimdrome")
# # else:
# #     print("word is not palimdrome")
# text = input("Enter a string: ")

# reverse = ""

# for ch in text:
#     reverse = ch + reverse

# if text == reverse:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")
# n= int(input("enter the number"))

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()
        
# n = int(input("Enter number of rows: "))

# for i in range(1, n + 1):
#     print(" " * (n - i), end="")

#     for j in range(1, 2 * i):
#         print(j, end="")

#     print()
lst= [1,3,5,8,9,11]
for i in lst:
    if i % 2 == 0:
        break
    print(i)
   
