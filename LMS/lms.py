from student_list import StudentList
from course_list import CourseList
from student import Student
from teacher import Teacher
from course import Course


class LMS(Student):

    def __init__(self):

        self.studentlist=StudentList()
        self.courselist=CourseList()


    def app(self):
        
        Humera=Teacher("Mis Humera",2121)
        Bari=Teacher("Sir Bari",1122)
        Mariam=Teacher("Mis Mariam",1212)
        Huzaifa=Teacher("Huzaifa",1221)
        

        oop=Course("CS-352","Object Oriented Programming",Humera)
        dld=Course("CS-354","Digital Logic Design",Bari)
        ds=Course("CS-358","Discrete Structure",Mariam)
        la=Course("CS-356","linear Algebra",Huzaifa)
        

        self.courselist.add_course(oop)
        self.courselist.add_course(dld)
        self.courselist.add_course(la)
        self.courselist.add_course(ds)

        self.courselist.remove_course(ds)

        self.courselist.search_by_title("linear Algebra")


        b=Student("Behroz",37,1,self.courselist)
        a=Student("Ali",77,1,self.courselist)        
        am=Student("Asim",38,1,self.courselist)
        f=Student("Faiq",39,1,self.courselist)
        h=Student("Ahmed",40,1,self.courselist)   
        

        self.studentlist.add_student(b)
        self.studentlist.add_student(a)
        self.studentlist.add_student(h)
        self.studentlist.add_student(f)
        self.studentlist.add_student(am)

        self.studentlist.remove_student(am)

        self.studentlist.search_by_name("Behroz")
        self.studentlist.search_by_seat(77)
        self.studentlist.search_by_semester(1)
        self.studentlist.search_by_semester(2)

    
    @property
    def show_all_students(self):
        
        print(f"{self.studentlist.get_student}")
    
    @property
    def show_all_courses(self):
        
        print(f"{self.courselist.get_course}")







