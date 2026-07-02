# method
#  a method is a function defined within a class 
#( method ak ase function ko kehte hai jo class ke andr define hu )
#jab koi function class ke andr hota hai, usko method kehte hai 
class car:
    def start (self):
        print("car started")
 # start()  method hai
 # reason ( kyu ke ye ak class ke andr hai )
 # method main hamesha self hota hai  
 # self ( ye current object ko represent krta hai  )
 # meaning ( mtlb jis method ne object call kya )
c = car()
c.start()
#specail function ( a speacil function defines built- in behavior automatically associated with certain operations)
#  wo  function jo python main already specail meaning rakhta hain or automatically call hu jaty hain  also call mmagic methods/ dunder methods 
#  # example __init__
class student:
    def __init__(self,name):
        self.name = name 
# ye kya krta hai jb object bnta hai 
s = student("ali")                     
 # ye automatically call hu jata hai 
 #__init__ ( object ko initialize karna ( data dena))
 


#Main difference
#FEATURE              NORMAL METHOD            SPECAILS METHOD --INIT--
#class ke andr          YES                      YES
#call kaise hota         manually                automatically
#example                 show()                  __init__()
      #__> jab dono class ke andr hai to alg kase 
      #.dono class ke andr hai 
      #. dono method hai 
    #difference
    #normal method _> tum khud call krte hu 
    #specail method _> python khud call krta hai  auto call 
