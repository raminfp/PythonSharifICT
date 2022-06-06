# Read File
fp = open("tmp/readme")
msg = fp.readline()
while msg != "":
    # print(msg.replace("\n", ""))
    msg = fp.readline()
# fp.seek(0)# start to file index 0
# print(fp.read())
fp.close()

# Write File
fw = open("tmp/test.txt", "a+")
# fr = open("tmp/test.txt")
fw.write("this is a test\n")
fw.close()
# fr.seek(0)
# print(fr.read())

# fr.close()

for line in open("tmp/test.txt"):
    print(line.replace("\n", ""))


