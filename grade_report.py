
import pandas as pd
df= pd.read_csv("students.csv")
print(df)


def class_summary():
 print("==============================")
 print("STUDENTS GRADE REPORT") 
 print("==============================")
 print(f"Total students: {len(df)}")
 print(f"Average score: {df["Grade"].mean():.2f}")
 print(f"Highest score:{df["Grade"].max()}")
 print(f"Lowest score: {df["Grade"].min()}")
 passed = df[df["Grade"] >=50]
 print(f"Number of students who passed: {len(passed)}")
 passed_rate = (len(passed) / len(df)) * 100
 print(f"The percentage rate of passed students: {passed_rate:.2f}%")
 print("==============================")

class_summary()

def subject_summary():
 print("==============================")
 print("SUBJECT SUMMARY") 
 print("==============================")
 math_students = df[df["Subject"] == "Math"]
 science_students = df[df["Subject"] == "Science"]  
 print(f"Maths Average score: {math_students["Grade"].mean():.2f}")
 print(f"Science Average score: {science_students["Grade"].mean():.2f}")
 print("==============================")

subject_summary()

def save_report():
 with open("report.txt" , "w") as f:
  f.write("==============================
")
  f.write("STUDENTS GRADE REPORT
") 
  f.write("==============================
")
  f.write(f"Total students: {len(df)}
")
  f.write(f"Average score: {df["Grade"].mean():.2f}
")
  f.write(f"Highest score:{df["Grade"].max()}
")
  f.write(f"Lowest score: {df["Grade"].min()}
")
  passed = df[df["Grade"] >=50]
  f.write(f"Number of students who passed: {len(passed)}
")
  passed_rate = (len(passed) / len(df)) * 100
  f.write(f"The percentage rate of passed students: {passed_rate:.2f}%
")
  f.write("==============================
")


 print("Report saved to report.txt")
 with open("report.txt", "r") as f:
  print(f.read())

save_report()


def menu ():
 while True:
     print("
=========================")
     print("   GRADE REPORT MENU")
     print("=========================")
     print("1. View Class Summary")
     print("2. View Subject Breakdown")
     print("3. Save Report to File")
     print("4. Exit")
     print("=========================")


     try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                class_summary()
            elif choice == 2:
                subject_summary()
            elif choice == 3:
                save_report()
            elif choice == 4:
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Try again!")
     except ValueError:
            print("Please enter numbers only!")

menu()
