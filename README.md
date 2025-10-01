# Student_LMS_Project

Student LMS Project
 The focus is on developing and refactoring a Student LMS project, involving several Python
 files related to students, courses, teachers, and lists. The work includes defining classes
 and methods for managing students, courses, and teachers, as well as implementing functionalities
 for adding, removing, and searching for students and courses.

 Key Activities & Code Modifications

 • student.py include a Student class inheriting from a Person class, with attributes like
 student_id and a CourseList object for managing enrolled courses.
 • Implemented get_seat , set_seat , get_semester , set_semester methods in the Student
 class.
 • Created Course class in course.py with attributes for code, title, and teacher
 , including getter and setter methods for code and title.
 • Developed CourseList class in course_list.py
 to manage list of courses, including methods to add_course, remove_course, and
 search_by_title.
 • Developed StudentList class in student_list.py
 to manage a list of students, including methods to add_student, remove_student
 , and search by name, seat, or semester.
 • Modified lms.py to include classes for Student, StudentList, Course, CourseList, and
 Teacher, with methods for adding, removing, and searching students and courses.
 • Implemented an app method within the LMS
 class to initialize teachers and courses, add them to course lists, and add students to 
 student lists. The
 app method also includes calls to remove_course, search_by_title, remove_by_name
 , and search_by_seat.
 • main function in lms.py to instantiate the LMS class and call the app method

### **Classes and Relationships**
- **Person**
  - (Base class, likely with attributes like name, email, etc.)
- **Student** (inherits from Person)
  - Attributes: seat_number, semester, courses (CourseList)
  - Methods:  get_seat, set_seat, get_semester, set_semester,  **str**()
- **Teacher** (inherits from Person )
  - Attributes: name, id
  - Methods: **str**()
- **Course**
  - Attributes: code, title, teacher (Teacher)
  - Methods: get_code, set_code, get_title, set_title, **str**()
- **CourseList**
  - Attributes: courses (list of Course)
  - Methods: add_course(), remove_course(), search_by_title(), get_course,**str**()
- **StudentList**
  - Attributes: students (list of Student)
  - Methods: add_student(), remove_student(), search_by_name(), search_by_seat(), search_by_semester(), get_student(),**str**()
- **LMS**
  - Attributes: studentlist (StudentList), courselist (CourseList)
  - Methods: app(), show_all_students, show_all_courses
- **main**
  - Function: main() (instantiates LMS and runs app)
### **Relationships**
- Student *has a* CourseList
- Course *has a* Teacher
- CourseList *contains* Course
- StudentList *contains* Student
- LMS *has a* StudentList and CourseList
