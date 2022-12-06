import smtplib
from email.message import EmailMessage

def send_email(subject, body, to):
	"""Send an SMS to a specified number on a specified carrier.

	Parameters
	----------
	subject : str
		The subject of the message.

	body : str
		The body of the message.

	to : str
		The recipient's email_address
	"""

	msg = EmailMessage()
	msg.set_content(body)
	msg['subject'] = subject
	msg['to'] = to

	user = "halavicii@gmail.com"
	msg['from'] = user
	password = "bupemlmdnhewjsmx"

	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login(user,password)
	server.send_message(msg)
	server.quit()

	return

