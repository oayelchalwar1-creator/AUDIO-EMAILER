import imaplib
import email

def fetch_emails():
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login("your_email@gmail.com", "app_password")

    mail.select("inbox")
    _, data = mail.search(None, "ALL")

    mail_ids = data[0].split()

    emails = []

    for num in mail_ids[-5:]:
        _, msg_data = mail.fetch(num, "(RFC822)")
        msg = email.message_from_bytes(msg_data[0][1])

        emails.append(msg["subject"])

    return emails