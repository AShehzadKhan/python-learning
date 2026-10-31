# Declaring and Calling a Function

def greet():
    print("Hello world")

greet()

# ++++++++++++++ Functions without parameters +++++++++++

def add_nums():
    num1 = 10
    num2 = 20
    total = num1 + num2
    print(total)

add_nums()

# ++++++++++ Function Returning a Value ++++++++++++++=

def name():
    first_name = "Selena"
    last_name = "Khan"
    full_name = first_name + last_name
    return full_name

print(name())


# +++++++++++ Function with Parameters +++++++++++

def greetings(name):
    message = "Hello " + name + " Welcome back"
    return message

print(greetings("Selena"))

def area_of_cirlce(radius):
    area = 2 * 3.14 * radius
    return area

print(area_of_cirlce(3))


def add_two_nums(num1, num2):
    total = num1 + num2
    return total

print(add_two_nums(10,20))


# if we pass the key value pair in arguments the order of argument doesn't matter


def name(first, second):
    full_name = first + second
    return full_name

print(name(second="khan", first="selena"))


# ++++++++++++++++++++ Returning a boolean ++++++++++++++++++++

def is_even(num):
    if num % 2 == 0:
        return True
    return False

print(is_even(6))
print(is_even(7))


# ++++++++++++++++++++++ Returning a list ++++++++++++++++++

def even_nums(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens

print(even_nums(10))

# +++++++++++++++ Function with Default Parameters ++++++++++++++

def greet(name = "Selena"):
    message = name + ",Welcome"
    return message

print(greet())

# +++++++++++++++++ Arbitrary Number of Arguments +++++++++++++++
# If we do not know the number of arguments we pass to our function, we can create a function which can take arbitrary number of arguments by adding * before the parameter name.

def sum_all_nums(*nums):
    total = 0

    for num in nums:
        total += num
    return total

print(sum_all_nums(12,4,5))

# +++++++++++++ unpacking the dictionary +++++++++++++

def greet(name, location):
    message = "Hi " + name + " What's going on in " + location
    return message

info = {"name":"Selena", "location":"Nova"}

print(greet(**info))


# ++++++++++++ Function as a Parameter of Another Function ++++++++++

def add(num1, num2):
    return num1 + num2

def multiply(num1, num2):
    return num1 * num2

def calculate(func, num1, num2):
    return func(num1, num2)

print(calculate(add,10,5))
print(calculate(multiply,3,4))


# +++++++++++++++++ Exercises +++++++++++++++++++++++++

def celcius_to_fahrenheit(celcius):
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit

print(celcius_to_fahrenheit(38))


# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.


def odd_sum(*nums):
    total = 0
    for num in nums:
        if num % 2 != 0:
            total += num
    return total


print(odd_sum([1,2,3,4,5,6,7]))


def even_sum(nums):
    total = 0
    for num in nums:
        if num % 2 == 0:
            total += num

    return total

print(even_sum([1,2,3,4,5,6,7]))


def remove_item(items_list, item):
    ls = items_list
    ls.remove(item)
    return ls


food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_stuff,"Milk"))


def add_item(items_list, item):
    ls = items_list
    ls.append(item)
    return ls


food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']

print(add_item(food_stuff,"Oranges"))


def reverse_list(nums):
    ls = nums
    ls.reverse()
    return ls

print(reverse_list([1,2,3,4,5]))