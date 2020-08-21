number = int(input("enter number:"))
perfect_square_list = []
nearest_perfect_square = []
multiplication_values = []
for i in range(number):
    answer = i * i
    perfect_square_list.append(answer)
    multiplication_values.append(str(i)+" X "+str(i)+" = "+str(answer))
    if answer > number:
        break
if len(perfect_square_list) == 1:
    nearest_perfect_square = perfect_square_list.copy()
    nearest_perfect_square.append(multiplication_values[0])
if number in perfect_square_list:
    num = perfect_square_list.index(number)
    perfect_square_list.remove(number)
    del multiplication_values[num]
for i in range(len(perfect_square_list)):
    if len(perfect_square_list) == 2:
        break
    else:
        del perfect_square_list[0]
        del multiplication_values[0]
if perfect_square_list[0] < number:
    if number - perfect_square_list[0] < perfect_square_list[1] - answer:
        nearest_perfect_square.append(perfect_square_list[1])
    else:
        nearest_perfect_square.append(perfect_square_list[0]) 
elif perfect_square_list[0] > number:
    if perfect_square_list[0] - number > number - perfect_square_list[1]:
        nearest_perfect_square.append(perfect_square_list[1])
    else:
        nearest_perfect_square.append(perfect_square_list[0])
print(nearest_perfect_square[0])
print(multiplication_values[0])
    
        
    
