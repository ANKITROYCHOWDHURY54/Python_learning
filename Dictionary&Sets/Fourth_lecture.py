dict = {
    "key": "value",
    "name" : "Ankit",
    "learning": "python",
    "age" : 35,
    "is_adult" : True,
    "subjects" : ('Dictionary','Sets')
}

dict1 = {}
print(type(dict1))
print(dict["name"])
print(dict["learning"])
print(dict["key"])
print(dict["age"])
print(dict["is_adult"])
print(dict["subjects"])

dict["name"] = "Sushmita"
dict["surname"] = "Poddar"

#Nested Dictionary

students = {
    "name" : "Ankit",
    "subjects" : {
        "physics" : 97,
        "chemistry" : 88,
        "math" : 95
    }
}

print(students["subjects"]["physics"])


#Dictionary Methods

#1. dict.keys() Returns all keys

print(tuple(students.keys()))

#2. dict.values() Returns all values

print(list(students.values()))

#3. dict.items() Returns all (key,val) pairs as tuples

print(students.items())

#4.dict.get("key") Returns the key according to value 

print(students.get("name")) # doesn't give error if key not exist, it will give None as a value

#5. dict.update(ndict) Inserts the specified items to the dictionary

new_dict = {"city" : "delhi", "food" : "biryani"}
students.update(new_dict)

print(students)


# Sets in python

num1 = [1,2,3,2]  # Doesn't allow duplicate values
print(set(num1))

collection = {1,2,3,5}
print(type(collection))

collection1 = set()
print(type(collection1))

#Set Methods

#1 .set.add(el) Adds an  element

collection1.add(1)
collection1.add(2)
collection1.add(3)
collection1.add("Hello Bro")

print(collection1)

#2. set.remove(el) Removes an element

collection1.remove(1)
print(collection1)

#3. set.clear() Empties the set

collection1.clear()
print(len(collection1))

#4. set.pop() Removes a random value

collection2 = {"Hello" , "Ankit", "Hello", "Sushmita", "Congratulations"}

print(collection2.pop())

#5. set.union(set1) Returns a new set with all elements from both sets

set1 = {1,2,3}
set2 = {2,3,4}

print(set1.union(set2))

#6. set.intersection(set1) Returns a new set with all common elements from both sets

print(set1.intersection(set2))