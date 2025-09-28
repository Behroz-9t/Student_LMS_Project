from course import Course
from teacher import Teacher


class CourseList:
    def __init__(self):
        self._courses=[]
        self.list_of_courses=[]

    def add_course(self,course:Course):

        if isinstance(course,Course):
            self._courses.append(course)
            self.list_of_courses=[str(course) for course in self._courses]

        else:
            return TypeError("\nCan only add courses!")


    def remove_course(self,course:Course):

        if isinstance(course,Course):
            
            self._courses.remove(course)
            self.list_of_courses=[str(course) for course in self._courses]
                 
        else:
            return TypeError ("\nCan Only Remove courses!")
        

    @property  
    def get_course(self):
        return f"------Course List------\n\n{self.list_of_courses}\n"


    def search_by_title(self,key):

        found_course=[course for course in self._courses if course.title == key]
        
        if found_course:
            print(f"\nFound results based on title {key}: {len(found_course)}\n\n")
            for i in found_course:
                print(i)

        else:
            print(f"\nNo courses found with the same name:'{key}'\n")

    def __str__(self):

        return f"{self.list_of_courses}"
    
# c=CourseList()

# Humera=Teacher("Mis Humera",2121)
# Bari=Teacher("Sir Bari",1122)
# Mariam=Teacher("Mis Mariam",1212)
# Huzaifa=Teacher("Huzaifa",1221)
        

# oop=Course("CS-352","Object Oriented Programming",Humera)
# dld=Course("CS-354","Digital Logic Design",Bari)
# ds=Course("CS-358","Discrete Structure",Mariam)
# la=Course("CS-356","linear Algebra",Huzaifa)


# c.add_course(oop)
# c.add_course(dld)
# c.add_course(la)
# c.add_course(ds)

# print(c.get_course)




