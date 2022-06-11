# s = set()
#
#
# s.add(1)
# s.add(2)
#
# print(s)
#
# # s.clear()
# # print(s)
#
# sc = {2, 3, 4}
# print(sc)
#
# print(s.difference(sc))
#
# s1 = {1, 2, 3}
# s2 = {1, 2, 5}
# s1.difference_update(s2)
# # print(s1)
# s1 = {1, 2, 3, 4}
# s1.discard(2)
# print(s1)
#
# s1 = {1, 2, 3}
# s2 = {1, 2, 4}
# s1.intersection_update(s2)
# print(s1)

# s1 = {1, 2}
# s2 = {1, 2, 4}
# s3 = {5}

# s1.isdisjoint(s2)
# print(s1)
s1 = {1, 2}
s2 = {1, 2, 4}

d = s1.union(s2)
print(d)

s1.update(s2)
print(s1)

