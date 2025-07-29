
  
# students={}
def add_student():
    student_ID=(input("Enter student ID"))
    name=input("Enter student name")
    marks=(input("Enter students marks"))

    # students[student_ID]={"name":name,"marks":marks}
    student = f"Id : {student_ID}\nName:{name}\nMarks:{marks}\n"
    with open("student.txt",'a') as f:
        f.write(student) 
    
    print("Student added successfully..")

# def displayStudent():
#     for i in students:
#         print("Name : ",students[i]["name"])
#         print("Marks : ",students[i]["marks"])
#         print("Id : ",students[i]["student_ID"])


def displayStudentFromFile():
     with open("student.txt",'r') as f: 
        data = f.read()
        print(data)


while True:
    uc = int(input("1)Add Student\n2)Display Student From File\n3)Exit\nEnter Choice : "))

    if uc == 1:
        add_student()
    # elif uc==2:
        # displayStudent()
    elif uc ==2:
        displayStudentFromFile()
    elif uc==3:
        print("Thank You")
        break 
    else:
        print("Wrong input")