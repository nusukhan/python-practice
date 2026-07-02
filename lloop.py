# loop in python
# koi asi cheez jo bar bar repeat hoti hai usko loop kehte hai
# loops are used to repeat instructions until a certain condition is met

# there are two types of loops in python
# 1. for loop
# 2. while loop

# for loop
# for loop is used to iterate over a sequence
# (list, tuple, string) or other iterable objects
# iterable objects are objects that can be iterated over

# syntax of for loop
# for variable in sequence:
#     code to be executed

# example of for loop

#fruits = ["apple", "banana", "cherry"]  # fruits is a list of strings

# fruit is a variable that takes the value
# of each item in the list one by one
#for fruit in fruits:
 #   print(fruit)  # output will be apple, banana, cherry

# or we can also use the range function
# to generate a sequence of numbers

# range function is used to generate a sequence of numbers

# syntax of range function
# range(start, stop, step)

# start is the starting number of the sequence
# (default is 0)

# stop is the ending number of the sequence
# (not included in the sequence)

# step is the increment value of the sequence
# (default is 1)

# i is a variable that takes the value
# of each item in the sequence one by one
#for i in range(5):
    # output will be 0, 1, 2, 3, 4
    # 5 is not included because it is the stop value
 #   print(i)

# we can also specify the start and step values

# example of range function with start and step values
#for i in range(1, 10, 2):
    # 1 is the start value
    # 10 is the stop value
    # 2 is the step value

    # output will be 1, 3, 5, 7, 9
    # 10 is not included because it is the stop value
 #   print(i)

# for loop can also be used to iterate over a string

# example of for loop to iterate over a string
#for letter in "hello":
    # letter takes each character one by one
 #   print(letter)  # output will be h, e, l, l, o

# we can also use for loop to iterate over a tuple

# example of for loop to iterate over a tuple

#numbers = (1,2,3,4,5,)

# numbers is a tuple of integers
# and it is an iterable object

#for number in numbers:
    # number takes the value of each item
    # in the tuple one by one
  #  print(number)  # output will be 1, 2, 3, 4, 5

# Q:
# Why does range skip the end value,
# but for number in numbers does not skip 5?

# Answer:
# Because range() has a stop value rule.
# The stop value is never included.

# Example:
# range(5) -> 0, 1, 2, 3, 4

# But in "for number in numbers",
# the loop is directly iterating over the tuple values.

# The tuple already contains 5,
# so the loop prints it as well.

# for loop itself does not skip values.
# It only prints whatever exists inside the iterable object.
#in this case, the tuple contains 5, so it is printed.
# in contrast, range (5) generates numbers from 0 to 4, excluding 5, due to its stop value rule.
#for loop is just a way to iterate over the items in the tuple, and it does not have any rules about skipping values.
# the behavior of skipping values is determined by the iterable object (like range)and not by the for loop itself . so it mean ke for loop is just a tool to access the items in the ietrated object
# so iska mtlb ye howa skip hone ka decision range function ka hai,for loop ka nahi. for loop bas item ko acess karne ka tarika hai,aur range function decide karta hai ki kaure values ko include karna hai aur kaunse ko skip karna hai.
# for loop just string,list,tuple ke items ko acess karne ka tarika hai,aur range function decide karta hai ki kaure numbers ko include karna hai aur kaunse ko skip karna hai.



#while loop
#while loop is used to execute a block of code repeatedly until a certain condition is met 
#syntax of while loop
#while condition:
#  code to be executed
#example of while loop
#i = 0 # i is a variable that is initialized to 0 and it will be used to control the loop  
#while i < 5: # the loop will continue to execute as long as the condition i < 5 is true and when i bcomes 5 or greater, the loop will stop executing 
 #   print(i) #output will be 0,1,2,3,4
#    i += 1 # increment the value of i by 1 in each iteration i += 1  # same as i = i + 1


