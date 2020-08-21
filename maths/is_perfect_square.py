while True:
    number = int(input("enter number:"))
    final = []
    for i in range(number):
        if i * i == number:
            final.append(str(number)+" is a perfect square\n"+str(i)+" X "+str(i)+" = "+str(number))
            break
        elif i * i > number:
            final.append(str(number)+" is not perfect square")
            break
    if len(final) == 0:
        print(str(number)+" is not perfect square")
    else:
        print(final[0])
