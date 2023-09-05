import qrcode

qr =qrcode.QRCode(version=1,
              error_correction=qrcode.constants.ERROR_CORRECT_L,
              box_size=20,
              border=2
              )

qr.add_data("https://www.youtube.com/watch?v=l4ugfcj7qrI")
qr.add_data("sì sì")
qr.make(fit=True)
img = qr.make_image()

img.save("ricardo1.png")


import qrcode
img1 = qrcode.make("ez")
img1.save("test.png")