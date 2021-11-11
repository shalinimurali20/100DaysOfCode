#004 banking roulette using lists and random module
import random

name = input("Enter names separated by commas: ")
names = name.split(", ")
# ran = random.randint(0, (len(names)-1))

# print(f"{names[ran]} should pay the bill")

person = random.choice(names)
print(person)