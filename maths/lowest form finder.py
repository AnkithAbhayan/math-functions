from time import sleep
while True:
    final_nums = []
    numerator = int(input("enter numerator: "))
    denominator = int(input("enter denominator: "))
    print("processing:")
    if numerator > denominator:
        num = denominator
    elif denominator > numerator:
        num = numerator
    elif denominator == numerator:
        num = numerator
    for i in range(num + 1):
        if i == 0 or i == 1:
            pass
        else:
            lower1 = numerator / i
            lower2 = denominator / i
            if len(str(lower1)) <= len(str(numerator)) + 2 and len(str(lower2)) <= len(str(denominator)) + 2:
                lower1 = str(lower1)
                lower2 = str(lower2)
                if int(lower1[-1]) == 0 and int(lower2[-1]) == 0:
                   final_nums.append("dividing numerator and denominator by "+str(i) + "  " + str(lower1)+"/"+str(lower2))
                else:
                    pass
    for i in range(len(final_nums)):
        if i == len(final_nums) - 1:
            print("\n")
            print("lowest form:")
            print(final_nums[i])
        else:
            print(final_nums[i])
    if len(final_nums) == 0:
        print(str(numerator) + " and " + str(denominator) + " are in the lowest form")
        


        

    
            
        
            
