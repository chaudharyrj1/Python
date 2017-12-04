from StudentSchedular import StudentSchedular
class Client:
    flag=0
    studentSchedular=StudentSchedular()
    def test(self):
        while(self.flag==0):
            str=input("\n\n1. Add Student\n2. Add Batch\n3. Add Faculty\n4. Add Courses\n5. View Reports \n6. Exit\n")
            if(str=="1"):
                self.addStudent()
            elif(str=="2"):
                self.addBatch()
            elif (str == "3"):
                self.addFaculty()
            elif (str == "4"):
                self.addCourse()
            elif (str == "5"):
                choice=input("1. Display Students\n2. Display Batches\n3. Display Faculties\n4. Display Courses\n5. Display Student Details by Roll No\n6. Display Batch Details by Batch ID")
                if(choice=="1"):
                    self.displayStudents()
                elif(choice=="2"):
                    self.displayBatches()
                elif(choice=="3"):
                    self.displayFaculties()
                elif(choice=="4"):
                    self.displayCourses()
                elif(choice=="5"):
                    rollno=input("Enter Roll Number: ")
                    self.displayStudentDetailsByRollNo(rollno)
                elif(choice=="6"):
                    id=input("Enter ID: ")
                    self.displayBatchDetailsByID(id)
                else:
                    print("Please Choose Valid Option")
            elif(str=="6"):
                break;
            else:
                print("\nPlease Enter Valid Input\n")

    def addStudent(self):
        courses=[]
        print("Enter Student Details:")
        rollno = input("Enter Roll No.:")
        if(self.studentSchedular.getStudentsByRollNo(rollno) is None):
            name = input("Enter Name:")
            courseNumber=int(input("Enter no of Courses:"))
            for i in range(courseNumber):
                course=input("Enter course: ")
                courses.append(course)
            self.studentSchedular.addStudent(rollno, name,courses)
        else:
            print("Roll No already exists")

    def displayStudents(self):
        count = 1
        students = self.studentSchedular.showAllStudents()
        if(students==[]):
            print("\nNo Student Available ")
        else:
            for student in students:
                print("\nStudent ", count, "Details:")
                print("Roll Number: ", student.getRollNo())
                print("Name: ", student.getName())
                print("Courses: ", student.getCourses())
                count += 1

    def addBatch(self):
        students=[]
        print("Enter Batch Details:")
        ID = input("Enter ID.:")
        course = input("Enter Course:")
        faculty=input("Enter Faculty Name:")
        studentNo=int(input("Enter no of students in batches:"))
        for i in range(studentNo):
            rollno=input("Enter roll no of student in batch:")
            student=self.studentSchedular.getStudentsByRollNo(rollno)
            students.append(student)
        self.studentSchedular.addBatch(ID,course,faculty,students)

    def displayBatches(self):
        count=1
        if(self.studentSchedular.showAllBatches()==[]):
            print("\nNo Batch Available ")
        else:
            for batch in self.studentSchedular.showAllBatches():
                print("\nBatch ",count,"Details:")
                print("Batch ID: ",batch.getID())
                print("Course: ",batch.getCourse())
                print("Faculty: ",batch.getFaculty())
                students=batch.getStudents()
                print("Students:")
                for student in students:
                    print("Roll No: ",student.getRollNo(),"    Name: ",student.getName())
                count+=1

    def addFaculty(self):
        print("Enter Faculty Details: ")
        id=input("Enter Id: ")
        name=input("Enter Name: ")
        course=input("Enter Course: ")
        self.studentSchedular.addFaculty(id,name,course)

    def addCourse(self):
        course=input("Enter Course Name: ")
        self.studentSchedular.addBatch(course)

    def displayFaculties(self):
        print("Faculty List: ")
        count=1;
        if(self.studentSchedular.showAllFaculties()==[]):
            print("\nNo Faculty Available")
        else:
            for faculty in self.studentSchedular.showAllFaculties():
                print("Faculty ",count," Details: ")
                print("ID: ",faculty.getID(),"  Name: ",faculty.getName(),"  Course: ",faculty.getCourse())
                count+=1

    def displayCourses(self):
        print("Course List: ")
        if(self.studentSchedular.showAllCourses()==[]):
            print("\nNo Courses Available")
        else:
            for course in self.studentSchedular.showAllCourses():
                print(course.getCourse())

    def displayBatchDetailsByID(self,id):
        batch=self.studentSchedular.getBatchDetailsByBatchID(id)
        print("Batch Details for ID ",id,": ")
        if(batch is None):
            print("No batch available for this ID ")
        else:
            print("Course: ", batch.getCourse())
            print("Faculty: ", batch.getFaculty())
            students = batch.getStudents()
            print("Students:")
            for student in students:
                print("Roll No: ", student.getRollNo(), "    Name: ", student.getName())

    def displayStudentDetailsByRollNo(self,rollno):
        student=self.studentSchedular.getStudentsByRollNo(rollno)
        print("Student Details for Roll No ",rollno,": ")
        if(student is None):
            print("No student Available for this Roll Number")
        else:
            print("Name: ", student.getName())
            print("Courses: ", student.getCourses())

client=Client()
client.test()