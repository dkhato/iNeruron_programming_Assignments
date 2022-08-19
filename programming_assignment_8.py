# Program 1
print ("**** Adding two matrices ****")
import numpy as np
A = np.array([[2, 4], [5, 1]])
B = np.array([[9, 3], [3, 6]])
C = A + B      # element wise addition
print(C)

# Program 2
print ("**** Multiplying two matrices ****")
c = A*B
print (c)

# Program 3
print ("**** Transpose of a Matrix ****")
print(A.transpose())

# Program 5
print ("**** Program to remove the punctuation from a string ****")
string = input("Enter your string : ")
lst = []
str1 = " "
lst = string.split()
for i in lst:
    if i in (',', '.', ';'):
        pass
    else:
        str1 = str1 + ' ' + i

print (str1)



