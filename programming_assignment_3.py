# Program 1
print("**** Check if a number is positive negative or Zero ****")
i = int (input ("Enter a number"))
if i<0:
    print ("The number is a negative")
elif i>0:
    print ("The number is positive")
else:
    print ("The number is 0")


# Program 2
print("**** Check if a number is odd or even ****")
i = int(input("Enter a number"))
if i%2 == 0:
    print("The number is even")
else:
    print("The number is odd")


# Program 3
print("**** Check if a year is leap year ****")
y = int(input("Enter the year"))
if y%4 == 0:
    if y%100 == 0:
        if y%400 == 0 :
            print ("Its a leap year)")
        else:
            print ("Its not a leap year")
    else:
        print ("Its a leap year")
else:
    print ("Its not a leap year")


# Program 4
print("**** Check if the entered number is a prime number ****")
n = int (input("Enter a number"))
flag = 'N'
for i in range(2,n):
    if n%i == 0:
        print("NUmber is not prime")
        flag = 'N'
        break
    else:
        flag = 'Y'

if flag == 'Y':
    print ("NUmber is prime")


# Program 5
print("**** Print all prime number in the range of 1-10000 ****")
N = 10000
# check for every number from 1 to N
flag = 'N'
for i in range(1,N+1):
    flag = 'N'
    if i == 1:
        pass
    else:
        for j in range(2,i):
            if i%j == 0:
                flag = 'N'
                break
            else:
                flag = 'Y'
    if flag == 'Y':
        print (i)

