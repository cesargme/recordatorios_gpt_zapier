import PySimpleGUI as sg
import gpt
import zapier
import os

# Diseño de la interfaz gráfica

webhook_url = os.getenv("ZAPIER_WEBHOOK_RECODATORIOS")

# prompt = "recuérdame ver mi carpeta mañana a las 3 de la tarde"
prompt = ""


layout = [
    [sg.Text("Ingrese el texto del recordatorio (máximo 3 líneas):")],
    [sg.Multiline(size=(40, 3), key='texto', default_text=prompt)],
    [sg.Button("Enviar", size=(20, 1), button_color=("white", "blue")), sg.Button("Cancelar")]
]

# Crear la ventana
window = sg.Window("Enviar Recordatorio a Zapier", layout)

# Event loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancelar':
        break
    if event == 'Enviar':
        texto = values['texto']
        # Aquí iría el código para procesar el texto con GPT-4 y enviar a Zapier
        detalles_evento = gpt.extraer_detalles_evento(texto=texto)
        datos = {'evento': detalles_evento}
        status, response = zapier.enviar_a_zapier_webhook(datos, webhook_url)
       
        sg.popup("Se envió a zapier para que lo ponga en el 📅 Calendario.")  # Solo para propósitos de demostración
        
        #cerrar aplicativo
        break

window.close()

