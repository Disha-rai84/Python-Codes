class Student:
    id=101
    name="user"

    def addDetails(self,id,name):
        self.id = id
        self.name=name
    def showDetails(self):
        print("Id :",self.id)
        print("Name :",self.name)

s1 = Student()
s1.addDetails(1001,"Jhon")
s1.showDetails()

s2 = Student()
s2.addDetails(1002,"Jane")
s2.showDetails()


print("hi")
