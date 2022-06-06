
# def <any name>(a, b, c):
#   write code here

def name(name):
    print(f"Name Function {name}")


def retName(a, b):
    return a + b


def checklst(lst):
    return func1(lst)

# name("python")
# print(retName(2, 1))

def func1(lst):
    return [item * 2 for item in lst]

def func2(strlst):
    return "python" in strlst

def func3():
    pass

# ls = [1,2,3,4,5,6]
# print(checklst(ls))
s_lst = ["go", "php", "python"]
if func2(s_lst):
    print("matched")
else:
    print("not matched")


