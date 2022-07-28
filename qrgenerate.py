# Import QRCode from pyqrcode

import pyqrcode
from pyqrcode import QRCode

# URL string
site = "YOUR PHONE HAS BEEN HACKED"

# Generate QR code
getqrcode = pyqrcode.create(site)

# save in svg file format
getqrcode.svg("qrcode.svg", scale=10)
