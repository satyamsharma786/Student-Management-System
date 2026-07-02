#HEADING
print("=======STUDENT MANAGEMENT SYSTEM=======")
print("Welcome to Student Management System")


#login page
while True:
    print("=====Login Page=====")

    print("Choose User Type:\n 1. Admin\n 2. Student")
    user=int(input("Enter your choice: "))
    print("\n\n")

    if(user==1):   
        print("====Admin Panel====\n")
        print("1.Add student\n2.View student\n3.Search student\n4.Update Student\n5.Delete Student\n6.Save Student\n7.Exit\n")                      #admin panel menu 
        ac=int(input("Enter your choice: "))                                                                                                        #admin panel option choice
        print("\n")
        break
        
        
        
    elif(user==2):
        print("====Student Panel====\n")
        print("1.View my details\n2.Search student\n3.Exit\n")           #student panel menu 
        sc=int(input("Enter your choice: "))                             #student panel choice input 
        print("\n")
        break
    
    else:
        print("Invalid Option Entered. Please retry again after some time.\nThank You.")


students=[] #declaration of empty list for a number of students


def add_student():          #function for adding student details
    while True:
        roll=int(input("Enter Roll no.:  "))
        name=input("Enter name: ")
        course=input("Enter course: ")
        marks=int(input("Enter marks: "))
        
            
        student={
            "roll": roll,
            "name": name,
            "course":course,
            "marks": marks,
        }
        
        students.append(student)
        print("Studdent Added Successfully!")
        print(students)
        
        ch=input("Do you want to add another student?(Y/N): ")
        if(ch.lower()=="n"):
            break
        
        
while True:
    print("====Admin Panel====\n")
    print("1.Add student\n2.View student\n3.Search student\n4.Update Student\n5.Delete Student\n6.Save Student\n7.Exit\n")                      #admin panel menu 
    ac=int(input("Enter your choice: "))
    
    
    if(ac==1):
        add_student()
        
    elif(ac==7):
        break

