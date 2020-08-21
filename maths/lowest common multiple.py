import time
number1 = int(input("enter first number:"))
number2 = int(input("enter second number:"))
if number1 > number2:
    big_num = number1
    small_num = number2
elif number2 > number1:
    big_num = number2
    small_num = number1
lcm_not_found = True
a = 2
i = 2
lcm = []
test_small_num = small_num
test_big_num = big_num
while lcm_not_found:
    if test_small_num < test_big_num:
        test_small_num = small_num * i
        i += 1
    elif test_small_num == test_big_num:
        i -= 1
        lcm.append("the lowest common multiple is "+str(test_small_num))
        lcm.append(""+str(small_num)+" X "+str(i)+" is "+str(test_small_num))
        lcm.append(""+str(big_num)+" X "+str(a)+" is "+str(test_small_num))
        lcm_not_found = False
    elif test_small_num > test_big_num:
        while test_small_num > test_big_num:
            test_big_num = big_num * a
            a += 1
for i in range(len(lcm)):
    print(lcm[i])
    
