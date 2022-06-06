

# try:
#     d = [1, 2, 3, 4, 5, 6]
#     print(d[9])
# except IndexError:
#     print("Error: we have a error in the my program")
#     # pass
# finally:
#     pass

# try:
#     f = open("test.txt", "r")
#     f.write("this is a test")
# except IOError:
#     print("we have a error in the open the file")
# else:
#     print("Written file is successfully")
#     f.close()

# try:
#     f = open("okokok", "r")
#     f.write("this is a test")
#     f.close()
# except IOError:
#     print("we have a error to write the file")
#
# finally:
#     print("code block is executed")

def askint():
    global val
    while True:
        try:
            val = int(input("Please enter a number : "))
        except:
            continue
        else:
            print("Yep that's an integer")
            break
        finally:
            print("Finally, ")
        print(val)

askint()