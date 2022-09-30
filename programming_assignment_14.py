# Program 1
print("**** with a generator function iterate through numbers in a given range and print 7 divisible ****")


def test(x, y):
    for i in range(x, y + 1):
        if i % 7 == 0:
            yield i


num1 = int(input("Enter the First num : "))
num2 = int(input("Enter the Second num : "))

for i in test(num1, num2):
    print(i)

# Program 2
print("**** Count the frequency of words ****")

string_1 = input("Enter your String : ")

words = string_1.split()
words = sorted(words)
dict_1 = {}
for i in words:
    if i in dict_1:
        dict_1[i] += 1
    else:
        dict_1[i] = 1

for key, value in dict_1.items():
    print(key, value)

# Program 3
print("**** Class person and deriving subclasses male and female ****")


class person:
    gender = " "

    def get_gender(self, gender):
        self.gender = gender
        print(self.gender)


class male(person):
    def get_gender(self, gender):
        self.gender = gender
        print(self.gender)


class female(person):
    def get_gender(self, gender):
        self.gender = gender
        print(self.gender)


obj1 = person()
obj2 = male()
obj2.get_gender("Male")
obj3 = female()
obj3.get_gender("Female")

# Program 6
print("**** Binary search to find the index of a desired element ****")


def binary_search(num_list, num1):
    low = 0
    high = len(num_list) - 1
    mid = 0
    while low <= high:
        mid = (low + high) // 2
        if num_list[mid] < num1:
            low = mid + 1
        elif num_list[mid] > num1:
            high = mid - 1
        else:
            return mid

    return -1


num = int(input("Enter the length of your list : "))
num_list = []

for i in range(0, num):
    num_list.append(int(input("Enter your number : ")))

num1 = int(input("Enter the element you want the index : "))

result = binary_search(num_list, num1)
print("The index of the element {}".format(num1) + " " + "is" + " " + str(result))

# Program 5
import sys
import zlib

print("**** Compress and decompress a string ****")
string = "hello world!hello world!hello world!hello world!"

print("The size of the original string ", sys.getsizeof(string))
compressed = zlib.compress(string.encode())
csize = sys.getsizeof(compressed)
print("The size of the compressed string : ", csize)
