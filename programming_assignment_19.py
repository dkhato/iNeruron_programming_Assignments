# Program 1
print("**** Printing each letter of the string twice ****")

string_1 = input("Enter your string : ")

str1 = ' '

for i in string_1:
    str1 = str1 + i * 2

print("The string after repeating each character ", str1)

# Program 2
print("**** Reverse a Boolean expression, if any other value entered then return Boolean Expected ****")


def reverse(string1):
    if string1 == 'True' or string1 == 'true':
        return False
    else:
        return True


lst = ['True', 'true', 'false', 'False']

conti = 'Y'
while conti == 'Y':
    string_1 = input("Enter the boolean string that you want to reverse : ")

    if string_1 in lst:
        print(reverse(string_1))
        conti = input("Do you want to continue ? ")
    else:
        conti = input("Boolean Expected !!!, Wanna try again ? ")

print("Okay Bye!!")


# Program 3
print ("**** The thickness of a folded paper ****")


def num_layers(n):
    thickness = 0.5
    for i in range(n):
        thickness = thickness*2

    return str(thickness / 1000) + 'm'  # for meters


print(num_layers(1))
print(num_layers(4))
print(num_layers(21))


# Program 4
print("**** Index of caps **** ")


def index_of_caps(x):
    lst = []
    for i in range(len(x)):
        if x[i].isupper():
            lst.append(i)
    return lst


string = input("Enter your String :")

index = index_of_caps(string)

print("The indexes of all caps are : ", index)


# Program 5
print("**** Using list comprehensions find all even numbers from 1 to n **** ")


def find_even_numbers(x):
    lst1 = [i for i in range(1,x+1) if i % 2 == 0]
    return lst1


num = int(input("Enter the range of numbers N :"))
lst = []
lst = find_even_numbers(num)
print (lst)