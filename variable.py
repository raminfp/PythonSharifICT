

# x = 25
# def printer():
#     x = 50
#     return x
#
# print(x)
# print(printer())

# name = "this is a global name"
# def check():
#     name = "python"
#     def hello():
#         print("Hello " + name)
#     hello()
#
# print(name)
# check()
#

x = 50

def func1():
    # global x
    x = 2

func1()
print(x)