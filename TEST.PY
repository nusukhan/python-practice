# 5. Map numbers to whether they are even
# numbers = [3, 6, 9, 12, 15]

# Create a dictionary where:

# key = number
# value = True if even, otherwise False

# Expected output:

# {3: False, 6: True, 9: False, 12: True, 15: False}

numbers = [3,6,9,12,15]

words = {}

for number in numbers:
    words[number] = number % 2 == 0

print(words)
   


#1. Map Numbers to Their Squares

#Given:

#numbers = [1, 2, 3, 4, 5]

#Create a dictionary that maps each number to its square.

#Expected Output:#Gi

#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}   
numbers = [1, 2, 3, 4, 5]
words = {}
for number in numbers:
    words[number] =number** 2
print(words)

#2. Map Numbers to Their Cubes

#Given:

#numbers = [1, 2, 3, 4]

#Create a dictionary that maps each number to its cube.

#Expected Output:

#{1: 1, 2: 8, 3: 27, 4: 64}

numbers = [1, 2, 3, 4]
cube ={}
for number in numbers:
    cube[number] = number **3
print(cube)  

#3. Map Names to Their Lengths

#Given:

#names = ["Ali", "Sara", "Ahmed", "Zainab"]

#Create a dictionary that maps each name to its length.

#Expected Output:

#{"Ali": 3, "Sara": 4, "Ahmed": 5, "Zainab": 6}
names = ["ALI","sara","Ahmad","Zainab"]
lenght ={}
for name in names:
    lenght[name] =len(name)
print(lenght)    
#Convert Words to Uppercase

#Given:

#words = ["python", "java", "c++", "javascript"]

#Create a dictionary that maps each word to its uppercase version.

#Expected Output:

#{
    #"python": "PYTHON",
   # "java": "JAVA",
  #  "c++": "C++",
 #   "javascript": "JAVASCRIPT"
#}
words = ["python", "java", "c++", "javascript"]
uppercase={}
for word in words:
    uppercase[word] = word.upper()
print(uppercase)
#Map Fruits to Their First Letter

#Given:

#fruits = ["apple", "banana", "mango", "orange"]

#Create a dictionary that maps each fruit to its first letter.

#Expected Output:

#{
    #"apple": "a",
   # "banana": "b",
  #  "mango": "m",
 #   "orange": "o"
#}
fruits = ["apple", "banana", "mango", "orange"]
letter = {}
for fruit in fruits:
    letter[fruit] =fruit.capitalize()
print(letter)    


#6. Map Words to Number of Vowels

#words = ["apple", "banana", "kiwi", "orange"]

#Create a dictionary that maps each word to the number of vowels it contains.

#Expected Output:

#{
  #  "apple": 2,
 #   "banana": 3,
  #  "kiwi": 2,
 #   "orange": 3
#}
words = ["apple", "banana", "kiwi", "orange"]
vowels = "aeiou"
letter = {}
for word in words:
    count = 0
    for ch in word:
        if ch in vowels:
            count += 1
        letter[word] = count

print(letter)    

#7. Create a Dictionary from Two Lists

#Given:

#students = ["Ali", "Sara", "Ahmed"]
#marks = [85, 92, 78]

#Create a dictionary mapping students to their marks.

#Expected Output:

#{
   # "Ali": 85,
  #  "Sara": 92,
 #   "Ahmed": 78
#}
#8. Map Numbers to "Even" or "Odd"

#Given:

#numbers = [1, 2, 3, 4, 5, 6]

#Create a dictionary that maps each number to "Even" or "Odd".

#Expected Output:

#{
    #1: "Odd",
    #2: "Even",
   # 3: "Odd",
   # 4: "Even",
  #  5: "Odd",
 #   6: "Even"
#}
#9. Map Words to Their Reversed Form

#Given:

#words = ["apple", "banana", "kiwi"]

#Create a dictionary that maps each word to its reversed form.

#Expected Output:

#{
   # "apple": "elppa",
  #  "banana": "ananab",
 #   "kiwi": "iwik"
#}
#10. Map Characters to ASCII Values

#Given:

#chars = ["A", "B", "C", "D"]

#Create a dictionary that maps each character to its ASCII value.

#Expected Output:

#{
 #   "A": 65,
  #  "B": 66,
   # "C": 67,
    #"D": 68
#}