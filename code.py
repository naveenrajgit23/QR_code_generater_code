
import segno

# Website URL
data = "http://rut.kpriet.ac.in/"

# Generate QR code
qr = segno.make(data, error="L")

# Save QR code as PNG
qr.save(
    "static_qr_code.png",
    scale=10,
    border=4,
    dark="black",
    light="white"
)

print("QR code generated successfully!")
print("Saved as: static_qr_code.png")
