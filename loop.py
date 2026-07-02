x = [10,20,30,"ali",5.45]
for i in x:
    print(i)

name = " ali ahmad"
for a in name:
    print(a)


data = {
    "cgpa":2.43,
    "name":"ali",
    "samester": 5
}        
for a,b in data.items():
    print(a,"--",b)


for i in range (10):
    print(i)


cname = ["blue","black","white","red"]
for i in cname:
    if "e" in i:
        print(i)

shopping ={
    "shirt": 6500,
    "kaftan":9900,
    "frock":6900,
    "trouser":1500

}                
total = 0
for i ,p in shopping.items():
    print(i,":",p)
    total = total + p
print("total price is :",total)




x = []
x.append(10)
print(x)


x = []
for i in range(5):
    n = int(input("enter a number"))
    if n in x:
        print("already added")
    else:
        x.append(n)
print(x)









product = int(input("enter the product you buy"))
for i in range(product):
    name = input("enter the name of product")
    price = int(input("enter the price of product"))
    shopping["frock"]= price        
    
total = 0
for i ,p in shopping.items():
    print(i,":",p)
    total = total + p
print("total price is :",total)


