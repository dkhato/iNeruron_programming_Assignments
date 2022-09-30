# Program 1
print("**** with a generator function iterate through numbers in a given range and print 7 divisible ****")


def test(x, y):
    for i in range(x, y + 1):
        if i % 7 == 0 and i % 5 == 0:
            yield i


num1 = 0
num2 = int(input("Enter the number : "))

for i in test(num1, num2):
    print(i)


# Program 2
print("**** Print even numbers within a given range using generators  ****")


def test(x, y):
    for i in range(x, y + 1):
        if i % 2 == 0:
            yield i


num1 = 0
num2 = int(input("Enter the number : "))

for i in test(num1, num2):
    print(i)


# Program 3
print("**** Print fibonacci using list comprehension ****")

n = int (input("Enter the number in console : "))
mylist = [0,1]
[mylist.append(mylist[-2] + mylist[-1]) for n in range(n)]

str1 = " "
for i in mylist:
    str1 = str1 + str(i) + ","

print (str1)


# Program 4
print ("**** Print user name from the email address ****")
email_username = input("Enter your email address : ")
username = " "
for i in email_username:
    if i == '@':
        break
    else:
        username = username + i

print (username)


# Program 5
print("**** Class shape and subclass square class ****")


class shape:
    def area(self, length):
        return length ** 2


class square(shape):
    def __init__(self, length):
        self.length = length


length = int(input("Enter the length: "))
obj = square(length)
area = obj.area(length)
print(area)
