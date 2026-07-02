# 1. Write a program that takes salary as input. Using conditional statements, calculate the final tax
# based on the following rules: (Marks 3)
# • If the salary is less than 30,000 → Tax rate is 5%
# • If the salary is between 30,000 and 70,000 → Tax rate is 15%
# • If the salary is greater than 70,000 → Tax rate is 25%
# x = int(input("enter your salary:"))
# if x < 30000:
#   tax = x * (5 / 100)
# elif 30000 <= x <= 70000:
#   tax = x * (15 / 100)
# else:
# tax = x * (25 / 100)
# print("Tax:", tax)
salary = int(input("enter your salary:"))

tax = 0

if 30000 > salary > 70000:
    tax = salary * 10 / 100
else:
    print("condition does not meet")

print("Tax:", tax)


# 2.Given a list of words: words = ["apple", "banana", "kiwi", "cherry", "mango"] (Marks 3)
# Create a dictionary that maps each word to its corresponding length.
# Example Output: ({"apple": 5, "banana": 6, "kiwi": 4, "cherry": 6, "mango": 5})
