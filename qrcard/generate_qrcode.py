import logging
import pyqrcode
import png
from pyqrcode import QRCode

def generate_and_save_qrcode(url_string="google.com", 
							 qrcode_filename="qr_code.png",
							 qrcode_scale=6):
		
	"""Create and save a QRCode from a provided url string
		Parameters
	    ----------
	    url_string : str
	    	url of redirect site.

	    qrcode_filename : str
	    	the name for QR Code PNG file.

	    qrcode_scale : int
	    	the scale factor for the QR Code.
	    	
	    Returns
	    -------
	    Saves a QR to the local directory
	    """	


	"""Create and save a QR Code from a provided url string, output filename, and size.
	url_string: the url to which the qr code will redirect.
	qrcode_filename: the name of the file to save the QR code as.
	size: a simple scale metric for the QR Code output.
	"""

	# Create and save QR code
	url = pyqrcode.create(url_string)

	# Create and save the png file with the specified name
	url.png(qrcode_filename, qrcode_scale)
