from utils.jalali import *
from helper.email_validation import isValid

print(Gregorian('2022-6-6').persian_string())

print(Persian('1393/1/11').gregorian_string("{}/{}/{}"))

print(isValid("name.surname@gmail.com"))
print(isValid("anonymous123@yahoo.co.uk"))
print(isValid("anonymous123@...uk"))
print(isValid("...@domain.us"))
