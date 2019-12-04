list2 = [41, 44, 47, 48, 50]


'''
# lambda function
even_no = list(filter(lambda x: (x % 2 == 0), list2))

print(even_no, end=" ")


# list compression
even = [num for num in list2 if num % 2 == 0]

print(even)

# while loop
num = 0
while num < len(list2):
    if num % 2 == 0:
        print(list2[num], end=" ")
    num += 1

'''

for num in list2:
    if num % 2 == 0:
        print(num, end=" ")
