#HEADING
print("=======STUDENT MANAGEMENT SYSTEM=======")
print("Welcome to Student Management System")

#defining username and passwords for the admin login
ADMIN_USERNAME="admin"
ADMIN_PASSWORD="1234"
current_student= None

students=[] #declaration of empty list for a number of students

#function for student data loading
def load_students():
    try:
        file = open("students.txt", "r")
        for line in file:
            data = line.strip().split(",")
            student = {
                "roll": int(data[0]),
                "name": data[1],
                "course": data[2],
                "marks": int(data[3]),
                "password": data[4],
            }
            students.append(student)
        file.close()
    except FileNotFoundError:
        pass
load_students()

#exception handling
def get_int(message):
    while True:
        try:
            value = int(input(message))
            return value
        except ValueError:
            print("Invalid Input! Please enter numbers only.")


#name validation
def get_name(message):
    while True:
        name = input(message).strip()

        if name == "":
            print("Name cannot be empty.")
            continue

        if not name.replace(" ", "").isalpha():
            print("Name should contain only alphabets.")
            continue

        return name


#course validation    
def get_course(message):
    while True:
        course = input(message).strip()

        if course == "":
            print("Course cannot be empty.")
            continue

        return course

#marks validation
def get_marks():
    while True:

        marks = get_int("Enter Marks: ")

        if marks < 0 or marks > 1000:
            print("Marks must be between 0 and 1000.")
        else:
            return marks


#function for admin login 
def admin_login(): 
    username=input("Enter Username: ")
    password=input("Enter password: ")
    
    if(username==ADMIN_USERNAME and password==ADMIN_PASSWORD):
        print("Login Successful\n")
        return True
    else:
        print("Access Denied\n")
        return False



#function for student login
def student_login():

    roll = get_int("Enter roll no.: ")
    password = input("Enter password: ")

    for student in students:

        if student["roll"] == roll and student["password"] == password :

            print("Login Successful\n")
            return student

    print("Invalid Roll no. or password\n")
    return False



#login page
while True:
    print("=====Login Page=====")

    print("Choose User Type:\n 1. Admin\n 2. Student")
    user=get_int("Enter your choice: ")
    print("\n\n")

    if(user==1):

        if admin_login():
            break
                
    elif(user==2):
        current_student=student_login()
        if current_student:
            break
    
    else:
        print("Invalid Option Entered. Please retry again after some time.\nThank You.")




#function for adding student details
def add_student():   
    while True:
        roll=get_int("Enter Roll no.:  ")
        if roll<=100:
            print("Roll number must be greater than 100")
            continue
        
        duplicate=False
        for student in students:
            if student["roll"]==roll:
                duplicate=True
                break
        if duplicate:
            print("Roll Number already exists!")
            continue
        
        name=get_name("Enter name: ")
        
        course=get_course("Enter course: ")
        
        marks=get_marks()
        
        password = name.lower().replace(" ", "") + str(roll)
            
        student={
            "roll": roll,
            "name": name,
            "course":course,
            "marks": marks,
            "password":password,
        }
        
        students.append(student)
        save_student()
        print("Student Added Successfully!")
        print(f"Generated Password : {password}")
    
        ch=input("Do you want to add another student?(Y/N): ")
        if(ch.lower()=="n"):
            break




#function for view student data stored 
def vs(): 
    if len(students)==0:
        print("\n No students found.\n")
        return
    
    print("\n======STUDENT RECORDS FOUND======\n")
    for student in students:
        print(f"Roll no. :{student['roll']}")
        print(f"Name :{student['name']}")
        print(f"Course :{student['course']}")
        print(f"Marks :{student['marks']}")
        print("-"*25)




#function to search student data 
def search_student():

    if len(students) == 0:
        print("\nNo students found.\n")
        return

    search_roll = get_int("Enter Roll Number to Search: ")

    found = False

    for student in students:

        if student["roll"] == search_roll:

            print("\n====== STUDENT FOUND ======\n")
            print(f"Roll No : {student['roll']}")
            print(f"Name    : {student['name']}")
            print(f"Course  : {student['course']}")
            print(f"Marks   : {student['marks']}")
            print("-" * 30)

            found = True
            break

    if found == False:
        print("\nStudent not found.\n")





#function to update details of a student
def update_student():

    if len(students) == 0:
        print("\nNo students found.\n")
        return

    roll = get_int("Enter Roll Number to Update: ")

    found = False

    for student in students:

        if student["roll"] == roll:

            print("\nCurrent Details")
            print(f"Roll No : {student['roll']}")
            print(f"Name    : {student['name']}")
            print(f"Course  : {student['course']}")
            print(f"Marks   : {student['marks']}")
            print(f"Password: {student['password']}")
            
            

            student["name"] = get_name("Enter New Name: ")
            student["course"] = get_course("Enter New Course: ")
            student["marks"] = get_marks()
            student["password"] = student["name"].lower().replace(" ", "") + str(student["roll"])
            
            save_student()
            print("New Password :", student["password"])
            print("\nStudent Updated Successfully!\n")

            found = True
            break

    if found == False:
        print("\nStudent Not Found.\n")





#function to delete student data from previous records
def delete_student():

    if len(students) == 0:
        print("\nNo students found.\n")
        return

    roll = get_int("Enter Roll Number to Delete: ")

    found = False

    for student in students:

        if student["roll"] == roll:
            choice = input("Are you sure? (Y/N): ")

            if choice.lower() != "y":
                print("Deletion Cancelled.")
                return
                        
            students.remove(student)
            save_student()
            print("\nStudent Deleted Successfully!\n")

            found = True
            break

    if found == False:
        print("\nStudent Not Found.\n")
        


        
#function to save data as .txt file               
def save_student():

    file = open("students.txt", "w")

    for student in students:

        file.write(f"{student['roll']},{student['name']},{student['course']},{student['marks']},{student['password']}\n")

    file.close()

    
    

#function to view my data
def view_my_details():

    print("\n=====MY DETAILS=====\n")

    print(f"Roll No : {current_student['roll']}")
    print(f"Name    : {current_student['name']}")
    print(f"Course  : {current_student['course']}")
    print(f"Marks   : {current_student['marks']}")

    print("-"*30)




#admin panel loop 
if(user==1):     
    while True:
        print("====Admin Panel====\n")
        print("1.Add student\n2.View student\n3.Search student\n4.Update Student\n5.Delete Student\n6.Save Student\n7.Exit\n")                      
        ac=get_int("Enter your choice: ")
        
        
        if(ac==1):
            add_student()
        
        elif(ac==2):
            vs()    
        
        elif(ac==3):
            search_student()
        
        elif(ac==4):
            update_student()
            
        elif(ac==5):
            delete_student()
            
        elif(ac==6):
            save_student()
            print("\nStudent Data Saved Successfully!\n")
            
        elif(ac==7):
            print("Thank you for using Student Management System")
            break




#student panel loop 
if (user==2):
    while True:
        
        print("====Student Panel====")

        print("1.View My Details")
        print("2.Search Student")
        print("3.Exit")

        sc = get_int("Enter your choice: ")
        
        
        if(sc==1):
            view_my_details()

        elif(sc==2):
            search_student()

        elif(sc==3):
            print("Thank you for using Student Management System")
            break
        
        else:
            print("Invalid Choice!")



