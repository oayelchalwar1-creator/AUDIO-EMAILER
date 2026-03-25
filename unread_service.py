import imaplib
import email

def get_server(provider):

    if provider == "gmail":
        return "imap.gmail.com"

    if provider == "outlook":
        return "imap-mail.outlook.com"

    return "imap.mail.yahoo.com"


def fetch_unread(provider, user, password):

    server = get_server(provider)

    mail = imaplib.IMAP4_SSL(server)

    mail.login(user, password)

    mail.select("inbox")

    # search for unread emails
    status, data = mail.search(None, "UNSEEN")

    email_ids = data[0].split()

    return mail, email_ids
def read_unread_emails(provider, user, password):

    mail, email_ids = fetch_unread(provider, user, password)

    messages = []

    if len(email_ids) == 0:
        return []

    for num in email_ids:

        status, msg_data = mail.fetch(num, "(RFC822)")

        msg = email.message_from_bytes(msg_data[0][1])

        body = ""

        if msg.is_multipart():
            for part in msg.walk():

                if part.get_content_type() == "text/plain":

                    body = part.get_payload(decode=True).decode(errors="ignore")
                    break

        else:

            body = msg.get_payload(decode=True).decode(errors="ignore")

        messages.append({
            "from": msg.get("From"),
            "subject": msg.get("Subject"),
            "body": body
        })

    return messages
