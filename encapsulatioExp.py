# class Parent:
#     _data=10
    
    
    
#     def printData(self):
#         print("Data(Parent)  :",self._data)

# class Child(Parent):
#     def printData(self):
#         print("Data(Child)  :",self._data)
#         super().printData()
#     pass
# p = Parent()
# c = Child()
# # 
# # p.printData()
# c.printData()


class Example:  
  # show() method with two arguments  
  def show(self, a, b):  
    print(f"Two arguments: {a}, {b}")  
  
  # show() method with single argument  
  def show(self, a):  
    print(f"Single argument: {a}")  
  

# instantiating the class  
obj = Example()  
# calling the method  
obj.show(5,10)  
