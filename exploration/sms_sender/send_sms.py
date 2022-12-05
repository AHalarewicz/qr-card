import smtplib
from email.message import EmailMessage

def send_sms(subject, body, phone_number, phone_carrier):

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


if __name__ == '__main__':
	send_sms("testsubject", "python test", "3107419469" , "att")
