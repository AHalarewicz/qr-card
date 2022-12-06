import smtplib
from email.message import EmailMessage

def send_email(subject, body, to):
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

if __name__ == '__main__':
	send_email("mysubject", "mybody", "ahalarewicz@gmail.com")
