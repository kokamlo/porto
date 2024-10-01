import smtplib , ssl
import os 



def send_email(message):
    user_name= 'behzad0hosseinzadeh@gmail.com'
    password = os.getenv('PassWord')

    host = 'smtp.gmail.com'
    port = 465

    reciver = 'behzad0hosseinzadeh@gmail.com'
    my_context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host , port , context=my_context) as server:
        server.login(user_name , password)
        server.sendmail(user_name , reciver , message)