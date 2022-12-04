from qrcard.generate_qrcode import generate_and_save_qrcode
from os.path import exists

def test_generate_and_save_qrcode():

	generate_and_save_qrcode("https://github.com/AHalarewicz/qr-card",
						  "tests/test_qrcode.png",
						  6)

	assert exists("tests/test_qrcode.png")