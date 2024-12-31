#WAP to input user's first name & print its length

# name = input("Enter your fristname: ")
# length = len(name)
# print("The length of the name is: ",length)

# WAP to find the occurence of '$' in a string

# str1 = "I am studing $ college whose fees is $$$ for hostel and $ for college"
# count = str1.count("$")
# print("The occurence of $ in the string is: ",count)

# WAP to grade students based on marks

# marks = int(input("Enter marks obtained: "))

# if (marks > 90):
#     print("Grade A")
# elif (marks < 90 and marks >= 80):
#     print("Grade B")
# elif (marks < 80 and marks >= 70):
#     print("Grade C")
# else:
#     print("Grade D")

# WAP to check if a number is even or odd

# num = int(input("Enter a number: "))

# if (num % 2 == 0):
#     print(num,"is a even number")
# else:
#     print(num,"is a odd number")

# WAP to find the greatest of 3 numbers entered by users

# a,b,c = list(map(int, input("Enter the 3 numbers:").split()))

# if (a > b and a > c):
#     print(a,"is the greatest number")
# elif (b > a and b > c):
#     print(b,"is a greatest number")
# else:
#     print(c,"is the greatest number")

# WAP to check if a number is multiple of 7 or not

number = int(input("Enter the number: "))

if (number % 7 == 0):
    print(number,"is a multiple of 7 x",number // 7)
else:
    print(number,"is not a multiple of 7")
