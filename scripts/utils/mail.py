import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email():
    # AWS SES SMTP settings
    smtp_server = 'email-smtp.us-west-2.amazonaws.com'
    smtp_port = 587
    smtp_username = ''
    smtp_password = ''

    # Email settings
    from_address = ''
    to_address = ''
    subject = 'Test Subject'
    body = 'This is a test email.'

    # Create MIME email
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Send email
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(from_address, to_address, msg.as_string())
        server.quit()
        print('Email sent successfully.')
    except Exception as e:
        print(f'Failed to send email. Error: {e}')

if __name__ == '__main__':
    send_email()
