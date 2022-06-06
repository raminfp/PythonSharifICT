# Create tuple
# basic methods
# Immutability
# when we use tuple

my_tuple: tuple[int, int, int, int, int, int] = (1, 2, 3, 1, 1, 2)
# my_tuple = (1, 2, 3, 1, 1, 2)
print(len(my_tuple))
print(my_tuple)
print(my_tuple[0])
print(my_tuple[-1])

# Basic Methods
print(my_tuple.index(3))
print(my_tuple.count(2))

# Change Value (Immutability)
lst_tup = list(my_tuple)
lst_tup[0] = 123
my_tuple = tuple(lst_tup)
print(my_tuple)
print(type(my_tuple))
