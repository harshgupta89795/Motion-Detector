import smtplib
from email.message import EmailMessage
import imghdr

password="ugwzhigatcooapmm"

def send_email(image_path):
    email_message=EmailMessage()
    print("Email was sent")
    email_message["Subject"]="New Customer showed up!"
    email_message.set_content("Hey, we just saw a new customer")

    with open(image_path,'rb') as file:
        content=file.read()
    email_message.add_attachment(content,maintype="image",subtype=imghdr.what(None,content))
    gmail=smtplib.SMTP("smtp.gmail.com",587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login("hgagra12@gmail.com",password)
    gmail.sendmail("hgagra12@gmail.com","hgagra12@gmail.com",email_message.as_string())
    gmail.quit()


