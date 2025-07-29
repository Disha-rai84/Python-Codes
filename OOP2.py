class Employe:
    
    Name= "Trisha"
    Salary= "95k"
    Education=(" Masters in Engineering")

    def __init__(self,Name,Salary,Education):
        self.Name = Name
        self.Salary=Salary
        self.Education=Education
        print("Student Added Successfully")

    def addDetails(self,Name,Salary,Education):
        self.Name = Name
        self.Salary=Salary
        self.Education=Education
    def showDetails(self):
        print(" Name :",self.Name)
        print("Salary :",self.Salary)
        print("Education :",self.Education)
        
E1 = Employe("Trisha","95k","software Engineering")
# E1.addDetails("Trisha","95k","software Engineering")
E1.showDetails()
print("---------------------------------------------")
E2 = Employe("Jhon","90k", "Hardware Engineering")
# E1.addDetails("Jhon","90k", "Hardware Engineering")
E2.showDetails()













        
      