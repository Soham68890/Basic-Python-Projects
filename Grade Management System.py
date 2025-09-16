#Student Grade Management System

print("Welcome to Student Grade Management System")
student_details = {

}  

no_of_students = 0

def grades(marks):
        if marks > 80:
            return "A"
        elif marks > 60:
            return "B"
        elif marks > 40:
            return "C"
        elif marks > 20:
            return "D"
        else:
            return "E"

 
while True:
    print("1. Add Student\n2. Remove Student\n3. Update Student Marks\n4. View Student\n5. Exit ")
    choice = (input("Enter your choice: "))
    if choice == "1":
        new_student = input("Enter name of student: ")
        student_marks = int(input("Enter Student's Marks: "))
        grade = grades(student_marks)
            
        no_of_students += 1
        
        student_details.update({new_student: {"Marks" : student_marks, "Grade" : grade}})
        print(f"Student {new_student} has been added with grade {grade}")
    
    elif choice == "2":
        
        while True:
            remove_student = input("Enter Student name to be removed: ")
        
            if remove_student in student_details:
                del student_details[remove_student]
                print(f"Student {remove_student} has been removed")
                break
            else:
                print(f"Student named {remove_student} is not present.\nTry again with a valid name")
                continue
            

    elif choice == "3":
        
        while True:
            update_student = input("Enter student name to be updated: ")
            new_marks = int(input("Enter new marks of student: "))
            if update_student in student_details:
                student_details[update_student]["Marks"] = new_marks
                new_grade = grades(new_marks)
                student_details[update_student]["Grade"] = new_grade
                print(f"{update_student}'s marks has been updated and grade has been changed to {new_grade}")
                break
            else:
                print("PLEASE ENTER A VALID NAME!")
                continue

    elif choice == "4":
        if len(student_details) == 0:
            print("No student has been added")
        else:    
            print(student_details)

    elif choice == "5":
        break

    else:
        print("Invalid input. Try choosing 1-5")
        continue
        

        


    
