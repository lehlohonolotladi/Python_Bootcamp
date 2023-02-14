my_list = [[1, 2], 1, 2.5, 'a', ['a', 'b', 3.3]]
print(my_list[1:][-1][-1])
# Checkout the following
# list with 4 elements: a float, an integer, a string and another list
my_list = [2.3, 5, 'Python', ['a', 2]]

# the 2nd element of my_list
x = my_list[1]

# the 2nd element of the inner list
y = my_list[3][1]

# list slicing that returns a new list with the first 2 elements of my_list
z = my_list[0:2]
