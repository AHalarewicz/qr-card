from qrcard import email_sender

def test_email_sender():
	 """Test the sms sender function."""

	 email_sender.send_email("subject_test",
	 					 "body_test",
	 					 "test@gmail.com",
	 					  )