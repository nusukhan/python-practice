with open("data.txt","w")as f:
    f.write("hello")
    #"data.txt" ye real file hai (disk me saved)
    #open("data.txt","w")
    #ye kya krta hai
    #file ko open krta hai or banta hai file object
     #as f us filr object ko name de dia f 
     # f = file object
     #f.write("hello")
     # ye kya kre ga file object ke through ( real file (data.txt) me "hello " elkh de ga )
with open ("missing.txt","r") as file:
    print(file.read())
 # ye ak error de ga ke is trha ke file nhi hai 
 # is trha ke error ko sahi krne ke lye hum lgte hai (try)
try: #  yaha hum python ko kehte hai is code ko try kro  kyu ke hume shakh hai ke is code main koi exception aa sakte hai  
    with open("missing.txt","r") as file:
        print(file.read())
except FileNotFoundError: # or yaha hum lekh dete hai ke agr error aa to python ne kya except krna hai 
    print("File not found!")
# or phr hume bta dete hai ke ye error aa to ye krna ye aa to ye krna  
# yaha humne btya hai ke agr filenot found ka error aa to tumne print kr dena hai
# agr file nahi hu g to wo hume just error ka output de de g itna lamba message eeror ka nhi de g 
  
# importance of exception handling
#  ( due to an error, python will stop the program & display an error message; instead the error & allow the program to continue running)
#    exception handling 
# WHEN AN ERROR occurs in your program , yiu inform python that the erro was expected & that you are handling it.
