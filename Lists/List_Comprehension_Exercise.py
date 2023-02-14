# Using list comprehension construct another list called km that stores the distances from the miles list in kilometers.
# For this example 1 mile = 1.609 km
miles = [12, 10, 26, 80]
# 1 mile = 1.609 km
km = [m * 1.609 for m in miles]
print(km)  # => [19.308, 16.09, 41.834, 128.72
