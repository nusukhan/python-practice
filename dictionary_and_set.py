# dictionary are used to store values in key : value pairs 
# they are unordered , mutable (changeable) & don't allow duplicate key
#simple jab bhe muje kisi  word ka mtlb dhondna hu ga  search krna hu ga 
#hum meaning ko search nahi kre ge hum word ko search kre ga 
# for example word hota hai or uska meaning hota hai 
#word    meaning 
# key    valuue ( so is trha ke key type value ko python main store krwane ke lye hum  tp usko hum store krwate hai in the form off dictionary )
info1={
    "key":"value",
    "name":"apnacollage",
    "learning":"coding"
}
print(info1)
info = {
"subject":["python","c","java" ],# hum list main bhe dictionary create kr sakte hai 
"topics": ("dict","set"),# tuples 
"age": 35 ,
"is_adult": True
}
print(info)
#key ak flooting value bhe hu sakte hai ,number bhe bulin value tuple asi value jo change na hu sake
print(info1["name"])
print(info["topics"])
print(info["age"])

info["name"] = "shradhakhapra" #we can change the value in the key 

print(info)
info["name"] = "shradha"

person = {  
    "name" : "Umar",
    "name" : "Samra",
    "age" : 27,
}

# person["name"] = 'Samra'

print(person["name"])
null_dict = {}
print(null_dict)