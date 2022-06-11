import _csv

data = open("1.csv")
mydata = _csv.reader(data)
# print(list(mydata)[3:9])
mydata_value = []
for item in list(mydata):
    mydata_value.append(item[2])

print(mydata_value)
ddd = open('1.txt', "w")
for i in mydata_value:
    ddd.write(i + "\n")
ddd.close()