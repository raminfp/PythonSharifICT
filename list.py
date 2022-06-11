# create list
# indexing and slice list
# basic list method
# nesting list

# Create list
my_lst = [1, 2, 3, 4, 5]
my_lst2 = ["one", "two", "three"]
my_lst3 = [my_lst2, my_lst]
my_list4 = ["hi", 112, 1.2, False]
print(my_lst)
print(my_lst2)
print(my_lst3)
print(my_list4)
print(len(my_list4))
# Index & Slice
print(my_list4[0])
print(my_list4[1])
print(my_list4[:])
my_list5 = my_list4 + ["hello dady"]
print(my_list5 * 2)

# basic methods
my_list4.append("test")
my_list4.append(12312)
print(my_list4)
print(my_list4.pop())
print(my_list4)
my_lll = ['a', 'e', 'x', 'b', 'c']
print(my_lll)
my_lll.reverse()
print(my_lll)
my_lll.sort()
print(my_lll)
my_lll.extend(("ttt", 11111))
print(my_lll)
# Nesting list
lst_1 = [1, 2, 3]
lst_2 = [4, 5, 6]
lst_3 = [7, 8, 9]
all_lst = [lst_1, lst_2, lst_3]
print(all_lst)
print(all_lst[0][0])
print(all_lst[0][1])
print(all_lst[0][2])

# List Comprehensions
row_lst = [row[1] for row in all_lst]
print(row_lst)
print(type(row_lst))


list1 = [1, 2, 3, 4]
list1.append(5)
print(list1)
print(list1.index(4))

list1.insert(2, "insert")
print(list1)


list1.remove("insert")
print(list1)
