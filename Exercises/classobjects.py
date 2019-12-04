class student:
    school = "govt school"
    count = 0
    def __init__(self, RegNo, Name, place):
        self.RegNo = RegNo
        self.Name = Name
        self.place = place

    count = count + 1
    def studentinfo(self):
        print("School:", student.school)
        print("RegNo: {}, Name :{}, place :{}".format(self.RegNo, self.Name, self.place))



s1 = student("123", "manju", "hulikatte")
s2 = student("124", "man", "dvg")
s1.studentinfo()
s2.studentinfo()


