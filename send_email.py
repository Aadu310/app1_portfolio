import smtplib,ssl

host = "smtp.gmail.com"
port = 465
context = ssl.create_default_context()

username = "ettaki23@gmail.com"
password = "ngbkrrgqsjdkwjac"

receiver = "adarshmanjunath88@gmail.com"

message = '''
Hi,
How are you?
'''

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.ehlo()
    server.login(username, password)
    server.sendmail(username, receiver, message)