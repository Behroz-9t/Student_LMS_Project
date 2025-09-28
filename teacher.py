from person import Person

class Teacher(Person):

    def __init__(self, name,id):
        super().__init__(name)
        self.id=id

    def __str__(self):
        return f"{super().__str__()} of id: {self.id}"
    


        