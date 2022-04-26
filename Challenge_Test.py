import smtplib
from email.message import EmailMessage
sendemail = input("Enter sender email address: ")
sendpassword = input("Enter sender password: ")
Entersubject = input("Enter subject title: ")
message_content = input("Enter message: ")
receiveremail = input("Enter receiver email address: ")
msg = EmailMessage()
msg.set_content(message_content)
msg['Subject'] = Entersubject
msg['From'] = sendemail
msg['To'] = receiveremail
try:
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(sendemail, sendpassword)
    server.send_message(msg)
except Exception as e:
    print("You have entered an invaild email")
finally:
    server.quit()

print("Your message had been delivered")
       