# object attribute & methods 
class student:

    def __init__(self,name,age,grade):
         self.name = name  # is main hamre  pass 3 instance varible hai name ,age ,grade) or ye hume kase pata chle ga self. se 
         self.age = age # 3 he hamre pass instance method hai  one is contractor and 2 is normal display or is eligible or hume kase pata chala ahi ye instance method hai kyu ke phla argumnet self se pass howa hai wo object hai jis pr ye method call hu ga 
         self.garde = grade   
    def display_info(self):
         print(f"student Name:{self.name}") 
         print(f"age:{self.age}") 
         print(f"grade:{self.grade}") 
    def is_eligible(self):  
     if self.age>= 15:
              print(self.name,"is eligible for admission.")
     else:
            print(self.name,"is not eligible for admission")
 # creating objects
student1 = student ("ali",16,"10th")
student2 = student("sara",14,"8th")
 # accessing aatributes          
print(student1.name) #  inke andr attribute set kr rhe hai 
print(student2.grade) # instance method ke zarye se instance varaible ko kase access krte hai 
# calling methods
student1.display_info()
student2.is_eligible()
 
student2.display_info()
student.is_eligible()


print('My name is Ali and I am 16 years old. I am in 10th grade.')