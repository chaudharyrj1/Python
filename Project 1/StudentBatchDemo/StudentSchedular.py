from Student import Student
from Batch import Batch
from Faculty import Faculty
from Course import Course
class StudentSchedular:
    students=[]
    batches=[]
    faculties=[]
    courses=[]

    def addStudent(self,rollno,name,courses):
        student=Student()
        student.setName(name)
        student.setRollNo(rollno)
        student.setCourses(courses)
        self.students.append(student)

    def showAllStudents(self):
        return self.students

    def addBatch(self,ID,course,faculty,students):
        batch=Batch()
        batch.setID(ID)
        batch.setCourse(course)
        batch.setFaculty(faculty)
        batch.setStudents(students)
        self.batches.append(batch)

    def showAllBatches(self):
        return self.batches

    def addCourse(self,course):
        cou=Course()
        cou.setCourse(course)
        self.courses.append(cou)

    def showAllCourses(self):
        return self.courses

    def addFaculty(self,id,name,course):
        faculty=Faculty()
        faculty.setID(id)
        faculty.setName(name)
        faculty.setCourse(course)
        self.faculties.append(faculty)

    def showAllFaculties(self):
        return self.faculties

    def getBatchDetailsByBatchID(self,batchId):
        flag=0
        for batch in self.batches:
            if(batch.getID()==batchId):
                flag=1
                return batch
        if(flag==0):
                return None

    def getStudentsByRollNo(self,rollno):
        flag = 0
        for student in self.students:
            if (student.getRollNo() == rollno):
                flag = 1
                return student
        if (flag == 0):
            return None

