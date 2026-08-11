import smtplib

sender = "januharshith278@gmail.com"
password = "qwkz rhcv ynng xksm"
receivers =["januharshith278@gmail.com"]

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login(sender,password)

for email in receivers:
    message = f"""subject:hello,

python class"""
    server.sendmail(sender,email,message)
print("all emails sent")
server.quit()
