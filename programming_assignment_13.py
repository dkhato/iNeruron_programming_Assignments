# Program 1
import math

print("Program to calculate and print values accordingly : ")
print("Q = Square root of [(2 * C * D)/H] ")


def square_root(d, c, h):
    i = (2 * c * d) / h
    return math.sqrt(int(i))


c= 50
h = 30
d = []
for i in range(0,3):
    d.append(int(input("Enter D : ")))

for i in d:
    print (square_root(i,c,h))


# Program 3
print ("**** sort a String of words alphabetically ****")
string_1 = input("Enter your string separated by , : ")
words = string_1.split(",")
words.sort()
word = []
str1 = " "
for i in words:
    str1 = str1 + i + ","

print (str1)


# Program 4
print ("**** Remove the duplicates ****")
string_1 = input("Enter your string separated by : ")
words = string_1.split()
word = []
for i in words:
    if i not in word:
        word.append(i)

str1 = " "
word.sort()
for i in word:
    str1 = str1 + i + ","

print (str1)


# Program 5
print ("**** Count the number of letters and digits ****")
string_1 = input("Enter your string separated by : ")
words = string_1.split()
digits = ['1','2','3','4','5','6','7','8','9','0']
no_of_digits = 0
no_of_letters = 0
for i in words:
    for j in i:
        if j not in digits:
            no_of_letters = no_of_letters + 1
        else:
            no_of_digits = no_of_digits + 1

print ("The number of letters {}".format(no_of_letters))
print ("The number of digits {}".format(no_of_digits))


# Program 6
print("**** Check the validity of passwords ****")
string_1 = input("Enter all your passwords: ")
words = string_1.split()
digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
alphanumeric = ['$', '#', '@']
invalid = 'N'
valid_password = []
for i in words:
    if len(i) < 6:
        invalid = 'Y'
        continue
    if len(i) > 12:
        invalid = 'Y'
        continue
    if i.islower() and i.isupper():
        pass
    if i.isalnum():
        pass
    count = 0
    for j in i:
        if j in alphanumeric:
            count = count + 1
    if count == 0:
        invalid = 'Y'
        continue
    if invalid == 'N':
        valid_password.append(i)

print(valid_password)