#| Step | i value | Condition `i < 5` | Print | Next i |
#| ---- | ------- | ----------------- | ----- | ------ |
#| 1    | 0       | True              | 0     | 1      |
#| 2    | 1       | True              | 1     | 2      |
#| 3    | 2       | True              | 2     | 3      |
#| 4    | 3       | True              | 3     | 4      |
#| 5    | 4       | True              | 4     | 5      |
#| 6    | 5       | False → STOP      | ❌     | -      |

#Agar i += 1 na hota, to:

#i kabhi change nahi hota
#condition hamesha true rehti
#loop infinite (endless) ho jata 😵




    #muje ye while loop samjh nahi aaya, kya aap muje iska ek usable example de sakte hai, jisse mujhe ye samjh aajai ki while loop kaise kaam karta hai aur iska use kab karna chahye?
    #sure,lets say you want to create a simple game where the user has to guess a number between 1 and 10. you can use a while loop to keep asking the user for their guess until they guess the correct number.here is an example of how you can use a while loop for this game:
#import random #import random is a module that provides functions to generate random numbers 
#number_to_guess = random.randint(1,10) #number_to_guess is a variable that stores a random number between 1 and 10 that the user has to guess random.randint(1,10) is a function that generates a random integerbeteen 1 and 10 
#user_guess = 0 #user_guess is a varaible that will store the user's guess and it is initialized to 0
#while user_guess != number_to_guess: #the loop will continue to execute as long as the user's guess is not equal to the number to guess
 #   user_guess = int(input("Guess a number between 1 and 10: ")) #ask the user for their guess and convert it to an integer
  #  if user_guess < number_to_guess: #if the user's guess is less than the number to guess, print "Too low!"
   #     print("Too low!")
   # elif user_guess > number_to_guess: #if the user's guess is greater than the number to guess, print "Too high!"
    #    print("Too high!")
    #else: #if the user's guess is equal to the number to guess, print "Congratulations! You guessed the correct number!"
     #   print("Congratulations! You guessed the correct number!")

 # 1. import random (Ye Python ka module (library) hai)
 #Is se hum random (random = koi fixed nahi) numbers generate karte hain
 # 2. number_to_guess = random.randint(1, 10)Is line ka matlab:
#Computer ek random number choose karta hai 1 se 10 ke beech
#Wo number hidden hota hai user se
#Example:
#3
#7
#10
#(kuch bhi ho sakta hai)
#3.user_guess = 0 
# Iska matlab:( Abhi user ne koi guess nahi kiya
# 0 sirf starting value hai loop start karne ke liye
#4.while user_guess != number_to_guess
# Loop ka main rule:
#Jab tak user ka guess correct nahi hota, loop chalta rahega
#!= ka matlab: not equal
#Agar guess galat hai → loop repeat
#5.Input lena:
#user_guess = int(input("Guess a number between 1 and 10: "))
# Iska matlab:
#User se number poocha jata hai
#int() input ko number mein convert karta hai
#Example:
#User types: "5"
#Python converts it to: 5

#6.Condition check
# Case 1:
#if user_guess < number_to_guess:
# Agar guess chhota hai:
# Print: "Too low!"

# Case 2:
#elif user_guess > number_to_guess:

# Agar guess bada hai:
# Print: "Too high!"

# Case 3:
#else:

# Matlab guess sahi ho gaya:
# Print:

#Congratulations! You guessed the correct number!
#Full Game Flow (Real Example)

#Maan lo number hidden hai = 6

