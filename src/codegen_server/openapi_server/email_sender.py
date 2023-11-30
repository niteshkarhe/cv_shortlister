import smtplib
from email.message import EmailMessage

def send_email_gmail(subject, message, destination):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    #This is where you would replace your password with the app password
    server.login('service.punebot@gmail.com', 'nrdnfjcpruhgysni')

    msg = EmailMessage()

    message = f'{message}\n'
    msg.set_content(message)
    msg['Subject'] = subject
    msg['From'] = 'me123@gmail.com'
    msg['To'] = destination
    server.send_message(msg)

send_email_gmail('Python Email', 'This is the python generated email', 'nilgattani@gmail.com')