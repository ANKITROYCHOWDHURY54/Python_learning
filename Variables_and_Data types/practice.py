# WAP to find the area of a square 
side = float(input("Enter the side of the square: "))
area = side * side
area = side ** 2
print("The area of the square is: ",area)

# WAP to input 2 floating point numbers and print their average

num1 = float(input("Enter number1: "))
num2 = float(input("Enter number2: "))
average = (num1 + num2) / 2
print("The average of ",num1,"and",num2,"is",average)

#WAP to input 2 int numbers, a and b.
# print True if a is greater than b, False otherwise.

a = int(input("Enter number1: "))
b = int(input("Enter number2: "))
print(a >= b)