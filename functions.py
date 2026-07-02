def calc_sum(a=2, b=3):
    sum = a + b
    print(a + b)
    return a + b


calc_sum()


# retundant(repeat again and again )khrb coder ke neshani hai bar bar wahi same of line repeat krta hai jab ak cheez bar bar hu rhe hai to hum usko function bana dete hai
# do number ko lee or usko print kr de
# dwf mean define the function phr hum apne function ko kuch bhe name de sakte hai function main hum colon  paranthese main hum 2 value ko input lete hai
# input ( parametor) some value in input call def calcsum(parametor1,parametor2): is he trha hum multiple parametor le sakte hai parametor call variable ke name lekhne hote hai
def calc_sum(a=22, b=4):  # in value ko input lya
    sum = a + b  # in value pr kaam kyaa
    print(sum)
    # yaha tk hamra function kuch bhe output return nahi kr raha pr humchhte to hum apna return krwah sakte hai  return bhe hamri output ko waps bejhne ke lye use hota hai
    return a + b  # is value ko output lya


calc_sum()  # argument( value supply krna hai)


def calc_sum(a, b):  # a,b call parametor
    return a + b


sum = calc_sum(
    1, 2
)  # 1,2 call arguments calc_sum(1,2) this is call function call and argumnets ke he value hamre parametor main store hu jati hai  return ko hum kisi bhe varaible main store krwah sakte hai islye humne isko sum ke varaible main store krwaya hai
print(sum)


def print_hello():  # in parametor ko hum empty bhe chod sakte hai  YE JO hello function hai ye nahi koi input lee raha hai na he iske koi parametor hai nahe koi output de raha hai

    print("hello")


print_hello()
output = print_hello()
print(
    output
)  # none jo function output main kuch return nahi krta usko ouput main none aa ga


# calculate average of 3 value
def calc_avg(a, b, c):
    sum = a + b + c
    avg = sum / 3
    print(avg)
    return avg


calc_avg(1, 2, 3)
print("apnacollage")
cities = ["lahore", "karchi", "peshawar", "multan", "okara"]
heroes = ["imran", "ali", "amjad", "kashif", "salman"]
print(cities[0], end=" ")
print(cities[1], end=" ")


def print_len(cities):
    print(len(cities))


print_len(cities)
print_len(heroes)


def print_list(list):
    for item in list:
        print(item, end=" ")


print_list(heroes)
# string ( are immutable thing that cannot change index pr value ko acees krna allow tha lekin value ko change krna allow nahi th )

# list mutable that can be change  but in list  we can axcess the value as well as change the value
# name = "nusu" # AB YE AK STRING HAI isko hum excess kr sakte hai is lekin change nhi kr sakt
# name[0] = "M"# see jab hum ne n ke jaga m replace kya to wo error de ga
# lekin hum nayi string bana sakte hai
name = "nusu "
new_name = "M" + name[1:]
print(new_name)
# list ( change kr sakte hai ,index pr value replace kr sakte hai )
# example
fruite = ["apple", " banana", " mango"]
# index table
# value  apple  banana mango
# index    0       1     2
# agr hum change kre
fruite[1] = " orange "
print(fruite)  # yaha list change hu g mtlb mutable
# access our change ka difference
print(fruite[2])  # access krna mtlb  surfdekhna
# output mango ye surf value dekha raha hai
fruite[2] = "grape"  # ab list change hu g
# simple comparison
# feature          string     list
# immutable         yes       no
# index se access   yes        yes
# index se change    no          yed
# index ke andr jitni value hamri hai surf ushe ko access kr sakte hai just like agr humri list main surf 4 value hai to hum 5 wala access nahi kr sakte wo error de ga
# list slicing sublist list_name [ starting_index : ending_idx] ending indx is not including
marks = [87, 64, 33, 95, 76]
#   0  1  2  3  4
marks[1:4]  # 64 33 95 aa ga 76 nahi aa ga just
marks[:4]  # is same as marks [0:4]
marks[1:]  # is same as marks [1:len(marks)]
marks = [85, 94, 76, 63, 48]
print(marks[1:])
print(
    marks[-3:-2]
)  # iske , galne se iske type tuple ban gai : ye dale ge to slicing banne ge
# comma not allow colon allow list indexing main surf ek integer allow hota hai marks [2] ye integer hai
# ya skicing allowed hoti hai marks [ 1:4] ye ab slicing hu gai
# list methods mean function
# len hamri string ,list ,tuple ke bhe lenghth print krwah de ga
# list method
# print('==================================================================================================')
