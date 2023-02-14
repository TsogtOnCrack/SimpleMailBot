import email.message
import ssl
import smtplib

# SET VARIABLES HERE:

# here you enter the email you want to send from.
email_sender = "email_of_sender@gmail.com"
# this is where you put the generated app password from google.
email_password = "password"
email_receivers = [  # here you enter your list of email recipients in object(library) form.
    {
        "email": "example@gmail.com",
        "name": " Mr/Ms Example",
        # you may add any number of variables.
        # ex:
        # "age" : 69,
    },
    {
        "email": "example2@gmail.com",
        "name": " Mr/Ms Example2",
        # "age" : 420,
    }
]

# for loop that goes through every object in email_recievers list.
for email_receiver in email_receivers:

    # enter your Email Template here:
    subject = f""" Hello { email_receiver["name"]}. """
    body = f"""
    This is the place you write your template
    
    With as many \n space as you want
    
        Even this will work
        
    you can take variables aswell: {email_receiver} would be very happy to hear from you :)
    
    """
    
    # Sending Mail Part:
    em = email.message.EmailMessage()
    
    em["From"] = email_sender
    em["To"] = email_receiver["email"]
    em["Subject"] = subject
    em.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver["email"], em.as_string())
