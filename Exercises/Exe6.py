#Febinacci sequence:

n = 10
n0 = 0
n1 = 1
count = 0
if n <= 0:
    print("Enter +ve number: ")
elif n == 1:
    print("Enter the febinacci sequence upto : ",n,":")
else:
    print("Numbers in the febinacci sequence upto : ",n)
    while count < n:
        print(n0, end=',')
        nth = n0+n1
        n0 = n1
        n1 = nth
        count += 1