from course import Course
from teacher import Teacher
from person import Person
from course_list import CourseList

class Student(Person):

    def __init__(self,name:str,seat_number:int,semester:int,courses:CourseList):
        super().__init__(name)
        self.seat_number=seat_number
        self.semester= semester 
        self.courses=courses

    @property
    def get_seat(self):
        return self.seat_number
    
    @get_seat.setter
    def set_seat(self,value):
        self._s=value

    @property
    def get_semester(self):
        return self.semester
    
    @get_semester.setter
    def set_semester(self,value):
        self._s=value

    
    
    # def __str__(self):
    #     return f"{self.name} of {self.seat_number} and {self.semester} "


    def __str__(self):
        
        return f"{super().__str__()} of seat number: {self.seat_number} of semester: {self.semester} has courses --> {self.courses}"
    






