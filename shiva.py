class student:
    def readstudentdata(self):
        print("id of current object=",id(self))
        self.stno=int(input("Enter Student Number"))
        self.sname=input("Enter Student Name")
        self.marks=float(input("Enter Student Marks"))
    def dispstudentdata(self):
        print("id of current object",id(self))
        print("Student Number={}".format(self.stno))
        print("Student Name={}".format(self.sname))
        print("Student Marks={}".format(self.marks))
s1=student()
s2=student()
print("First student data")
print("id of s1 in main program:",id(s1))
s1.readstudentdata()

print("Second Student data")
print("id of s2 in main program:",id(s2))
s2.readstudentdata()

print("content of s1")
print("id of s1 in main program:",id(s1))
s1.dispstudentdata()
print("content of s2")
print("id of s2 in main program:",id(s2))
s2.dispstudentdata()


