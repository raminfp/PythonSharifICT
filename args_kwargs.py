

# def func1(a,b,c,d,e):
#     return sum((a,b,c,d,e))
#
# print(func1(1,2,3,4,5))

# def myfunc(*ok):
#     return sum((ok))
#
# print(myfunc(10, 20, 30, 40, 50))

# def myfunc(**kwargs):
#     if 'php' in kwargs:
#         print(f"we have string php {kwargs['php']} in here")
#     else:
#         print("we don't have php string in here")
#
# myfunc(php="okokk")

def myfunc(*args, **kwargs):
    if 'go' and 'python' in kwargs:
        print(f"{kwargs['go']} and {kwargs['python']}")
        print(args[0])
    else:
        print(args)

myfunc("reza", go="golang", python="python")