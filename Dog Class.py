class Dog():
    '''A Simple attempt to model a dog.'''
    def __init__ (self,name,age):
        '''Initialize the name and age and other stuff'''
        self.name = name
        self.age = age
    def get_up (self):
        '''Simulate a dog get up in rasponse to command.'''
        print(f'Hey! {self.name} get up ')
    def sit(self):
        '''Command to sit '''
        print(f'{self.name} sit here.')
    def find_age (self):
        '''To find age of dog given by user'''
        print(f'{self.name} is {self.age} years old')
        
my_dog=Dog('Tommy',10)
my_dog.sit()
my_dog.find_age()