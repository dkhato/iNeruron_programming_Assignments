# Program 1
print("**** Printing the factorial of a number ****")
n = int(input("Enter the number you want the factorial for :"))
t = 1
for i in range(1,n+1):
    j = i;
    t = t*i

print(t)

# Program 2
print("**** Displaying the multiplication table of a number ****")
n = int(input("Enter the number you want table for :"))
for i in range (1, 11):
    j = n*i
    print("{} * {}".format(n,i) + "=" + str(j))

# Program 3
print("**** Check if a number is a Armstrong number ****")
n = input ("Enter the number you want to check")
x = len(n)
y = 0
for i in n:
    temp = int(i)**x
    y = y + temp

if y == int(n):
    print ("Its an Armstrong number")
else:
    print("Oops its not")


# Program 4
print("**** Check if a number is Armstrong number in an interval ****")
proceed = 'Y'
numlst = []
while proceed == 'Y':
    start = int(input("Enter the Start of Interval : "))
    end = int(input("Enter the End of Interval : "))
    if end <= start:
        print("Invalid Interval, please try again")
        proceed = input("Do you want to Proceed ?")
        if proceed == 'Y':
            continue
        else:
            print("Thank you !!")
            proceed = 'N'
    else:
        for i in range (start,end+1):
            numlst.append(i)
            proceed = 'N'

# Check which numbers are armstrong by reading each one from the list.
armstronglist = []
for i in numlst:
    i = str(i)
    x = len(i)
    y = 0
    for j in i:
        temp = int(j) ** x
        y = y + temp
    if y == int(i):
        armstronglist.append(int(i))


print ("The following are the armstrong number list : ")
for i in armstronglist:
    print (i)


# Program 5
print("**** Addition of a N numbers ****")
n = int (input("Enter the number of elements to be added"))
temp = 0
for i in range (1, n+1):
    temp = temp + i

print (temp)