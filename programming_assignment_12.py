# Program 1
print("**** Program to Extract Unique Dictionary values ****")
size = int(input("Enter the size of your dictionary : "))
empl = {}

while len(empl)<size:
    name = input("Enter the name : ")
    sal = int(input("Enter the salary : "))
    empl[name] = sal

lst = set(empl.values())
print ("Unique values from the dictionary ", lst)


# Program 2
print("**** Program to find the sum of all items in the dictionary ****")
size = int(input("Enter the size of your dictionary : "))
empl = {}

while len(empl)<size:
    name = input("Enter the name : ")
    sal = int(input("Enter the item : "))
    empl[name] = sal

sum =0
lst = empl.values()
for i in lst:
    sum = sum + i

print ("Sum of all the items is : ", sum)


# Program 3
print("**** Merge two dicts ****")
size = int(input("Enter the size of your first dictionary : "))
dict1 = {}
dict2 = {}

while len(dict1)<size:
    name = input("Enter the key : ")
    sal = int(input("Enter the item : "))
    dict1[name] = sal

size2 = int(input("Enter the size of your second dictionary : "))

while len(dict2)<size2:
    key = input("Enter the key : ")
    val = int(input("Enter the item : "))
    dict2[key] = val

dict3 = {**dict1, **dict2}
print ("Merged dictionaries : ",dict3)


# Program 5
from collections import OrderedDict
print("**** Merge two dicts ****")
size = int(input("Enter the size of your first dictionary : "))
dict1 = {}

while len(dict1)<size:
    name = input("Enter the key : ")
    sal = int(input("Enter the value : "))
    dict1[name] = sal

dict1 = OrderedDict(dict1)
key = input("Enter your new key : ")
value = int(input("Enter your value :"))
dict1.update({key:value})
dict1.move_to_end(key, last = False)


print (dict1)


# Program 6
