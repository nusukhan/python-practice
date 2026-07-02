#function code ko short clean pr prganized banna ek specific kaam ko alg se handle krna and ak esa code block banna jo bar bar use hu
#def calcsum(a,b):#a,b parametor calcsum function call 1,2 arguments

 #   return a + b 
#sum = calcsum(1,2)
#print(sum)
def print_Hello():
     print("Hello")
print_Hello()
def calc_avg(a,b,c):
     sum=a+b+c
     avg=sum/3
     print(avg)
     return(avg)
calc_avg(1,2,3)
print("apna collage","shradha")#sep = "," koi gap nahi dete lekin sep automatically dono main gap de de ga
#kyu ke wo function ke line main already define hai space or ab output main space aa gai 
print("apna collage")
print("shradha")     #end = \n backslashin ka mtlb next ``line 
#now agr muje dono line ko same line pr print krwana hai then ending parametor ke koi or line edd krne hu g
#ending parametor ke koi or line pass krni hu g 
print("apna collage",end =" ")# end = " " hu gya to muje space chhe next line nhi chhe 
print("shradha")# now ye value same line pr print hu kr aa jai g " " is main kuch bhe pass kre g to wo output main print hu kr aa jai ga 
#funtion 
#built in function jo already python main built hai sach hai print,len,type,range or dosra hai user define jo user khud lekhta hai 
def cal_prod(a, b):
    print( a * b )
    return a * b

cal_prod(5,5) # ab jab main ase kro g to ye muje ak error de ga  cal_ pro ke andr 2 require arguments  hai jo missing hai jo a,b ke andr ja kr store hone the 
#or agr hum chhte hai ke bgr koi arguments pass kye function run kre to hum  to ab hum to hum apne parametor ko kuch default value de asi value jo tab use hu g jab koi argument pass nahi kre ge
#ab jab main koi argument pass nhi kro g to ye vale 1 assume kr le ga .
print("nusu")
print("i am a programmer")
print(" hello worlds")
print("shradha")
print("hello")