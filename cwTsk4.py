class Student:
    def __init__(self,name,cgpa,course_taken):
        self.name = name
        self.cgpa = cgpa
        self.courses_taken = course_taken

        if self.cgpa < 2.00:
            self.student_status = "Probation"
            if course_taken > 2:
                self.advising_status = "Denied"
                self.courses_taken = 0
                print(f"Sorry, {self.name}, you are on probation and cannot take more than 2 courses.")
            else:
                self.advising_status = "Approved"
                print(f"Study hard this time, {self.name}.")



        else:
            self.student_status = "Regular"


            if self.courses_taken < 3:
                 self.advising_status = "Denied"
                 self.courses_taken = 0
                 print(f"Hello {self.name}, You are a regular student and have to take between 3 to 5 courses.")

            else:
                self.advising_status = "Approved"
                print(f"All the best, {self.name}, for the upcoming semester.")

s1 = Student("Clark", 3.45, 4)
print(f"Name: {s1.name}\nCGPA: {s1.cgpa}\nCourses Taken: {s1.courses_taken}")
print(f"Student Status: {s1.student_status}\nAdvising Status: {s1.advising_status}")
print("--------------------------------------------------------------------------------")
s2 = Student("Barry", 1.93, 2)
print(f"Name: {s2.name}")
print(f"Student Status: {s2.student_status}\nAdvising Status: {s2.advising_status}")
print("--------------------------------------------------------------------------------")
s3 = Student("Diana", 2.91, 2)
print(f"Advising Status: {s3.advising_status}\nCourses Taken: {s3.courses_taken}")
print("--------------------------------------------------------------------------------")
s4 = Student("Bruce", 1.52, 5)
print(f"Advising Status: {s4.advising_status}\nCourses Taken: {s4.courses_taken}")

