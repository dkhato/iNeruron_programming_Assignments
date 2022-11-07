# Program 1
print("**** Take out integers and put in a list from a list of strings and integers ****")


def filter_list(x):
    lst2 = []
    for i in x:
        if i.isdigit():
            lst2.append(i)
    return lst2


num = int(input("Enter the number of elements in your list : "))
lst = []
for i in range(0, num):
    x = input("Enter your list element : ")
    lst.append(x)

lst1 = []
lst1 = filter_list(lst)

print(lst1)


# Program 2
print("**** Add Indexes to the elements in the list ****")


def add_indexes(x):
    lst1 = []
    for i in range(len(x)):
        lst1.append(x[i] + i)
    return lst1


num = int(input("Enter the number of elements in your list : "))
lst = []
for i in range(0, num):
    x = int(input("Enter your list element : "))
    lst.append(x)


lst1 = add_indexes(lst)

print(lst1)


# Program 3
import math

pi = math.pi
print("**** Cone volume ****")


def volume_cone(r, h):
    return (1 / 3) * pi * r * r * h


radius = int(input("Enter the radius : "))
height = int(input("Enter the height : "))

print("The volume of the cone is : ", round (volume_cone(radius, height),2))


# Program 4
print("**** Find the number of dots in a Triangular number sequence ****")


def triangle(x):
    return (x * (x + 1)) / 2


num = int(input("Enter your number : "))

no_of_dots = triangle(num)

print("The number of dots : ", int(no_of_dots))


