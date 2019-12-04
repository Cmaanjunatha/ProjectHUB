class employee:
    def __init__(self, id, name, age, salary):
        self.id = id
        self.name = name
        self.age = age
        self.salary = salary


e1 = employee(1,'manju', 30, 700000)
print(e1.id)
print(e1.name)
print(e1.age)
print(e1.salary)