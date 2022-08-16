# Program 1
print("**** Display fibonacci using recursion ****")


def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return recur_fibo(n - 1) + recur_fibo(n - 2)


nterms = int(input("Enter the number you want to see the series for : "))

# check if the number of terms is valid
if nterms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(nterms):
        print(recur_fibo(i))


# Program 2
print("**** Calculate the factorial of a number using Recursion ****")
def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n * recur_factorial(n - 1)
num = int (input("Enter the number : "))
# check if the number is negative
if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of", num, "is", recur_factorial(num))


# Program 3
print ("**** Calculate the BMI ****")
weight = int (input("Enter your weight"))
height = float (input("Enter your height in mts"))
print ("Your BMI is : " , (weight/height**2)*100)


# Program 4
print ("**** Program to calculate the natural Log of a number ****")
import math
num = int (input("Enter the number you want to calculate the Log"))
print (math.log(num))


# Program 5
print ("**** Calculate the cube of N natural numbers ****")
num = int (input ("Enter the N natural numbers : "))
sum = 0
for i in range (1, num+1):
    sum = sum + (i*i*i)

print ("The cube of {} natural numbers is".format(str(num)) + " " + str(sum))

