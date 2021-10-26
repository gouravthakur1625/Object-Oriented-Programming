class Student:
    def __init__(self,name,rollno,std):
        self.name = name
        self.rollno = rollno
        self.std = std
        self.lap = self.Laptop()
    def information(self):
        print(f'The name of Student is {self.name} study in class {self.std} and his roll no. is {self.rollno} ')
    class Laptop:
        def __init__(self):
            self.model = 'HP'
            self.ram = 8
            self.memory = 256 
        def infolap(self):    
            print(f'The model is {self.model} with {self.ram} GB ram and {self.memory} GB SSD')
s1 = Student('Gourav',13,12)
s1.lap.infolap()