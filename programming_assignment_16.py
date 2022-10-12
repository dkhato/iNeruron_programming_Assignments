# Program 2
import math


def radians_to_degrees(x):
    return (180 / math.pi) * x


radian = int(input("Enter your degree in Radians : "))
print (radians_to_degrees(radian))

# Program 3
print("**** Check if a number is a curzon number *****")


def is_curzon(x):
    num1 = 2 ** x + 1
    num2 = 2 * x + 1
    if num1 % num2 == 0:
        return True
    else:
        return False


num = int(input("Enter the number : "))
result = is_curzon(num)
if result:
    print("number is curzon")
else:
    print("number is not curzon")


# Program 4
import math

print("**** Area of Hexagon ****")


def area(x):
    return ((3 * math.sqrt(3)) * (x ** 2)) / 2


side = int(input("Enter the side : "))
are_a = area(side)
print ("The area of hexgon is :", round(are_a, 1))


# Program 5
print("**** Convert base 10 decimal to base 10 binary ****")


def binary(x, lst):
    q = x
    while q != 1:
        q, r = divmod(q, 2)
        lst.append(r)

    lst.append(1)
    return lst


lst = []
num = int(input("Enter the base 10 decimal number : "))
binary(num, lst)
lst.reverse()
str1 = ' '
for i in lst:
    str1 = str1 + str(i)

print ("Afet conversion : ", str1)
