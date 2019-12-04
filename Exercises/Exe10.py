#armstrong

x = int(input("Enter input:"))
for i in range(x):
    num=i
    n=len(str(i))
    armstrong=0
    while(i>0):
        d = i % 10
        armstrong = armstrong+d**n
        i = i//10
    if num == armstrong:
        print(num, "number is armstrong")
    else:
        print(num, "number is not armstrong")
