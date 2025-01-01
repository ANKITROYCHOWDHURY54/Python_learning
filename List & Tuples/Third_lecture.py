### list in python ###

marks = [94.4,87.5,95.2,66.4,44.1]
print(marks)
print(type(marks))
print(len(marks))
print(marks[0],marks[1])


students = ["karan",95.4,"Delhi"] # List are mutable but String is immutable in python
print(students)
students[0] = "Sushmita"
print(students)

# List Slicing

marks2 = [85,75,94,63,48]
print(marks2[1:4])
print(marks2[:4]) # Same as marks2[0:4]
print(marks2[-3:-1])

# List Methods

# 1. list.append("element") Adds element at the end of the list

marks3 = [85,94,60]
marks3.append(90)
print(marks3)

#2. list.sort() Sorts in ascending order

marks3.sort()
fruits = ["banana","apple","litchi"]
print(marks3)
fruits.sort()
print(fruits)

#3. list.sort(reverse = True) Sorts in descending order

marks3.sort(reverse = True)
fruits.sort(reverse =  True)
print(marks3,fruits)

#4. list.reverse() Reverses the list

marks3.reverse()
fruits.reverse()
print(marks3,fruits)

#5. list.insert(index,element) Inserts elements at a particular index

list = [2,1,3]
list.insert(1,4)
print(list)

#6. list.pop(index) Removes the element at the specified index

list.pop(2)
print(list)

#7. list.remove(element) Removes the first occurence of the element

list.remove(4)
print(list)

#### Tuples in Python ###

# Tuples are immutable

tup = (1,2,3,2,4,3,2)
print(type(tup))
print(tup[0])

# Tuple Slicing

print(tup[1:3])

# Tuple Methods

#1. tup.index(element) Returns the index of the first occurence element

print(tup.index(2))

#2. tup.count(element) Returns the number of times the element appears in the tuple

print(tup.count(2))