from teacher import Teacher


class Course(Teacher):

    def __init__(self,code:str,title:str,teacher:Teacher):
        self.code=code
        self.title=title
        self.teacher=teacher

    @property
    def get_code(self):
        return self.code
    
    @get_code.setter
    def set_code(self,value):
        self._s=value
   
    @property
    def get_title(self):
        return self.title
    
    @get_title.setter
    def set_title(self,value):
        self._s=value


    def __str__(self):
        return f"{self.teacher} --> Subject: {self.title} of course code: {self.code}"
    


