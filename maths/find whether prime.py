number = int(input("enter a number:"))
item_list = []
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
            factor_list.append(item_list[a])
        else:
            pass
print("the factors of "+str(number)+" are: "+str(factor_list))
if len(factor_list) == 2:
    print(str(number)+" is a prime number")
else:
    print(str(number)+" is not a prime number")


    
        
        
