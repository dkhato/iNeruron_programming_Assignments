# Program 1
print ("**** Check if a number is a Disarium number ****")
proceed = 'Y'
while proceed != 'N':
    num = input("Enter your Number : ")
    num_digits = len(num)
    str1 = " "
    sum = 0
    for i in range(1,num_digits+1):
        str1 = num[i-1:i:1]
        n = int(str1)
        n = n**i
        sum = sum + n

    if sum == int (num):
        print ("Its a Disarium Number !! would you like to try again : (Y/N) ? ")
        proceed = input()

    else:
        print ("Oops it not a Disarium Number, would you like to try again : (Y/N) ? ")
        proceed = input()


# Program 2
print ("**** Print all the Disarium Numbers between a given interval ****")
start = int (input("Enter the start of the interval :"))
end = int (input("Enter the end of the interval :"))
lst = []
for i in range (start,end+1):
    converted_i = str(i)
    num_digits = len(converted_i)
    str1 = " "
    sum = 0
    for j in range(1, num_digits + 1):
        str1 = converted_i[j - 1:j:1]
        n = int(str1)
        n = n ** j
        sum = sum + n

    if sum == int(converted_i):
        lst.append(i)

print ("The list of all Disarium numbers between {} and {} is ".format(start,end))
print (lst)


# Program 3
print ("**** Check if a number is a Happy number ****")
num = input("Enter the number you want to check :")
if len(num) < 2:
    print ("Enter at least a 2 digit number")
num1 = num
sum = 0
lst = []
firsttime = 'Y'
while sum != 1:
    if firsttime == 'Y':
       for i in num1:
           sum = sum + (int(i)) ** 2
           firsttime = 'N'
       lst.append(sum)
    else:
        sum1 = 0
        sum_flag = 'N'
        length_flag = 'N'
        for i in str(sum):
            sum1 = sum1 + (int(i)) ** 2
            sum = sum1
        s = len(str(sum))
        if sum in lst:
            sum_flag = 'Y'
            break
        elif s < 2 and sum != 1:
            length_flag = 'Y'
            break
        else:
            lst.append(sum)

if sum_flag == 'Y' and length_flag == 'N':
    print ("Its not a Happy number sum has started repeating !!")
elif sum_flag == 'N' and length_flag == 'Y':
    print("Its not a Happy number as the sum is reduced to single digit.  !!")
else:
    print ("Its a Happy number!!")


print ("The list of sum of all consecutive numbers ", lst)


# Program 4
print ("**** Print all happy numbers between a given interval ****")
start = int (input("Enter the start of the interval : "))
end = int (input("Enter the end of the interval : "))
lst1 = []
for i in range(start,end+1):
    num1 = i
    sum = 0
    lst = []
    firsttime = 'Y'
    while sum != 1:
        if firsttime == 'Y':
            converted_num1 = str(num1)
            for j in converted_num1:
                sum = sum + (int(j)) ** 2
                firsttime = 'N'
            lst.append(sum)
        else:
            sum1 = 0
            sum_flag = 'N'
            length_flag = 'N'
            for j in str(sum):
                sum1 = sum1 + (int(j)) ** 2
                sum = sum1
            s = len(str(sum))
            if sum in lst:
                sum_flag = 'Y'
                break
            elif s < 2 and sum != 1:
                length_flag = 'Y'
                break
            else:
                lst.append(sum)

    if sum == 1:
        lst1.append(i)

print ("The happy numbers between {} and {}".format (start,end))
print (lst1)


# Program 5
print ("**** Check if a number is a Harshad number ****")
num = input("Enter the number you want to check : ")
sum = 0
for i in num:
    sum = sum + int (i)

if int(num)%sum == 0:
    print ("Its a Harshad number !!")
else:
    print ("Its not a Harshad number")


# Program6
def isPronicNumber(num):
    flag = False;

    for j in range(1, num + 1):
        # Checks for pronic number by multiplying consecutive numbers
        if ((j * (j + 1)) == num):
            flag = True;
            break;
    return flag;


# Displays pronic numbers between 1 and 100
print("Pronic numbers between 1 and 100: ");
for i in range(1, 101):
    if (isPronicNumber(i)):
        print(i),
        print(" "),    