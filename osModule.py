import os

# # os.rename("try.txt","newRenamed.txt")


# # os.mkdir("Folder")










# path=os.getcwd()+"\Folder"

# print(os.listdir(path))


# def main():  
#     i = 0  
#     os.chdir("Folder")
#     path=os.getcwd()+"\\"
#     for filename in os.listdir(path):  
#         destination = "new" + str(i) + ".png"  
#         source = path + filename  
#         destination = path + destination  
#         os.rename(source, destination)  
#         i += 1  
  
# if __name__ == '__main__':  
#     main()  

# os.chdir("Folder")
# f = open("abc.txt","x")

# # os.rmdir("Folder")
# temperatures=[10,-20,-289,100]    
# def c_to_f(c):    
#     if c< -273.15:    
#         return "That temperature doesn't make sense!"    
#     else:    
#         f=c*9/5+32    
#         return f    
# for t in temperatures:    
#     print(c_to_f(t))  

with open("SMS2.py",'r') as f:    
    content = f.read();    
    print(content)   

