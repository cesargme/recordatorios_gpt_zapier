import PySimpleGUI as sg
import gpt

# Diseño de la interfaz gráfica

prompt = "recuardame llamar a mi mamá mañana a las 3 de la tarde"

layout = [
    [sg.Text("Ingrese el texto del recordatorio (máximo 3 líneas):")],
    [sg.Multiline(size=(40, 3), key='texto', default_text=prompt)],
    [sg.Button("Enviar"), sg.Button("Cancelar")]
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
        respuesta = gpt.procesar_texto_con_gpt4(texto=texto)
        sg.popup("Texto recibido:", respuesta)  # Solo para propósitos de demostración

window.close()
