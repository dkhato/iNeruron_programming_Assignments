# Program 1
print("**** Converting Kilometer to miles****")

k = int(input("Enter the number of Kms to be converted to miles"))
m = k/1.609
print(m)

# Program 2
print("**** Converting celsius to fahrenheit****")
c = int(input("Enter the celsius to be converted into Fahrenheit"))
f = (c*1.8)+32
print (f)

# Program 3
print("**** Displaying a calender****")
import calendar
yy = 2022
mm = 8
print(calendar.month(yy, mm))
print(calendar.calendar(yy))

# Program 4
print("**** Solving a Quadratic Equation****")
import math


def equationroots(a, b, c):
    # calculating discriminant using formula
    dis = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(dis))

    # checking condition for discriminant
    if dis > 0:
        print(" real and different roots ")
        print((-b + sqrt_val) / (2 * a))
        print((-b - sqrt_val) / (2 * a))

    elif dis == 0:
        print(" real and same roots")
        print(-b / (2 * a))

        # when discriminant is less than 0
    else:
        print("Complex Roots")
        print(- b / (2 * a), " + i", sqrt_val)
        print(- b / (2 * a), " - i", sqrt_val)


a = 1
b = 10
c = 22

# If a is 0, then incorrect equation
if a == 0:
    print("Input correct quadratic equation")

else:
    equationroots(a, b, c)


# Program 5
print("****Swapping two numbers without using third variable****")
x = 5
y = 6
print ("Before swapping:")
print("Value of x : ", x, " and y : ", y)
x, y = y, x
print("After Swapping")
print("Value of x : ", x, " and y : ", y)
