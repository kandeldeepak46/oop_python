# Getting user input
temp = int(input("What's the tempreature?"))

# conditionals
if temp <= 0:
    print("Freezing")
elif temp >= 100:
    print("Boiling")
else:
    print("Good to go")

# Lists
populous_countries = ["China", "India", "USA", "Indonesia", "Brazil"]
# Mutable
populous_countries[2] = "United States"
populous_countries.append("Nepal")
populous_countries.append("Pakistan")

# For Loop
for i in range(10):
    print(i * i)
# Comprehension
list = [i * i for i in range(10)]

# While
from time import sleep

seconds_left = 3
while seconds_left > 0:
    print(seconds_left)
    sleep(1)
    seconds_left -= 1
print("Lift Off")

# Functions
def square(num):
    return num * num


# Assertions
assert square(10) == 100

# Dictionaries

fruit = {"a": "apple", "b": "banana", "c": "coconut"}

print(fruit["a"])
fruit["c"] = "cherry"
fruit["d"] = "dragon fruit"

# Exceptions
user_input = input("Give me a number:")

try:
    number = float(user_input)
except ValueError:
    print(f"{user_input} is not valid number")


if __name__ == "__main__":
    main()
