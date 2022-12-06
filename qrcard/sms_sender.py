import smtplib
from email.message import EmailMessage

def send_sms(subject, body, phone_number, phone_carrier):

	"""Send an SMS to a specified number on a specified carrier.

	Parameters
	----------
	subject : str
		The subject of the message.

	body : str
		The body of the message.

	phone_number : str
		The recipient's phone number

	phone_carrier : str
		The abreviation of the phone carrier.
		Must be in [att, tmobile, verizon, sprint].
		The recipient's mobile carrier must be known.
	"""


	CARRIERS = {
    "att": "@mms.att.net",
    "tmobile": "@tmomail.net",
    "verizon": "@vtext.com",
    "sprint": "@messaging.sprintpcs.com"
    }

	msg = EmailMessage()
	msg.set_content(body)
	msg['subject'] = subject
	msg['to'] = phone_number + CARRIERS[phone_carrier]

	user = "halavicii@gmail.com"
	msg['from'] = user
	password = "bupemlmdnhewjsmx"

	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login(user,password)
	server.send_message(msg)
	server.quit()

	return

