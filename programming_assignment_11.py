# Program 1
print ("**** Program to find words which are greater than given length K ****")
string = input("Enter your string : ")
num = int(input("Enter the length of words that you want to find greater than : "))
lst = string.split()
for i in lst:
    if len(i) >= num:
        print (i)


# Program 2
print ("**** remove the ith Char from a string ****")
string = input("Enter your string : ")
n = int(input("Enter the index of string which needs to be removed : "))
str1 = " "
for i in range (len(string)):
    if i != n:
        str1 = str1 + string[i]

print ("The string after removing the {}th char from the string ".format(n) + " " + str1)

# Program 3
print("**** Split a single string into two or split a string of words and join them. ****")

string_strings = input("Do you want to enter a single string or multiple words : String/Strings ? ")

if string_strings == "String":
    string = input("Enter your string : ")
    num = int(input("Enter the index in which you want to split : "))
    str1,str2 = string[:num], string[num:]
    print ("After splitting the string : ", str1, str2)

else:
    strings = input("Enter your string of words : ")
    inte = int(input ("Enter the index you want to split at : "))
    lst = strings.split()
    lst1 = []
    lst2 = []
    for i in range(len(lst)):
        if i >= inte:
            lst2 = lst[inte:]
        else:
            lst1 = lst[:inte]
    str1 = ' '.join(lst1)
    str2 = ' '.join(lst2)
    print ("The strings/list of words after splitting are as follows")
    print ("First String")
    print (str1)
    print("Second String")
    print(str2)


# Program 4
print ("**** Check if a given string is binary or not ****")
string = input ("Enter your string : ")
flag = ' '
for i in string:
    if i not in ['0','1']:
        flag = 'N'
        break
    else:
        flag = 'Y'

if flag == 'Y':
    print ("The string is binary")
else:
    print ("the string is not binary")


# Program 5
print ("**** print the common words from two strings ****")
str1 = input ("Enter string 1 : ")
str2 = input ("Enter string 2 : ")
lst1 = str1.split()
lst2 = str2.split()
lst3 = []
lst4 = []
for i in lst1:
    if i in lst2:
        lst3.append(i)
    else:
        lst4.append(i)

print ("The common words between two strings are : ",lst3)
print ("The uncommon words between two strings are : ",lst4)


# Program 6
print ("**** Check if any duplicate characters in a string ****")

string = input("Enter your string : ")
lst = []
lst1=[]
for i in string:
    if i not in lst:
        lst.append(i)
    else:
        if i not in lst1:
            lst1.append(i)


print("Duplicated characters in the string : ", lst1)


# Program 7
print ("**** Check if any duplicate characters in a string ****")

string = input("Enter your string : ")
lst = ['!','@','#','$','%','^','&','*','(',')']
for i in string:
    if i in lst:
        print (i)



