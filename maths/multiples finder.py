def finder():
    while True:
        number = int(input("enter number: "))
        for i in range(11):
            answer = number * i
            print(str(number)+(" x ")+str(i)+str(" = ")+str(answer))
    finder()
finder()
