import qrcode
path = input("Paste here URL or Text for QrCode: ")

qr = qrcode.QRCode(
    version = 1,  
    error_correction = qrcode.constants.ERROR_CORRECT_H, 
    border = 4,  
)

qr.add_data(path)
qr.make(fit = True)

img = qr.make_image(fill_color = "black", back_color = "white")

img.save("qrcode.png")

print(" QR code generated and saved as qrcode.png")