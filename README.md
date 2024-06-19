---- Generador de QR para WIFI ----


~ Descripción ~

Este proyecto genera códigos QR para la configuración de redes Wi-Fi utilizando FastAPI.

~ Requisitos ~

- Python 3.7+
- Virtualenv (opcional pero recomendado)


~ Instala las dependencias ~


pip install -r requirements.txt


~ Ejecuta la aplicación ~

uvicorn main:app --reload

## Abre tu navegador y ve a `http://127.0.0.1:8000/docs` para acceder a la interfaz Swagger UI y probar los endpoints ~

~ Endpoints ~

- `POST /generate-qr/`: Genera un código QR para la configuración de una red Wi-Fi.
- `GET /qr/{ssid}`: Obtiene el código QR generado basado en el SSID.

