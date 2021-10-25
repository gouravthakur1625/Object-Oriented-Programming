class Student:
    school = "St. marys's Inter College"
    def __init__(self,maths,science,sst,hindi):
        self.maths = maths
        self.science = science
        self.sst = sst
        self.hindi = hindi
    def avg(self):
        return (self.maths+self.hindi+self.science+self.sst)/4 
    def total(self):
        return (self.maths+self.hindi+self.science+self.sst) 
    @classmethod 
    def get_school(cls):
        print(cls.school)
s1 = Student(45,34,43,49)
print(s1.avg())       
print(s1.total()) 
s1.get_school()
