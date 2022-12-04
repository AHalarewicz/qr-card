import logging

def generate_and_save_qrcode(url_string="google.com", 
							 qrcode_filename="qr_code.png",
							 qrcode_scale=6):
		
	"""Create and save a QRCode from a provided url string
		Parameters
	    ----------
	    df : pandas.DataFrame
	        Data-frame containing the column `Name`
	    Returns
	    -------
	    pandas.DataFrame
	        Data-frame with additional column with titles
	    """	


	"""Create and save a QR Code from a provided url string, output filename, and size.
	url_string: the url to which the qr code will redirect.
	qrcode_filename: the name of the file to save the QR code as.
	size: a simple scale metric for the QR Code output.
	"""

	# Create and save QR code
	url = pyqrcode.create(url_string)

	# Create and save the png file with the specified name
	url.png(qrcode_filename, scale)