#Attempt	User Guess	Result
#1	3	Too low
#2	8	Too high
#3	6	Correct 
#Is game mein while loop isliye use kiya gaya hai kyunki hume user se baar baar input lena hai jab tak wo sahi guess nahi karta. Agar hum for loop use karte, to hume pehle se pata hona chahiye tha ki user kitni baar guess karega, jo ki possible nahi hai. Isliye while loop is case mein zyada suitable hai.
#while loop is used when we want to repeat a block of code until a certain condition is met, and we don't know in advance how many times we need to repeat it. in this example, we want to keep asking the user for their guess until they guess the correct number, and we don't know how many guesses it with take, so while loop is the best choice for the game.
# while loop kis kis pr use hota hai :
#1.user input lene ke liye
#2. kisi condition ke true hone tak code repeat karne ke liye
#infinite loops banane ke liye (jab tak user manually stop na kare)
#3. kisi process ko continously run karne ke liye (jaise ki server running)
#4. kisi game mein baar baar user se input lene ke liye jab tak wo sahi guess na kare
#5. kisi task ko repeat karne ke liye jab tak wo complete na ho jaye (jaise ki file download hona)
#6.kisi condition ke false hone tak code repeat karne ke liye (jaise ki while True: ... break when condition is false)
#7. kisi process ko continuously monitor karne ke liye (jaise ki sensor data read karna)
#8. kisi task ko repeat karne ke liye jab tak user exit command na de (jaise ki while user_input != "exit": ...)
#9. kisi condition ke true hone tak code repeat karne ke liye (jaise ki while not success: ...)
#10. kisi process ko continuously run karne ke liye (jaise ki while True: ... break when some condition is met)
#kya while loop string tuple list pr bhi use hota hai?
#while loop string, tuple, list pr bhi use hota hai, lekin for loop zyada suitable hota hai un cases mein. while loop tab use karte hain jab hume repeat karna hota hai jab tak koi condition true rahe, aur hume nahi pata hota ki kitni baar repeat karna hai. for loop tab use karte hain jab hume kisi sequence (jaise ki string, tuple, list) ke items ko access karna hota hai, aur hume pata hota hai ki kitne items hain. isliye for loop zyada convenient hota hai un cases mein. lekin agar aapko kisi sequence ke items ko access karna hai jab tak koi condition true rahe, to aap while loop bhi use kar sakte hain, bas thoda sa extra code likhna padega to manage the index and the condition.


#while loop mtlb jab tk koi condition true hai,tab tk code repeat hota rahega,aur jab condition false ho jati hai,to loop stop ho jata hai.isliye while loop ka use tab karte hain jab hume repeat karna hota hai jab tk koi condition true
#rahe,aur hume nahi pata hota ki kitni baar repeat karna hai. for loop tab use karte hain jab hume kisi sequence (jaise ki string, tuple, list) ke items ko access karna hota hai,aur hume pata hota hai ki kitne items hain. isliye for loop zyada convenient hota hai un cases mein. lekin agar aapko kisi sequence ke items ko access karna hai jab tk koi condition true rahe, to aap while loop bhi use kar sakte hain, bas thoda sa extra code likhna padega to manage the index and the condition.
#count condtion mtlb jab tk ye condition: colon laga kr some condition lekh dete ha
count = 1 # count is a variable that is initialized to 1 and it will be used to comtrol the loop yaha humne count ko 1 se start kiya hai,aur loop tab tk chalega jab tk count 5 se chhota ya barabar hai,aur har iteration ke baad count ko 1 se increase karenge, taki loop eventually stop ho jaye jab count 6 ho jaye, kyunki 6 > 5 hai, aur count 5 se barabar ya chahora na rahe 
while count <= 5: #while mtlb jab tk count 5 se chhota ya barabar hai,tab tk loop chalega yaha count ak condition hai,jo check karta hai ki count 5 se chhota ya barabar hai 
    print(count) #print kr do count ki value 
    count += 1 #count ko 1 se increase kr do har iteration ke baad, taki loop eventually stop ho jaye jab count 6 ho jaye,
 
n = 5 
while n >= 10:
    print(n)
    n -= 1
# kya iska mtlb ye haai ke n jo hai wo se 5 se start hu ga mtlb loop start hoga jab n ki value 5 hogi aur loop tab tk chalega jab tk n ki value 10 se b 
