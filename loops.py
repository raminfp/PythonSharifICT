
# for item in object:
#   do_anything
# lst = [1, 2, 3, 4, 5, 6]
# for item in lst:
#     print(item)
#
# new_lst = list()
# sum_ = 0
# for i in range(len(lst)):
#     sum_ += lst[i]
# avg = sum_ / len(lst)
# print("Avg : ", avg)
# for item in lst:
#     if int(avg) >= item:
#         continue
#     new_lst.append(item)
# print("New list greater of AVG :", new_lst)

# d = ["H", "E", "L", "L", "O"]
# chr_ = ["h", "e", "l", "l", "o"]
# s = "hello"
# new_str = ""
# for item in s:
#     for i in range(len(chr_)):
#         if item == chr_[i]:
#             new_str += d[i]
#             break
# print(new_str)

# my_tuple = (1, 2, 3, 4)
# my_tuple = [(1, 2), (1, 3), (2, 4)]
# # for item in my_tuple:
# #     print(item)
# for (t1, t2) in my_tuple:
#     print(t1, t2)

# my_dict = {'k1': 1, 'k2':2}
# for key, value in my_dict.items():
#     print(key, value)
#
# for key in my_dict.keys():
#     print(key)
#
# for value in my_dict.values():
#     print(value)

x = 0
while x < 10:
    if x == 3:
        x += 1
        # print("OKOK")
        continue

    if x == 6:
        break
    print("X is %s" % x)
    x += 1
else:
    print("All done!")