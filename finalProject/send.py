import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from platform import python_version

def sendMessage(txt, keys, ml):
    server = 'smtp.gmail.com'
    user = 'resttsg@gmail.com'
    password = 'rest229916'

    recipients = ml
    sender = 'resttsg@gmail.com'
    text = txt
    key = f"твой ключ {keys} !!!!!"
    html = '<html><head>' + key + '</head><body><p>' + text +'</p></body></html>'

    msg = MIMEMultipart('alternative')
    msg['From'] = 'Python script <' + sender + '>'
    msg['To'] = recipients
    msg['Reply-To'] = sender
    msg['Return-Path'] = sender
    msg['X-Mailer'] = 'Python/' + (python_version())

    part_text = MIMEText(text, 'plain')
    part_html = MIMEText(html, 'html')

    msg.attach(part_text)
    msg.attach(part_html)

    mail = smtplib.SMTP_SSL(server)
    mail.login(user, password)
    mail.sendmail(sender, recipients, msg.as_string())
    mail.quit()



