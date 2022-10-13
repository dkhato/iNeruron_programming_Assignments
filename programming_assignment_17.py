# Program 1
print("**** Cretae a function to evenly divide a range of numbers by a third number ****")


def evenly_divide(a, b, c):
    lst = []
    sum = 0
    for i in range(a, b + 1):
        if i % c == 0:
            lst.append(i)
    for i in lst:
        sum = sum + i
    return sum


num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
num3 = int(input("Enter the number to be divided evenly :"))
result = evenly_divide(num1, num2, num3)
print('The sum is : ', result)

# Program 3
print("**** Create a function to replace all vowels in a string with a character *****")
string = input("Enter your string : ")
vowels = ['a', 'e', 'i', 'o', 'u']
str1 = ''
for i in string:
    if i in vowels:
        str1 = str1 + '#'
    else:
        str1 = str1 + i

print(str1)


# Program 4
def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n * recur_factorial(n - 1)


num = int(input("Enter your number :"))

# check if the number is negative
if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of", num, "is", recur_factorial(num))

# Program 5
print("**** Calculate the hamming distance ****")

string_1 = input("Enter your first string : ")
string_2 = input("Enter your second string : ")
counter = 0
if len(string_1) != len(string_2):
    print("Hamming distance can be calculated only for equal length strings")

for i in range(len(string_1)):
    for j in range(len(string_2)):
        if i == j:
            if string_1[i] == string_2[j]:
                continue
            else:
                counter = counter + 1
        else:
            continue

print("The hamming distance is :", counter)
