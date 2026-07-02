#instance varaible and instance method
#instance se murad ak object hai  jo hum kisi bhe class ka bnta hai( an instance refers to an object created from a class)
#class ak template howa or isse jitne bhe hum object banne g wo instance hu g 
#purpose of making multiple object 
#( each object has iits own attributes.), each object has its own methods.
#har object ke apne attribute hu g apne method hu g 
class student:# student class 
    def __init__(self,name,age,grade):#init is our contractor  and there is 3 arguments name,age,grade)
         self.name = name # 3 instance varaible hum kase pata chle ga ke ye instance varaible hai har varaible ke start pr self . laga hu ga 
         self.age = age# instance varible hum self. ke key words se start krte hai 
         self.garde = grade # agr humne  studentke name ka data attribute  bana ha to hum usko self . ke name se banne g or phr hum  isko hum initilize kr de ge us   us input se jo humne contractor main pass ke    self .age se uska instance ban jai ga  self  ka varaible hume ye btta hai ke ye kis object pr call howa  ya ye  data  member kis particular object ka hai kyu ke class to ak template hoti ha uska physical koi  existance nahi hoti  physical vajood surf object ka hota hai  is lye hum ye bat sure hone chhe jo hum data attribute excess kr rhe hai wo kkis particular object ka hai  
    def display_info(self):# ye ak method hai display info ka  iske andr bhe self ka object pass howa ye wahi object hai jis pr ye function call howa 
         print(f"student Name:{self.name}") # yaha hum print kr rhe hai students ke 3 attribute 
         print(f"age:{self.age}") # sge name grade attribute  or jo hume attribute print krne hai wo instance varaible hai lehza unko print krne ke lye hum lekhe g self.age self.name,self.grade
         print(f"grade:{self.grade}") 
    def is_eligible(self):   # method is eligible 
     if self.age>= 15:
              print(self.name,"is eligible for admission.")
     else:
            print(self.name,"is not eligible for admission")
# parametor function define karte time jo name lekhte hai self,name age ,grade 
# argumnent function call karte time jo actual value dete hai  ali 15 A ye sab argumnets hai          
 # jo cheez self . ke sathho attribute ( instance varaible )     
