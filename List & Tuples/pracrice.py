# WAP to ask the user to enter names of their 3 favourite movies & store them in a list
movies = []

movie1 = input("Enter movie 1:")
movie2 = input("Enter movie 2:")
movie3 = input("Enter movie 3:")
movies.append(movie1)
movies.append(movie2)
movies.append(movie3)
print(movies)

# WAP to check if a list contains a palindrome of elements

list = [1, 2, 3, 2, 1]

list1=list.copy()
list1.reverse()

if (list1 == list):
    print("Palindrome")
else:
    print("Not a palindrome")

list1 = [1, 2, 3, 4, 5]

list2 = list1.copy()
list2.reverse()

if (list2 == list):
    print("Palindrome")
else:
    print("Not a palindrome")

# WAP to count the number of students with the "A" grade in the following tuple

grades = ("C","D","A","A","B","B","A")
students = grades.count("A")
print(students)

grades1 = list(grades)
grades1.sort()
print(grades1)

