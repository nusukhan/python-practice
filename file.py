#different formats of data  file handling 
#(abi tk jitna humn data humne lekha wo humne ak code main lekha lekin age jase  jaa kr bht zada data aa ga wo sab hum code main nahi rakh sakte  to is trha ke data ko hum differenet file main rakh dete hai  )
# to is main hum prhe ge is trha ke file ko hum kis trha read or write kr sakte hai
#different format of data 
#text file: ( a text fie contains simple, humna_readable textual data
#csv ( comma- separated values): a file format in which data is stored in tabular form, separated by commas.
#web application : ( commonly use json,javascript object notation ) format for structured data exchanege
 # uske lye hum kya krte hai ak file ka object bante hai 
file = open("demo.txt","r") # or python ko kehte hai ak file ka objevt bana kr humri file  ke varaible main rekh do 
print(file.read())
file.close()
file = open("demo.txt","w")
file.write("this is aonther test.")
file.close()
# agr hum file  open krte hai ,use krte hai to usko close krna bht zarori hai nahi to uske contant khrb hu jate hai
# yaha python hume ak sahulat dete hai ke  context manager ko use krke ye bta sakte  hai ke hum itne context  ke lye file ko  use kr rhe hai
# or phr python automatically us file ko close kr de
with open("demo.txt","r") as file: # with hai ye ak asa context manager hai  jis main hum ye batte hai ke ye ak khas context ke lye open krte hai or jab close hu g to close hu jia
    data = file.read() # ye in dono statement ko execute hone tk open rhe g or end pr indentation ke bad close hu jai g
    print(data)
    # file close automatically here!
     #__> open(): the standard file context manager for reading/ writing files.
     #__>tempfile.temporaryfile()/ NamedTemporaryFile(): creating temporary files that delete themselves automatically.
     #__>zipfile.zipfile(): opens.zip files for reading / writing.
     #__> contextlib.exitstack:lets you manage multiple files at once easily.
     #__> pathlib.path().open()( modern,object-oriented file opening via pathlib)
       



       # common issues in file handling
       #1.file not found
       #2.wrong path
       #3.wrong file mode 
       # in sab issue ke waja se hamra programm crash kr sakta hai 

       # apne program ko crash se bachne ke lye hum  exception handling krte hai


       #exception handling ( ak error hai jo chlte howe apke code main aa jta hai  or agr apne us exception ko handle kr lya to apka program crash nahi gya ga or agr ap nahi kr sake to apka  program crash hu jai ga )
    # or agr apne thk nahi kya to python error de kr program ko stop kr de ga
