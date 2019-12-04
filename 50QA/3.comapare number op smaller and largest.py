print("enter 'x' for exit")
print("enter any two numbers : ")

num1 = input()
if num1 == 'x':
    exit()
else:
    num2 = input()
    number1 = int(num1)
    number2 = int(num2)
    count = 0
    if number1 > number2:
        large_number = number1
        count = 1
    elif number1 < number2:
        large_number = number2
        count = 1
    else:
        print("\n both number are equal to each other")
    if count == 1:
        print("\n Large number : ", large_number)


