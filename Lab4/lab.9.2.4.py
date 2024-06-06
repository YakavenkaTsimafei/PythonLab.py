import qrcode
from PIL import Image
from pyzbar.pyzbar import decode

def generate_qr_code_from_text(text):
    # Create QR code object
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add text to be encrypted into the QR code
    qr.add_data(text)
    qr.make(fit=True)

    # Create QR code image
    qr_image = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code image
    qr_image.save("encrypted_qr_code.png")

    print("QR code successfully created and saved in 'encrypted_qr_code.png'")

def decrypt_qr_code(image_filename):
    # Load QR code image
    image = Image.open(image_filename)

    # Decode text from QR code image
    decoded_data = decode(image)
    if decoded_data:
        decrypted_text = decoded_data[0].data.decode("utf-8")
        print("Decrypted text from QR code:", decrypted_text)
    else:
        print("Failed to decrypt QR code.")

# Pass the text to be encrypted into the QR code
#generate_qr_code_from_text("Hello, world!")

# Decrypt text from the QR code
decrypt_qr_code("encrypted_qr_code.png")
