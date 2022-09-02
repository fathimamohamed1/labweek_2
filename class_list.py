

from dataclasses import dataclass

@dataclass
 # changed from a student class to a dataclass 
class Student:
    name: str
    school_id: str
    gpa:float

    def __str__(self): # using the self string method to filter , override and customize the generated fields however you like it 
      return f'Name {self.name},GPA: {self.gpa}' 
    
    #creating a main method
def main():

    mary = Student('Mary','bwhyv2',4.5)
    print(mary)          

                
    hannah = Student('Hannah','iyrvcks',2.5)
    print(hannah)

main() #calling the method



# The dataclass version is better than the traditional version because this allows the use of float in the method , it looks alot neater and simpler too. id definetely use the dataclass versions when using any 
# data that has number like prices or numbers. 
