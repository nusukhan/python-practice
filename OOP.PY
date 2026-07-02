class Animal:
    def speak(self):
        print("Animal bol sakta hai ")
class Dog(Animal):
    pass        
d = Dog()
d.speak()
# class = plan
#object = kaam shuru
# jab tk 
#1. object nahi bane ga
#2. function call nahi karo gi 
#3. tab tk output nahi aa ga 
# dog= Dog() tum dog class ka object bana rhe hu 
# d.speak()
#class = design / plan /blueprint
#class Dog:
    # pass _> iska mtlb hai main design bana rhe hu 
#object = real cheez 
# d = Dog() iska mtlb 
class Dod:
    pass
d = Dog()
print(d)      
# dog class
class Dog:
    def bark (self):
        print(" woof woof") # dog class
#object 
d = Dog()
#method call karo
d.bark()
class Dog:
    def __init__(self,name):
        self.name = name   
    def show (self):
        print(" dog ka name hai:",self.name)
# object
d = Dog("Tommy")
#method call               
d.show()
#attribute
#name bread, age,color,weight,gender
#function / method ( action / behavior)
# these describe what a dog can do ( bark(),eat(),sleep(),run(),sit(),wag_tail())
#  