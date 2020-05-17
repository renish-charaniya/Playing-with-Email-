import smtplib 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#environment variables
username='<Your Email>' #Please make sure to Turn On Less Secure Apps option in Google Account Security
password='<password>'

def send_mail(text='Email Body',subject='Hello World',from_email='Renish Charaniya < your email >',to_emails=None,html=None):
    assert isinstance(to_emails,list)
    msg=MIMEMultipart('alternative')
    msg['From']=from_email
    msg['To']=", ".join(to_emails)
    msg["Subject"]=subject

    txt_part=MIMEText(text,'plain text')
    msg.attach(txt_part)
    if html != None:
        html_part=MIMEText(html,'HTML')
        msg.attach(html_part)

    msg_str=msg.as_string()
    #login smtp server
    server=smtplib.SMTP(host='smtp.gmail.com',port=587)
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail(from_email,to_emails,msg_str)

    server.quit()
