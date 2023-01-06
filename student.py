class SchoolRecords:
    all_students = []
    """
    A program that creates and stores school records
    """
    def __init__(self):
        self.student_name = input("Enter Student's name: ")
        self.class_year = int(input("Enter Class Year: "))
        self.major = input("Enter Major: ")
        course = int(input("How many courses: "))
        courses = ""
        for i in range(1,course+1):
            new_course = input("Enter Course %d: "%i)
            courses += new_course
            courses += ", "
        self.courses = courses
        self.coursegrade = 0
        SchoolRecords.all_students.append(self)
    
    def __str__(self):
        #grades = {}
#Update return method for course grades       
        return "Name: %s\nYear: %d\nMajor: %s\nCourses: %s\nCourse Grades: %s\n"\
            %(self.student_name, self.class_year, self.major, self.courses, self.coursegrade)
#def all_students(self,)
        
    def set_name(self, students_name):
        self.student_name = students_name
        return self.student_name
    
    def set_year(self, year):
        self.class_year = year
        return self.class_year
    
    def set_major(self, student_major):
        self.major = student_major
        return self.major
    
    def set_course(self, student_courses):
        self.courses = student_courses
        return self.courses
    
    def set_grades(self, courses):
        print("Courses: %s"%(courses))
        print("Fill grades in order of courses, separate grades by coma(,)")
        grades = input("Enter grades: ")
        list_grades = grades.split(",")
        list_courses = courses.split(",")
        for i in range(len(list_grades)):
            print("%s: %s" %(list_courses[i], list_grades[i]))
            
        self.coursegrade = grades
        return self.coursegrade
    
    def get_name(self):
        return self.student_name
    
    def get_year(self):
        return self.class_year
    
    def get_major(self):
        return self.major
    
    def get_courses(self):
        return self.courses
    
    def get_grades(self):
        return self.coursegrade
    
def option(Choice):
    if Choice.lower() == "teacher":
        print("Pick an option")
        print("1. Enter New Student Record")
        print("2. Change Student Name")
        print("3. Change Student Class Year")
        print("4. Enter Student Grades")
        print("5. Get Student Record")
        print("0. Exit")
            
        selection = input("Your Selection: ")   
        while selection not in ['0','1', '2', '3', '4', '5']:
            selection = input("Your Selection")   
        return selection
    else:
        print("Pick an option")
        print("1. Get Student Record")
        print("2. Change Student Name")
        print("3. Change Student Class Year")
        print("4. Enter Student Grades")
        print("5. Get Student Record")
        print("0. Exit")
        
def new_record():
    record = SchoolRecords()


    #Wrte code to Validate number
    
    
if __name__ == "__main__":
    students = []
    Choice = input("Student or Teacher? ")
    Choice = Choice.lower()
    while Choice != "student" and Choice != "teacher":
       Choice = input("Student or Teacher? ")
       Choice = Choice.lower()
    
        ##Need to create a way to validate and be sure that it's a teacher
    user_option = option(Choice)
    #maxwell_account = SchoolRecords("Maxwel", 2026, "Biology", ("English, French"))
   # print(maxwell_account)
    while user_option != "0":
        if user_option == "1":
            student_file = new_record()
            students.append(student_file)
            user_option = option(Choice)
        elif user_option == "5":
            for i in students:
                re
            user_option = option(Choice)
        

        
        
         
        
        
        
        
        
    