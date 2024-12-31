str1  = "This is a string\n" #Preferable
str2 = 'Ankit\n'
str3 ='''This is a string.\n'''
str4 = "This is mycollege's name"
print(str1,str2,str3,str4)

#Concatenation of strings

mystr1 = "Ankit "
mystr2 = "Roy Chowdhury"

final_str = mystr1 + mystr2
print(final_str)

# Length of string

print(len(final_str))

# Indexing in strings

str = "My New String"
ch = str[4]
print(ch)

# Slicing in strings

str1 = "My New World"
substr = str1[3:12] # put +1 at the ending index
# Alternate way
substr1 = str1[3:] # put only starting index
print(substr)

#Negative Indexing
str2 = "apple"
print(str2[-3:-1])

# String Functions:

# 1. str.endswith("substring")
strg1 = "i am studing python Online"

print(strg1.endswith("ine"))
print(strg1.endswith("I"))

#2. str.captalize()
strg1 = strg1.capitalize()
print(strg1)

#3. str.replace(old,new)

strg2 = "I am at home"
strg2 = strg2.replace("home","hostel")
print(strg2)

#4. str.find(word) #returns 1st index at first occurence

print(strg2.find("hostel"))

#5. str.count("word")

print(strg2.count("a"))


### Conditional Statements
age  = 20

if (age>=18):
    print("Can vote and apply for liscence")
elif (age>=16):
    print("Cannot vote and apply for liscence")
else:
    print("Play games")
