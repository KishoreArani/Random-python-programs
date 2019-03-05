'''
Python program to generate QR Code using pyqrcode module.
'''

import pyqrcode
from pyqrcode import QRCode

#String which represent the QR Code
s = "Hello World!!!"

#Generate QR Code
url = pyqrcode.create(s)

#save using .svg extension
url.svg("myqr.svg",scale = 8)

#check out myqr.svg
#Scan the QR Code and it will display "Hello World!!!"
