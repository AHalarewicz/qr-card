import sys
import logging
import click
from qrcard import pipelines

logging.basicConfig(
    format='[%(asctime)s|%(module)s.py|%(levelname)s]  %(message)s',
    datefmt='%H:%M:%S',
    level=logging.INFO,
    stream=sys.stdout
)

@click.command()
@click.option('--url_string',
              type=str,
              prompt='URL for QR Code redirect.',
              help='URL for QR Code redirect.')
# @click.option('--qrcode_filename',
#               type=str,
#               prompt='Save QR Code png file as filepath.',
#               help='Provide the name and filepath for saving the QR Code png.')
# @click.option('--qrcode_scale',
#               type=int,
#               prompt='Scale factor for QR Code size (integer).',
#               help='Default value is 6.')

def generate_qrcode(url_string="instagram.com", qrcode_filename="qrcodes/qrcode.png", qrcode_scale=6):
    pipelines.run_generate_qrcode(url_string, qrcode_filename, qrcode_scale)
    