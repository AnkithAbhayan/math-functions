from math import *
import time
number = int(input("enter a number:"))
print("\n" * 1)
item_list = []
multiplication_list = []
factor_list = []
for i in range(number + 1):
    if i == 0:
        pass
    else:
        item_list.append(i)
length = len(item_list) + 1
for i in range(len(item_list)):
    length -= 1
    for a in range(len(item_list)):
        if item_list[a] * length == number:
            multiplication_list.append(str(item_list[a])+" X "+str(length)+" = "+str(number))
            factor_list.append(item_list[a])
        else:
            pass
for letter in multiplication_list:
    print(letter)
print("\n" * 2)
print("the factors of "+str(number)+" are: "+str(factor_list))


    
        
        
