from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
import qrcode
import os

app = FastAPI()

QR_DIRECTORY = "./qr_codes"
if not os.path.exists(QR_DIRECTORY):
    os.makedirs(QR_DIRECTORY)

@app.get("/")
def read_root():
    return {"message": "Generador de QR para Wi-Fi"}

@app.post("/generate-qr/")
def generate_qr(ssid: str, password: str, encryption: str = "WPA"):
    # Validación básica de entradas
    if not ssid or not password:
        raise HTTPException(status_code=400, detail="SSID y contraseña son requeridos")
    if encryption not in ["WEP", "WPA", "nopass"]:
        raise HTTPException(status_code=400, detail="El tipo de cifrado debe ser WEP, WPA, o nopass")

    wifi_string = f"WIFI:T:{encryption};S:{ssid};P:{password};;"
 
    # Configuración de QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(wifi_string)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')


    qr_filename = f"{QR_DIRECTORY}/{ssid}.png"
    img.save(qr_filename)

    return {"qr_code_path": qr_filename}

@app.get("/qr/{ssid}")
def get_qr(ssid: str):
    qr_filename = f"{QR_DIRECTORY}/{ssid}.png"
    if not os.path.exists(qr_filename):
        raise HTTPException(status_code=404, detail="Código QR no encontrado")
    return FileResponse(qr_filename)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
