# inject az variable to string
name = "python"
msg = "this is " + name + " lang" # concat
msg_2 = f'this is {name} lang' # formatting
print(msg)
print(msg_2)
# PlaceHolder :  %s, %d, ...
print("this is a %s,%s lang" % ("python", "go"))
python = "python"
golang = "go"
print("this is a %s,%s lang" % (python, golang))

print('this is a %s' % 'python')
print('this is a %r' % 'golang')

print('this is a %s' % 'golang\t Ok')

print('this is a integer %s' % 3.5)
print('this is a integer %d' % 4.1)

print('Floating point  numbers: %5.2f' % (13.144))
print('Floating point  numbers: %1.0f' % (13.144))
print('Floating point  numbers: %1.5f' % (13.144))

print('Fisrt: %s, Second: %5.2f Thrid: %r' % ("hi", 3.1432, "OK!"))


print('this is a string of {} lang'.format("python"))
print('this is a string of {} lang'.format("go"))

print('this is a string of {2} {1} {0} lang'.format("go", "python", "php"))
