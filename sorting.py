list = [2,1,3]

print(list)

list.append(4) # [2,1,3,4]

# print(list)

list.sort() # [1,2,3,4]

list.sort(reverse=True) # [4,3,2,1]

print(list)

# Sort "list" in ASC order again
list.sort()
print(list) # sorting is not just apply on number,it also apply on alphabet string 
# let se
list = [ "banana","liches","apple"]
print(list.append("grapes"))
print(list.sort(reverse=True))
print(list)
list = ['a','d','e','f','c','b']
list.reverse()
print(list)
list =[2,1,3]
#list.insert( idx,el) #insert element at index particullay index pr new value add krta hai  just if we add to value in the middle  first hai kon se index pr value add krna chhte hai dosra el , elemen ko add krna chhte hai 
list.insert (1,5)
print(list)
list =[2,1,3,1]
list.remove(1) # ab hum chhte hai 1 remove hu jai to wo dekhe ga list main 1 kaha hai wo usko remove kr de ga remove first occurrense of element [2,3,1]
print(list)
#list.pop(idx) #removes element at idx kisi ak particular index pr ja kr value ko delete krna
list=[2,1,3,1]
list.pop(2) #index 2 pr jaa kr value ko delte kr do ab hamre index 2 pr value 3 pari hai islye output main usko jaa kr remove kr de ga 
print(list) 


