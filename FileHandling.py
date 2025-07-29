# f = open("one.txt","r")
# # f.write("HI One.txt")


# print(f.read())


# f.close()

# f.read()


# a = float(input("enter the value of a : "))
# b = float(input("enter the value of b : "))
# c = float(input("enter the value of c : "))
 
# s = ( a + b + c ) / 2

# area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
# print(' the area of the trinagle is %0.2f' %area)

# def=trinagle_area(base,h)


# with open("one.txt","r") as f:
#     print(f.read(5))

# # print(f.read())

# A = ["Hello\n", "Coders\n", "JavaTpoint\n"]  
# f1 = open('one.txt', 'w')  
# f1.writelines(A) 

# f1 = open('one.txt', 'r')  
# Lines = f1.read()  
# count = 0  
# for line in Lines:  
#     count += 1  
#     print("Line{}: {}".format(count, line.strip()))  







f = open("try.txt","r")


print("The filepointer is at byte :",f.tell())    

f.seek(3)
    
#reading the content of the file    
print("After reading, the filepointer is at:",f.tell())    
content = f.read();    
print("After reading, the filepointer is at:",f.tell())    
    
#after the read operation file pointer modifies. tell() returns the location of the f.     
    