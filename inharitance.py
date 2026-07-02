#inheritance
# inharitance allows a new class to reuse the properties & methods of an existing class 
# agr apne ak achi se class bana le us main data bhe define kr dia or ache se method bhe define kr dia isko ab is class ko further class main bhe kr sakte hai
class Animal:
    def speak(self):
        print("some sound")

class Dog(Animal):
    pass

dog1 =Dog()
dog1.speak()

class Dog(Animal):
    def bark(self):
        print("woof!")

childdog = Dog()
childdog.bark()