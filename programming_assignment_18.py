# Program 1
print ("**** Removing strings from a list ****")
num = int(input("Enter the number of elements in the list : "))

lst = []
for i in range(0, num):
    x = input("Enter the elements of the list")
    if x.isdigit():
        x = int(x)
        lst.append(x)
    else:
        lst.append(x)

for i in lst:
    if i.isalnum():
        lst.remove(i)


print ("The list after removing the strings : ", lst)


# Program 2
print("**** Print a string in the reverse order ****")


def reverser(string1):
    lst = []
    for i in string1:
        lst.append(i)
    lst.reverse()
    str1 = ''
    for i in lst:
        str1 = str1 + i

    str2 = ''
    for i in str1:
        if i.islower():
            str2 = str2 + i.upper()
        else:
            str2 = str2 + i.lower()
    return str2


string_1 = input("Enter your string : ")
str2 = reverser(string_1)
print(str2)

# Program 4

print("**** Factorial of a number recursively **** ")


def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n * recur_factorial(n - 1)


num = int(input("Enter your number :"))

# check if the number is negative
if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of", num, "is", recur_factorial(num))


# Program 5
print ("**** Moving an item to the end of the list **** ")


num = int(input("Enter the number of elements in your list : "))
lst = []
for i in range (0,num):
    x = int(input())
    lst.append(x)

item = int(input ("Enter the item you want to move to the end"))

for i in lst:
    if i == item:
        lst.remove(i)
        lst.append(i)

print (lst)