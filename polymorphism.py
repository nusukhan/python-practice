#poly mean  multiple and morphism mean form 
#polymorphism refers to the ability of a function or method to exist in multiple forms.
#yne ak he object bht sari form lee sakta hai  ( )
class dog:  # define dog class or us main speak ka ak function rakha  hum different class ko  akhta kr ke ustilize kr sakte hi  object different class ko kase belong kr sakte hai  
    def speak(self):
        print("woof!") # or hume pata hai dog kase woof krta hai 

class cat: # another class of cat 
    def speak (self):
        print("meow!")

for pet in [Dog(),cat()]: # dog ke or cat ke class ko ak sath use kr rhe hai  ( yaha humne python ko kaha ak dog ,or ak cat ka object baneo  or in dono ko pet ke andr rakh do )
    pet.speak() # or unke speak ke function ko call kr rhe hai   ( pet ak asa list of object hai   jis ke and r phla object dog or dosra cat ka hai  or hum loop main is pori list ko alterate kr ke har  object pr speak ka function call kr sakte hai   ) 
 # function overriding ( ye hoti hai ke  hum inheritence ke andr  paraents class ke  ksis method ko chil class yni inhertance  )
 # jab child class  apni parent class  ke function ko same name se dobra likh deti hai , usko overriding kehte hain 
 #vehicle class main move ( function hai ,car class ne same name ka function dubra lekh de  iska mtlb child class ne parent class ka function replace kr dia )
class vehicle: # parent class  ( ye base class hai  isme orinal function move () bana howa hai )
    def move (self):
        print("vehicle is moving")

class car(vehicle): # child class = car isne vehicle class ko inharit kya hai  ye vehicle he bta rha ai (car, vehicle se he cheeze lee rha hai )
    def move(self):
        print("car is moving")   

 # inheritance kya hai ( jab ek class dusri class ke features ( function, varaible ) use kare ) )
 # class car(vehicle) ye car class automatically vehicle ke function use kar sakti hai         

car1 = car()
car1.move()
# agr overriding na hoti to kya hota  ( agr car class main move ()na lekhe to )
class car (vehicle):
    pass 
#or phr   
c = car()
c.move()
#output hota vec=hicle is moving  ( kyu ke car ne parent class ka function use kya hai )
 #lekin overriding ke wja se humne car main khud he move lekh dia 
def move(self):
    print("car is moving ") # parent wala function ignore hu gya ab or child wala function chle ga ab 
     
# overloading ( jab ak he function ko different number of arguments ke sath use karte hi usko overloading kehte hai ) 
# ( same function ko different input ke sath use kro )
class calculator:
    def add (self,a,b = 0,c = 0): # yaha hum ak he function add ko multiple  ways me use kar rhe hai 
        return a + b + c
calc1 = calculator()
print(calc1.add(5))
print(calc1.add(5,10))
print(calc1.add(5,10,15))

