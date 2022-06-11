import json

import requests

s = "Global variable"

def check_for_locals():
    dd = "okok"
    print(locals()["dd"])

# check_for_locals()
# print(globals()['s'])


def hello(name="python"):
    return f"hello {name}"

# # print(hello())
# passed = hello
# print(type(passed))
# print(passed())

# Functions in function

def hello(name="python"):
    print("This is hello() functions")
    def inhello():
        return "this is inhello() function"
    def inhello2():
        return "this is inhello2() function"
    if name == "python":
        return inhello
    else:
        return inhello2

# x = hello()
# print(type(x))
# print(x())

def hello():
    return "Hello All"

def other(func):
    print("Other functions")
    print(func())

# other(hello)

## Create decorator


def _methods(**kwargs):
    def _func(func):
       # func.<> = asdasd
       if kwargs['method'] == "GET":
            func()
       elif kwargs['method'] == "POST":
            func()
    return _func


@_methods(method="POST")
def post_Method():

    url = "https://reqbin.com/sample/post/json"
    data = {"Id": 78912}
    res = requests.post(url, json.dumps(data))
    if res.status_code == 200:
        print(res.text)


@_methods(method="GET")
def get_method():
    url = "https://reqbin.com/echo/get/json"
    res = requests.get(url)
    if res.status_code == 200:
        print(res.text)

