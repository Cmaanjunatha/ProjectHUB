class person:
    ct = 0
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        person.ct = person.ct + 1

    def showinfo(self):
        print("name: {}, gender: {}".format(self.name, self.gender))
    @classmethod
    def showcount(cls):
        print("No of objects are created: {}".format(cls.ct))


class account(person):
        def __init__(self, job, balance  ):
            self.job = job
            self.balance = balance

p1 = person('ani','male')
p2 = person('akki','male')
a = account('engineer','5000')
p2.showinfo()
a.showinfo()




p1 = person('ani','Male')
p2 = person('akki','Male')
p3 = person('rek','Female')
p1.showinfo()
person.showcount()