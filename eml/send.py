import smtplib
import getpass

smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
smtp_object.ehlo()
smtp_object.starttls()
email = getpass.getpass("Enter your email: ")
password = getpass.getpass("Enter your password : ")
smtp_object.login(email, password)
from_addres = getpass.getpass("Enter your email: ")
to_address = getpass.getpass("Enter the email of the recipient")
subject = input("Enter you subject email : ")
message = input("Type your message for this email: ")
msg = f"Subject: {subject}" + '\n' + message
smtp_object.sendmail(from_addres, to_address, msg)



