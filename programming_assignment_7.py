import array as arr
from array import *
# Program 1
print ("**** Sum of the elements of an array ****")
length = int(input("Enter the number of elements in your array"))
a = array('i')
for i in range(0, length):
    n = int(input("Enter next value"))
    a.append(n)

sum = 0
for i in (a):
    sum = sum + i
print ("The Sum of all elements of the array is : ", sum)


# Program 2
print("**** The largest element in an array ****")
max = 0
for i in (a):
    if i>max:
        max = i

print("The largest element is : ", max)


# Program 3
print ("**** Function for array rotation ****")
b = array('i')
for i in ((len(a))-1, 1, 0):
    b.append(a[i])

print ("The reversed array : ")
for j in b:
    print(j)


# Program 4
print("**** Program to split the array and add the first part to the end ****")
num = int (input("Enter the number of elements in the array : "))
lst =[]
for i in range(0,num):
    lst.append(int(input("Enter your value")))
print ("The original list : ", lst)

# Split the array
(mid) = num/2
lst1 = lst[:int(mid)]
lst2 = lst[int(mid):]

sum1 = 0
for i in lst1:
    sum1 = sum1 + i

sum2 =  0
for i in lst2:
    sum2 = sum2 + i

print ("The lists are split into :",lst1, lst2)
print ("The sum of First part and second part of the list is : ", sum1+sum2)


# Program 5
print("**** Check if the array is monotonic ****")
num = int (input("Enter the number of elements in the array : "))
lst =[]
for i in range(0,num):
    lst.append(int(input("Enter your value")))

m_i = 'N'
m_d = 'N'
for j in range(len(lst)-1):
    value1 = lst[j]
    value2 = lst[j+1]
    if value1 < value2:
        m_i = 'Y'
    else:
        m_i = 'N'
        break

for j in range(len(lst)-1):
    value1 = lst[j]
    value2 = lst[j + 1]
    if value1 > value2:
        m_d = 'Y'
    else:
        m_d = 'N'
        break

if m_i == 'Y' and m_d == 'N':
    print ("Its a monotone increasing")
elif m_i == 'N' and m_d == 'Y':
    print("Its a monotone decreasing")
else:
    print ("Its a mix!!")





