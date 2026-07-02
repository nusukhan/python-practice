# using getters & setters in python 
## getter
### getter are functions used to retrieve the data attributes of a class
### function hote hai jo kisi class ke  data attribute ko get krne ke lye use hote hai 
## settters
### setter are functions used to assign or modify the data attribute of a class
### ( kisi bhe class ke data ko set krne ke lye   use hote hu yne ase data attributte jo koi value assign krne ke lye use hu )
# jab hum kisi class main private data declare data memeber  to tab hum uska ak getters & setters bhe bana dete hai 
class student:
    @property
    def grade (self):
        return self.__grade
    def __init__(self,name,grade):
        self.__grade = grade
    def get_grade(self): # garde ko return kr de ga   
        return self.__grade
    def set_grade(self,grade): # or setter ka name set grade hu ga  jis ke andr hum ak garde recieve kre g as input or usko apne private dada member ko assign kr de g 
        if 0 <= grade <= 100:
            self.garde__grade = grade
        else:
            print("invalid grade")

student = student("ali", 90)
student.set_grade(95)
print(student.get_grade())

