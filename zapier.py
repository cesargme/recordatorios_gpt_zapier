import requests

def enviar_a_zapier_webhook(datos, url_webhook):
    try:
        response = requests.post(url_webhook, json=datos)
        return response.status_code, response.text
    except Exception as e:
        print(f"Error al enviar datos a Zapier: {e}")
        return None, None
