# List comprehension in Python is a compact way of creating a list from a sequence. It is a short way to create a new list. List comprehension is considerably faster than processing a list using the for loop

# For instance if you want to change a string to a list of characters. You can use a couple of methods. Let's see some of them:

# one way

word = "Selena"

ls = list(word)
print(ls)

# +++++++++++ List Comprehension +++++++++++

lst = [i for i in word]
print(lst)

nums = [i for i in range(6)]
print(nums)


# ++++++++++ list of tuples ++++++++++

nums = [(i,i+i) for i in range(5)]
print(nums)


# List comprehension can be combined with if expression

# even numbers
nums = [i for i in range(11) if i % 2 == 0]
print(nums)

# odd numbers
nums = [i for i in range(11) if i % 2 != 0]
print(nums)

# filtering out postive even nums

numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positve_nums = [i for i in numbers if i > 0 and i % 2 == 0]
print(positve_nums)


# Flattening a two dimensional array

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flat_list = [num for row in list_of_lists for num in row]
print(flat_list)


