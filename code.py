import qrcode

# Data to encode in the QR code
data = "http://rut.kpriet.ac.in/"

# Create a QR Code object
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # error correction level
    box_size=10,  # size of each box in the QR code grid
    border=4,  # border width
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image of the QR code
img = qr.make_image(fill='black', back_color='white')

# Save the image
img.save("static_qr_code.png")

print("QR code generated and saved as static_qr_code.png")
