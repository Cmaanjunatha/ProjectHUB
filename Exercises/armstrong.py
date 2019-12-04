# To Find armstrong number
# Entering input number
num = int(input("Enter number: "))
#declaring value in variable
#for i in range(num):
temp = num
# length of n digit in range
n = len(str(num))
result = 0
while (num >0):
    digit = num % 10
    result = result + digit**n
    temp = temp//10
if temp == result:
    print(temp)


