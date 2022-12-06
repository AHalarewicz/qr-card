from qrcard import sms_sender

def test_sms_sender():
	 """Test the sms sender function."""

	 sms_sender.send_sms("subject_test",
	 					 "body_test",
	 					 "8888888888",
	 					 "att")