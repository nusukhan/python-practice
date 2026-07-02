#lambda function 
#( a lambda in python is a small anonymous function written in a single line .)
add = lambda a,b:a + b #  2 input parameter lye hai a,b  pr a+ b ye ak body hai a and b ko add kr dia hai  or uske return add ke andr store kr de g  jo 2varaible ko pkr kr add kr de ga yaha humne function ko define kya hai 
print(add(3,5)) # yhaa hum lambda function ko call krte thee  is main humne 2 varaible pass kye hai 3,5)
#lambda is a built in function
double_it = lambda n:n* 2# 
print(double_it(5))
#lambda a,b : a + b
#meaning 
#a,b  _> input
#a + b _> formula  ye value return kare ga 
#print ( add (3,5)) 
# a = 3
# b = 5
nums = [1,2,3,4] # list banne 
squares = list(map(lambda x:x*x,num))
print(squares)
#EXAMPLE MAP()
numbers = [1,2,3]
result = list(map(lambda x: x + 10 , numbers)) #har value ko add kre g 
#samjheo
# x = 1 _> 1 + 10 = 11
# x = 2 _> 2 + 10 = 12
# x = 3 _> 3 + 10 = 13
#output 11,12,13
# example 
nums = [ 2,3,4]
result = list(map(lambda x:x*x,nums))
print(result)
#samjheo
#2*2 = 4
#3*3 = 9
#4*4 = 16
#output
#[4,9,16]
# FILTER + LAMBDA 
# EXAMPLE 1 ONLY ODD NUMBERS
numbers = [1,2,3,4,5]
result = list(filter(lambda x:x%2!=0,numbers))
print(result)
#samjheo 
#1 odd
#2 even
#3 odd
#4 even 
#5 odd
#output
#[1,3,4]