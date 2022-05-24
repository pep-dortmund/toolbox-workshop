# Requires:
# pip install qrcode

import qrcode

qr = qrcode.QRCode(version = 1,
                    box_size = 10,
                    border = 1)
qr.add_data('https://toolbox.pep-dortmund.org')
qr.make(fit=True)

img = qr.make_image(fill_color='black', back_color='white')
img.save('toolbox_qrcode.png')
