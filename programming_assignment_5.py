# Program 1
print("**** Find the LCM of two numbers ****")
num1 = int(input("Enter first number : "))
num2 = int(input("Enter first number : "))
if num1 > num2:
    greater = num1
else:
    greater = num2

while True:
    if ((greater % num1 == 0) and (greater % num2 == 0)):
        lcm = greater
        break
    greater += 1
print(lcm)


# Program 2
print("**** Find the HCF of two numbers ****")
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
if num1 > num2:
    smaller = num2
else:
    smaller = num1
for i in range(1, smaller+1):
    if((num1 % i == 0) and (num2 % i == 0)):
        hcf = i

print(hcf)


# Program 3
print("**** Python Program to Convert Decimal to Binary, Octal and Hexadecimal ****")
# Convert Decimal to Binary
num = int (input("Enter the number you want to convert to Binary, Octal and Hexadecimal"))
num1 = num
n = num
rlst = []
q = 1
while q != 0:
    q = n//2
    r = n%2
    n = q
    rlst.append(r)

rlst.reverse()
str1 = ' '
for i in rlst:
    str1 = str1 + str(i)

print("The binary for {}".format(num1) + " " "is",  int(str1))
rlst.clear()

# Convert Decimal to Octal

q = 1;
n = num
while q != 0:
    q = n//8
    r = n%8
    n = q
    rlst.append(r)
rlst.reverse()
str1 = ' '
for i in rlst:
    str1 = str1 + str(i)

print("The Octal for {}".format(num1) + " " "is",  int(str1))
rlst.clear()

# Convert Decimal to Hexadecimal

q = 1;
n = num
while q != 0:
    q = n//16
    r = n%16
    n = q
    rlst.append(r)
rlst.reverse()
str1 = ' '
for i in rlst:
    str1 = str1 + str(i)

print("The Hexadecimal for {}".format(num1) + " " "is",  int(str1))


# Program 4
print("**** Find the ascii value of a character ****")
char1 = input("Enter the character you want to find the ASCII value of : ")
print(ord(char1))


# Program 5
print("**** Python calculator with 4 basic ops ****")


# This function adds two numbers
def add(x, y):
    return x + y


# This function subtracts two numbers
def subtract(x, y):
    return x - y


# This function multiplies two numbers
def multiply(x, y):
    return x * y


# This function divides two numbers
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break

    else:
        print("Invalid Input")

