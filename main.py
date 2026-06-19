#Menu Function
def menu():
    print("\n===== SMART ATTENDANCE MANAGER =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Mark Attendance")
    print("4. View Attendance")
    print("5. Exit")

#Adding Students
import csv

def add_student():
    n=int(input("Enter the Number Of Students You want To Enter : "))
    for i in range(n):
        name=input("\nEnter a name : ")
        student_id=input("\nEnter The ID : ")

        with open("students.csv","a",newline="") as file:
            writer=csv.writer(file)
            writer.writerow([student_id,name])

    print("Students Has Been Succesffully Added")

#view students
def view_students():
    try:    
        with open("students.csv", "r") as file:
            reader = csv.reader(file)

            next(reader)
            students = [row for row in reader if len(row) >= 2]
            students = [row for row in students if len(row) > 0]
            students.sort(key=lambda x: int(x[0]))

        print("\nStudent List")

        for row in students:
            print(row[0], row[1])
    except Exception as e:
        print("ERROR:",e)
        

#Mark Attendance
from datetime import date
def mark_attend():
    today=date.today()
    with open ("students.csv","r") as file:
        reader=csv.reader(file)
        next(reader)
        students = [row for row in reader if len(row) >= 2]
        for student in students:
            print(f"\n {student[1]}")
            status=input("Is The Student P/A : ")
            if status=="p":
                status="present" 
            else:
                status="Absent"
            with open ("attendance.csv","a",newline="") as att:
                writer=csv.writer(att)
                writer.writerow([student[0],today,status])
            print("\nATTENDANCE SAVED")

#view Attendance
def view_attend():
    try:
        print("\n1. View All Attendance")
        print("\n2. Search Attendance Percentage")
        choice = input("Enter Choice: ")

        if choice == "1":
            with open("attendance.csv","r") as file:
                reader=csv.reader(file)
                next(reader)
        
                print(f"\nAttendance Records")

                student = [row for row in reader if len(row) >= 3]
                student.sort(key=lambda x:int(x[0]))
                for row in student:
                    print(row)
        elif choice =="2":
            student_id=input("Enter The ID : ")
            total=0
            present=0
            with open("attendance.csv","r") as file:
                reader=csv.reader(file)
                next(reader)
                for row in reader:
                    if len(row)<3:
                        continue
                    if row[0]==student_id:
                        total+=1
                        if row[2].lower()=="Present" :
                            present+=1
                if total==0:
                    print("The id is Invalid")
                else:
                    percentage=(present/total)*100
                    print(f"\nStudent ID : {student_id}")
                    print(f"Total Classes : {total}")
                    print(f"Present Days : {present}")
                    print(f"Attendance Percentage : {percentage:.2f}%")
        else:
            print("\nINVALID CHOICE.")
    except Exception as e:
            print("ERROR:", e)


#Tells User to Enter a Choice
while(True):
    menu()
    choice=input("Enter A Choice : ")
    if choice == '1' :
        add_student();
    elif choice == '2' :
        view_students();
    elif choice == '3' :
        mark_attend();
    elif choice == '4' :
        view_attend();
    elif choice == '5':
        break
    else:
        print("\nINVALID CHOICE")

