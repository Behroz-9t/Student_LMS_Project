from student import Student


class StudentList:
    def __init__(self):
        
        self._students=[]
        self.list_of_students = []
        

    def add_student(self,student:Student):
    
        if isinstance(student,Student):
            
            self._students.append(student)
            self.list_of_students=[str(stud) for stud in self._students]
                 
        else:
            return TypeError ("Can Only Add Students!")
        

    def remove_student(self,student:Student):

        if isinstance(student,Student):
            
            self._students.remove(student)
            self.list_of_students=[str(stud) for stud in self._students]
                 
        else:
            return TypeError ("Can Only Remove Students!")

    @property  
    def get_student(self):
        return f"------All the Enrolled Students' List------\n\n{self.list_of_students}\n"


    def search_by_name(self,key:str):
        
       
        found_students = [student for student in self._students if student.name == key]
        
        if found_students:
            print(f"\nFound results based on name {key}: {len(found_students)} \n\n")
            for student in found_students:
                print(student)
                     
        else:
            print(f"\nNo student found with the same name:'{key}'\n")


    def search_by_seat(self,key):

        found_seat=[student for student in self._students if student.seat_number == key]
        
        if found_seat:
            print(f"\nFound results based on seat number {key}: {len(found_seat)} \n\n")
            for student in found_seat:
                print(student)

        else:
            print(f"\nNo student found with the same seat number:'{key}'\n")    
    
    
    def search_by_semester(self,key):

        found_semester=[student for student in self._students if student.semester == key]
        
        if found_semester:
            print(f"\nFound results based on semester {key}: {len(found_semester)} \n\n")
            for student in found_semester:
                print(student)

        else:
            print(f"\nNo student found with the same semester:'{key}'\n")    


    def __str__(self):
        
        # return "\n".join(str(student) for student in self._students)
        return f"\n{self.list_of_students}\n"




