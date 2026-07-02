#tuples in python ( a built in data type that lets us create immutables sequences of value )
# list mutable we can change value tuple immutable uske value change  new elements ko add nahi kr sakte old ko delete nahi kr sakte nahi kr sakte  just like string
t = (1,2,3)
print(t)
#t(0) = 10 # error aa ga mtlb tuples ke value change nahi hu sakte 
#tuple directly change nahi hu sakta lekin list main change kr ke change hu sakte hai  
#for example
t = ( 1,2,3)
l = list(t) # tuple ko list banya 
l[0] = 10 # change kya 
t = tuple (l) # waps tuple banya 
print(t)
print(type(t))
print(t[0])
print(t[1])
#t[0] =10  # hum kisi bhe index pr jaa kr value change nahi kr sakte  humre pass error aa ga 
tup = () # valid tuple 
print(tup)
print(type(tup))
# lekin agr hum simple 
tup = (1,) # single value ke sath , lagna compulsor hai is trha kre ge to wo tuple typr dhoe kre ga 
tup = (1)# is trha wo 1 ko ak integer samjhe ga
print(tup) 
print(type(tup))
print(t[1:3])
#tuple method
#tup.index(el) fisrt time wo element kab aya
tup = (1,2,3,4)
print(tup.index(2)) #2 ak element hai or jo output de ga wo index bti ga
#tup.count hum jo bhe element pass krte hai wo kitne bar aya hai 
print(tup.count(2)) # is ka mtlb hai 2 kitni bar aya hai 
list =[ "salman","sharukh khan","umair"]
print(list)
