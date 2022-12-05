import logging 
from qrcard import generate_qrcode

def run_generate_qrcode(url_string="google.com", qrcode_filename="qr_code.png", qrcode_scale=6):
	"""Command Line function to generate and save a QR Code.

	Parameters
	----------
	url_string: str
		The url that the QR Code will point to.

	qrcode_filename: str
		Path and filename for saving the QR Code.

	qrcode_scale: int
		Scale factor of QR Code size.
	"""

	logging.info("Starting the QR Code generator")

	generate_qrcode.generate_and_save_qrcode(url_string, qrcode_filename, qrcode_scale)

	logging.info("The QR Code has been generated and saved.")
	
	return


