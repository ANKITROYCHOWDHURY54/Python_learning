#1. Store following word meaning in a python dictionary

new_dict = {
    "cat" : "a small animal",
    "table": ["a piece of furniture", "list of facts & figures"]
}
print(new_dict)

#2. Ypu are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students

subjecsts = {"python","java","C++","C","python","javascript","java","python","java","C++","C"}
print(len(set(subjecsts)))

#3. WAP to enter marks of 3 students from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as a value

marks1 = int(input("Enter marks of student 1: "))
marks2 = int(input("Enter marks of student 2: "))
marks3 = int(input("Enter marks of student 3: "))

dict = {}

dict["Python"] = marks1
dict["Java"] = marks2
dict["C++"] = marks3

print(dict)

#4. Figure out a way to store 9 & 9.0 as seperate values in the set

num = {"9","9.0"}
print(num)
