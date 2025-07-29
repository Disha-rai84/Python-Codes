import time

students={}
id = 100

def addStudent():
    global id
    id+=1
    students[id]={}
    students[id]['name']=input("Enter Name :")
    students[id]['marks']=input("Enter Marks :")
    print("Student with id {} added Successfully...\n".format(id))

def updateStudent():
    student = int(input("Enter Id :"))
    choice = int(input("Press 1 for Name Update\nPress 2 for Marks\nEnter YOUR CHOICE: "))
    if choice ==1:
        students[student]['name']=input("Enter Updated Name :")
    elif choice == 2:
        students[student]['marks']=input("Enter Updated Marks :")
    else:
        print("Invalid Choice please add again !")

def deleteStudent():
    student = int(input("Enter Id :"))
    print("Are you really want to delete student with id {}?".format(student))
    choice = int(input("Press 1 If Yes\nPress 2 If No\nEnter YOUR CHOICE: "))
    if choice ==1:
        del students[student]
    elif choice == 2:
        print("Student Deletion cancelled ..")
    else:
        print("Invalid Choice Try Again !")
def viewStudents():
    print("Students:")
    for i in students:
        print("-----------------------------")
        print("Name : ",students[i]['name'])
        print("Marks : ",students[i]['marks'])

def viewStudent():
    student = int(input("Enter Id :"))
    print("-----------------------------")
    print("Name : ",students[student]['name'])
    print("Marks : ",students[student]['marks'])



print("\t\t\t*** Student Management System ***")
time.sleep(2)

while True:
    user_choice = int(input("1)Add a new Student\n2)Update Existing Student\nDelete Existing Student\n4)View Single Student\n5)View All Students\n6)Exit\nEnter Your Choice :"))
    if(user_choice == 1):
        addStudent()
    elif(user_choice==2):
        updateStudent()
    elif (user_choice==3):
        deleteStudent()
    elif(user_choice==4):
        viewStudent()
    elif(user_choice==5):
        viewStudents()
    else:
        print("Thank you for using")
        time.sleep(2)
        break