# encapsulation
# encapsulation means keeping all the data ( attributes) & methods of an object inside that object
# iska mtlb ye hi ke hum ak object ke sare data attribue ko or method ko us objevt ke andr rakhte hai  or hum user ko ye facilate krte hai ke us object ko manipulate krna chhe to  to wo uske method ke zarye sse kr de yha pr data hiding ka concept aa jataa hai
# hum dataa ko user se hide kr de
# internal details behr dekhne ke bjhe hum usko class ke andr rakh detee hai
# or class ke method ko expose kr dete hai  take log unko use kr sake


# private attribute ( private attributes are those attribute that can obly be used within the class,'s own methods.)
# ase data attribute hote hai   jo surf class ke apne method ke and use ho sakte hai   unko global scale pr koi use nahi kr sakte
class student:
    def __init__(self, name, grade):
        self.__grade = grade  # private attribute ( kase pata chle ga private hai 2 underscore hai ) jis bhe daata attribute se phle hum underscore laga le wo private ban jtaa hai  asa data jo class ke andr function main istamal hu ga class ke behr istamal nahi hu ga


student1 = student("ali", 90)
print(student1.__grade)  # error


# to is trha ke private data ko access krne ke lye hum method ka sahra lete hai
# get_grade ke name se  or uske andr hum grade ko return kr de ga outside
class student:
    def __init__(self, name, grade):
        self.__grade = grade

    def get_grade(self):
        return self.__grade


student = student("ali", 90)
print(student.get_grade())
# humne ye dekha ke object orientated programming main encapsulation ka or ye (ak  classs ka jo data hai wo behr accessble na hu  ye concept acgieve krne ke lye hum class ke attribte ko private kr dete hai private attribute class ke behr accesible nahi hote  unko access krne ke lye class ke  wall ko method chice krne pare g     
