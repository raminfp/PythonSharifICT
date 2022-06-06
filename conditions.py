# if else elsif

print(2 > 3)
print(2 == 2)
print(2 != 2)
print("test" == "test")
print(None == None)
print(False == True)
print("#######")
print([] == [])
print([1, 2] == [2, 1])
print([1, 2] == [1, 2])
print(len([1, 2]) == len([3, 2]))
print({"key1": "value1"}.get("key1") == {"key2": "value1"}.get("key2"))
print((1, 2, 3) == (3, 2, 1))
print({1, 2, 3} == {1, 2, 3})
print("#############")
# if 2 > 3:
#     print("3 > 2")
# elif 3 == 3 :
#     print("OK")
# else:
#     print("2 > 3")
s = "hello"
if s == "hello":
    print("OK")
else:
    print("NOK")

s = [1, 2]
f = [2, 1]
f.reverse()
if s != f:
    print("NOK")
else:
    print("OK")

lst = 1
if isinstance(lst, list):
    print("is list")
elif isinstance(lst, str):
    print("is str")
elif isinstance(lst, tuple):
    print("is tuple")
elif isinstance(lst, bool):
    print("is boolean")
elif isinstance(lst, set):
    print("is set")
else:
    print("type is unknown")
print(3 < 2 < 3)
# 1 == True
# 0 == False

# 1 0 == False
# 0 1 == False
# 1 1 == True
# 0 0 == False
print(1 < 2 and 2 < 2)
print(1 < 3 > 2)
# 1 0 == True
# 0 1 == True
# 1 1 == True
# 0 0 == False
print(1 > 2 or 1 > 3)


