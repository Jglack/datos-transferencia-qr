import qrcode
from PIL import Image
import os

CARPETA = r"C:\Users\Jglack\Documents\Freelance\datos-transferencia-qr"

def generar_qr(contenido, nombre_archivo="qr", color="#000000", fondo="#ffffff"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(contenido)
    qr.make(fit=True)

    img = qr.make_image(fill_color=color, back_color=fondo)

    if not nombre_archivo.endswith(".png"):
        nombre_archivo += ".png"

    ruta = os.path.join(CARPETA, nombre_archivo)
    img.save(ruta)
    print(f"QR guardado en: {ruta}")

if __name__ == "__main__":
    print("=== Generador de QR ===")
    contenido = input("Texto o URL: ").strip()
    nombre = input("Nombre del archivo (sin extensión) [qr]: ").strip() or "qr"
    color = input("Color del QR en hex [#000000]: ").strip() or "#000000"
    fondo = input("Color de fondo en hex [#ffffff]: ").strip() or "#ffffff"

    generar_qr(contenido, nombre, color, fondo)
