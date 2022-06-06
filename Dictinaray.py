# Create Dict
# Accessing to dict
# Nesting Dict
# Basic dict methods
my_dict = {1: "value1", 2: "value2", "asdad": 123}
print(my_dict)
print(type(my_dict))
print(my_dict[1])
print(my_dict[2])
print(my_dict["asdad"])

my_dict_2 = {'key1': 123, 'key2': [1, 2, 3, 4], 'key3': "ok %s"}
print(my_dict_2["key2"][2])
print(my_dict_2["key3"] % "python")
my_dict_2['key1'] += 10
print(my_dict_2['key1'])

# new_dict = {} # general python
newDict: dict[str, str] = {} ## mypy
newDict["animal"] = "dog"
newDict["answer"] = "OK"
print(newDict)
# Nested dict
my_d = {'key1': {"nestkey1": "nestvalue1", "nestkey2": "nestvalue2"}, "key2": "value2"}
my_d2 = {'key1': [1,2,3,4,5], "key2": "value2"}
print(my_d)
print(my_d2)
# Methods
print(my_dict.items())
print(my_dict.values())
print(my_dict.keys())
print(my_dict.get(1))
print(my_dict.pop(1))
print(my_dict)
my_dict.update({"ok": 11})
print(my_dict)
# my_dict.clear()
# print(my_dict)
copy_dict = my_dict.copy()
dd = my_dict
my_dict.clear()
print(my_dict)
print(copy_dict)
print(dd)








