# Program 1
print("**** Add one element to the list and remove the first element ****")


def next_in_line(x, y):
    x.append(y)
    for i in x:
        x.remove(i)
        break
    return x


num = int(input("Enter the number of elements in your list : "))
lst = []
for i in range(0, num):
    x = int(input("Enter the element"))
    lst.append(x)

print("The current list :", lst)

num1 = int(input("Enter the element you want to eliminate : "))

lst = next_in_line(lst, num1)

print ("List after adding an element and removing the 1st element : ", lst)

# Program 2
print("**** Create the function that takes a list of dictionaries and returns the sum of people&#39;s budgets.: ")


empl = {}
num = int(input("Enter the number of employees : "))

for i in range(0,num):
    name = input("Enter the employee name : ")
    sal = int(input("Enter emp sal: "))
    empl[name] = sal

sum_sal = 0
for i, k in empl.items():
    sum_sal = sum_sal + k


print ("The salary for all the employee : ",sum_sal)


# Program 3
print("**** Arrange a given string in alphabetical order ****")


def alphabet_soup(x):
    return ''.join(sorted(x))


string = input("Enter your string : ")

print("After arranging in alphabetic order ", alphabet_soup(string))



# Program 5
print("**** Only return integers ****")


def return_ony_integer(lst):
    result_lst = []
    for i in lst:
        if i.isnumeric():
            result_lst.append(i)
    return result_lst


num = int(input("Enter the number of elements in your list : "))
lst = []
for i in range(0, num):
    x = input("Enter the element")
    lst.append(x)

lst1 = []
lst1 = return_ony_integer(lst)

print("The list with only integers ", lst1)


