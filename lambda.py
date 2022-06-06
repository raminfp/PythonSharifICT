# Lambda, map , filter

def squre(num):
    return num % 2 == 0

my_num = [0, 2, 3, 4]
# General
# print(squre(my_num))
# Map
# print(list(map(squre, my_num)))
# Filter
# print(list(filter(squre, my_num)))
# Lambda

def lamda_test(num):
    return num ** 2

# print(lamda_test(2))
upper = lambda num: num.upper()
lower = lambda name: name.lower()

print(upper("hello"))
print(lower("HELLO"))

print(list(map(lambda num: num * 2, my_num)))
print(list(filter(lambda n: n % 2 == 0, my_num)))

d = lambda x: x[0]
print(d([1, 2]))
