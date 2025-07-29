class A:
    def __init__(self):
        print("Hello")




a1 = A()
a2 = A()

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print("name:",self.name)
        print("age:",self.age)

p1=person("Disha",17)    
p1.show()    

