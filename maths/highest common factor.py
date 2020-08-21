def highest_common_factor(number1,number2):
   item_list = []
   item_list2 = []
   multiplication_list = []
   multiplication_list2 = []
   factor_list = []
   factor_list2 = []
   common_factor_list = []
   for i in range(number1 + 1):
       if i == 0:
           pass
       else:
           item_list.append(i)
   length = len(item_list) + 1
   for i in range(len(item_list)):
       length -= 1
       for a in range(len(item_list)):
           if item_list[a] * length == number1:
               multiplication_list.append(str(item_list[a])+" X "+str(length)+" = "+str(number1))
               factor_list.append(item_list[a])
   for i in range(number2 + 1):
       if i == 0:
           pass
       else:
           item_list2.append(i)
   length = len(item_list2) + 1
   for i in range(len(item_list2)):
       length -= 1
       for a in range(len(item_list2)):
           if item_list2[a] * length == number2:
               multiplication_list2.append(str(item_list2[a])+" X "+str(length)+" = "+str(number2))
               factor_list2.append(item_list2[a])
   if len(factor_list) > len(factor_list2):
       main = factor_list.copy()
       other = factor_list2.copy()
   elif len(factor_list) < len(factor_list2):
       main = factor_list2.copy()
       other = factor_list.copy()
   else:
       main = factor_list2.copy()
       other = factor_list.copy()
   for i in range(len(other)):
      if main.count(other[i]) != 0:
         common_factor_list.append(other[i])
   if len(common_factor_list) == 1:
      return common_factor_list[0]
   else:
      return max(common_factor_list)
highest_common_factor(33,111)
         
      
      
   
  

