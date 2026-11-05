# +++++++++++++++++ Importing a Module ++++++++++++++++++

# import module

# # print(module.gen_full_name("Selena","Khan"))


# +++++++++++++++++++ Import Functions from a Module ++++++++++++++++++

# from module import info, gravity

# mass = 50

# weight = mass * gravity

# print("weight of person ",info["name"], ":", weight)


# Import Functions from a Module and Renaming

# from module import gen_full_name as fullname, info as person, gravity as g

# print(fullname("Selena","Khan"))
# print(person)
# print(person["name"])

# mass = 50
# weight = mass * g
# print(weight)

# +++++++++++++++++ Import Built-in Modules +++++++++++++++++++++
# OS Module

# import os

# os.mkdir("new_folder")

# print(os.getcwd())

# os.rmdir("new_folder")

# +++++++++++++++++++ Statistics ++++++++++++++++++

# from statistics import *

# ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]

# print(mean(ages))
# print(median(ages))
# print(mode(ages))


# ++++++++++++++++ Math Module ++++++++++++++++++++

# import math

# print(math.pi)
# print(math.sqrt(4))
# print(math.pow(3,2))
# print(math.floor(3.3))
# print(math.ceil(3.7))
# print(math.log10(100))

# ++++++++++++ String Module +++++++++++++++

# import string

# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)


# +++++++++++++ random module ++++++++++++++++++

from random import randint,random
from math import floor

print(randint(5,20))
print(floor(random() * 10))