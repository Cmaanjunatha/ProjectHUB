String =input("Enter input: ")
count_lower = 0
count_upper = 0
for i in String:
    if (i.isupper()):
        count_upper+=1
    if i.islower():
        count_lower+=1

print(count_upper)
print(count_lower)