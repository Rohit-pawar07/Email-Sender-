import smtplib
sender_email = "<change here>"
rec_email = "<change here >"
password = '<change here>'
message = "This is test email sent using python script. Please do not reply to this mail !"

server = smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.login(sender_email,password)
print("Login Successful !")
server.sendmail(sender_email,rec_email,message)
print("Email has been successfully sent ")
