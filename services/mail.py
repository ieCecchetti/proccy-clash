import smtplib
from email.message import EmailMessage

from config.mail import SMTP_SERVER, SMTP_PORT, SMTP_USERNAME, SMTP_TOKEN


def send_mail(sender, target, subject, message=None, file_url=None, zip_url=None):
    """
    :param sender: our account. Mail from where we write
    :param target: target mail. mail account receiving the file
    :param subject: subject of the mail. Must be inserted or will be labeled as spam
    :param message: text message, or body of the mail
    :param file_url: some file sended, or image or whatever
    :param zip_url: zipped file to include in the mail as attached file
    :return:
    """

    # Create message specifications
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = target

    # Add some message if exists
    if message:
        msg.set_content('message')

    if file_url:
        # Add file or something to the body
        with open('file.txt', 'rb') as f:
            file_data = f.read()
        msg.add_attachment(file_data, maintype='text', subtype='plain', filename=file_url)

    if file_url:
        # Add file or something to the body
        with open('archive.zip', 'rb') as f:
            file_data = f.read()
            msg.add_attachment(file_data, maintype='application', subtype='zip', filename=zip_url)

    # Send post message
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_TOKEN)
        server.send_message(msg)