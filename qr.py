import qrcode

def create_qr(data, filename="qrcode.png"):
    img = qrcode.make(data)
    img.save(filename)
    return f"QR code saved as {filename}"


