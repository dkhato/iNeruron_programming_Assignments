# Program 1
print("**** Take a range of numbers and list out divisible numbers ****")


def list_operation(x, y, z):
    lst = []
    for i in range(x, y+1):
        if i % z == 0:
            lst.append(i)
    return lst


start = int(input("Enter the start : "))
end = int(input("Enter the end : "))
div = int(input("Enter the number to be checked for divisibility : "))

lst = []
lst = list_operation(start, end, div)

print(lst)


# Program 2
print("**** Compare twp lists to check if one follows the other ****")

num = int(input("Enter the number of elements in your list : "))

lst1 = []
lst2 = []

print("Adding elements in the first list : ")
for i in range(0, num):
    x = int(input())
    lst1.append(x)

print("Adding elements in the Second list : ")
for i in range(0, num):
    x = int(input())
    lst2.append(x)

print (lst1, lst2)

flag = 'N'
for i in range(len(lst1)):
    if i == 0:
        pass
    else:
        for j in range(len(lst2)):
            if j == 0:
                pass
            else:
                if lst2[j] + 1 == lst1[i]:
                    flag = 'Y'
                else:
                    flag = 'N'

if flag == 'Y':
    print("True")


# Program 3
print ("**** Create a secret Society name with name from friends ****")

num = int(input("Enter the number of friends :"))

lst = []
for i in range(0, num):
    x = input()
    lst.append(x)

lst2 = []
for i in lst:
    for j in i:
        lst2.append(j)
        break

lst2.sort()

str1 = ""
print ("The name of the secret society is : ", str1.join(lst2))



# Program 4
print("**** Determine Duplicates in a string ****")


def is_isogram(x):
    lst = []
    first_time = 'Y'
    counter = 0
    for i in x:
        if first_time == 'Y':
            lst.append(i)
            first_time = 'N'
        else:
            if i in lst:
                counter = counter + 1
                break
            else:
                lst.append(i)
    if counter >= 1:
        return False
    else:
        return True


string_1 = input("Enter your string : ")

print(is_isogram(string_1))


# Program 5
print("**** If string in Alphabetical order return true or else return False ****")


def is_in_order(x):
    lst1 = sorted(x)
    print (lst1)
    lst2 = []
    for i in x:
        lst2.append(i)
    if lst1==lst2:
        return True
    else:
        return False



string_1 = input("Enter your string : ")

result = is_in_order(string_1)

print (result)



