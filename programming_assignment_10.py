# Program 1
print("**** Sum of the elements of the list ****")
num = int(input("Enter the number of elements in the list : "))
lst = []
for i in range(0, num):
    ele = int(input("Enter you list element : "))
    lst.append(ele)
sum= 0
for i in lst:
    sum = sum +i

print ("The sum of the elements in the list is :", sum)


# Program 2
print ("**** Multiplication of the elements of the list ****")
num = int (input("Enter the number of elements in the list : "))
lst = []
for i in range(0,num):
    ele = int(input("Enter you list element : "))
    lst.append(ele)
mul= 1
for i in lst:
    mul = mul*i

print ("The multiplication of the elements of the list is :", mul)


# Program 3
print ("**** Find the smallest element in a list ****")
num = int (input("Enter the number of elements in the list : "))
lst = []
for i in range(0,num):
    ele = int(input("Enter you list element : "))
    lst.append(ele)

firsttime = 'Y'
for i in lst:
    if firsttime == 'Y':
        temp = i
        firsttime = 'N'
    else:
        if i < temp:
            temp = i
        else:
            continue

print("The smallest element in the list is : ",temp)


# Program 4
print ("**** Find the largest element in a list ****")
num = int (input("Enter the number of elements in the list : "))
lst = []
for i in range(0,num):
    ele = int(input("Enter you list element : "))
    lst.append(ele)

print("The largest element in the list is : ", max(lst))


# Program 5
print ("**** second Largest number in a list ****")
num = int (input("Enter the number of elements in the list : "))
lst = []
for i in range(0,num):
    ele = int(input("Enter you list element : "))
    lst.append(ele)

lst.sort()
lst.reverse()
for i in lst:
    if lst.index(i) == 1:
        second_largest = i
        break

print ("The second largest number is : ", second_largest)


# Program 6
print ("**** N Largest element in a list ****")
num = int (input("Enter the number of elements in the list : "))
lst = []
for i in range(0,num):
    ele = int(input("Enter you list element : "))
    lst.append(ele)

lst.sort()
lst.reverse()
n = int (input("Enter the number of Largest numbers to be retrieved : "))
lst1 = lst[0:n:1]
print ("The {} largest number in the list is ".format(n))
print (lst1)


# Program 7
print ("**** Print even numbers in a list ****")
num = int (input("Enter the number of elements in the list : "))
lst = []
for i in range(0,num):
    ele = int(input("Enter you list element : "))
    lst.append(ele)

for i in lst:
    if i%2 == 0:
        print (i)
    else:
        continue


# Program 8
print ("**** Print odd numbers in a list ****")
num = int (input("Enter the number of elements in the list : "))
lst = []
for i in range(0,num):
    ele = int(input("Enter you list element : "))
    lst.append(ele)

for i in lst:
    if i%2 == 0:
        continue
    else:
        print (i)


# Program 9
print ("**** Remove empty list from a list ****")
def empty_list_remove(input_list):
    new_list = []
    for ele in input_list:
        if ele:
            new_list.append(ele)
    return new_list

# input list values
input_list = [5, 6, [], 3, [], [], 9]
print(f"The original list is : {input_list}")
print(f"List after empty list removal : {empty_list_remove(input_list)}")

# Program 10
import copy
print ("**** Cloning or copying a list ****")
num = int (input("Enter the number of elements in the list : "))
lst = []
for i in range(0,num):
    ele = int(input("Enter you list element : "))
    lst.append(ele)

lst1 = copy.copy(lst)
print (lst1)


# Program 11
print ("**** Count the occurrences of an element in a list ****")
num = int (input("Enter the number of elements in the list : "))
lst = []
for i in range(0,num):
    ele = input("Enter you list element : ")
    lst.append(ele)

n = input("Enter the element you want to know the count : ")
count = 0
for i in lst:
    if i == n:
        count = count+1

print ("The occurrences of {} is ".format(n) + " " + str(count))
