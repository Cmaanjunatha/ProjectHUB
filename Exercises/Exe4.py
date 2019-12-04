with open("test.txt") as countletter:
    count = 0
    text = countletter.read()
    for char in text:
        if char.isupper():
            count+=1
print(count)