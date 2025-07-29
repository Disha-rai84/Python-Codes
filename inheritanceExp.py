# class Animal:  
#     def speak(self):  
#         print("Animal Speaking")  
# #child class Dog inherits the base class Animal  
# class Dog(Animal):  
#     def bark(self):  
#         print("dog barking")  
# d = Dog()  
# d.bark()  
# d.speak()  




# class A:
#     def __printMsg(self):
#         print("A Class")

# class B(A):
#     def printMsg(self):
#         print("B Class")

# class C:
#     def __printMsg(self):
#         print("C Class")
# class D(B,C):
#      def __printMsg(self):
#         print("D Class")


# d1 = D()
# d1.printMsg()

# class Animal:  
#     def speak(self):  
#         print("Animal Speaking")  
 
# class Dog(Animal):  
#     def bark(self):  
#         print("dog barking")  
 
# class DogChild(Dog):  
#     def eat(self):  
#         print("Eating bread...")  
# d = DogChild()  
# d.bark()  
# d.speak()  
# d.eat()  




class Students:
    def speak(self):
        print(" The students are speaking")
class Girl(Students):
    def talking(self):
        print(" The girl is talking ")     
class Kids(Girl,Students):
    def eat(self):
        print(" The kids are eating ")  

k= Kids()
k.speak()
k.talking()
k.eat()


print(Kids.__bases__)



