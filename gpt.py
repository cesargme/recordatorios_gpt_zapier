import openai
import os
import json
from datetime import date
from datetime import timedelta

usar_gpt_4 = False


def str_to_dict(func):
    def wrapper(*args, **kwargs):
        result_str = func(*args, **kwargs)
        try:
            result_dict = json.loads(result_str)
            return result_dict
        except json.JSONDecodeError:
            print(
                "Error al convertir la cadena a diccionario. Asegúrate de que la salida sea un JSON válido."
            )
            return None

    return wrapper


@str_to_dict
def extraer_detalles_evento(texto):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    prompt = f"""
    Texto: {texto}
    Extraer los detalles del evento en formato de diccionario. Incluir hora de inicio, hora de fin y resumen del evento. Formatear las fechas y horas en formato ISO 8601 (AAAA-MM-DDThh:mm:ss).
    
    Contexto:
    Hoy es: {date.today()}
    mañana es: {date.today() + timedelta(days=1)}

    Ejemplo de salida esperada:
    {{
        "hora_inicio": "2023-05-20T15:00:00",
        "hora_fin": "2023-05-20T16:00:00",
        "resumen": "Reunión con el equipo de proyecto"
    }}
    
    Salida:
    """

    model = "gpt-4-1106-preview" if usar_gpt_4 else "gpt-3.5-turbo-instruct"

    try:
        response = openai.Completion.create(
            model=model,  # o el modelo de GPT-4 que prefieras
            prompt=prompt,
            max_tokens=150,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error al procesar el texto: {e}")
        return None


if __name__ == "__main__":
    # Ejemplo de uso
    texto = "recuardame llamar a mi mamá mañana a las 3 de la tarde"
    detalles_evento = extraer_detalles_evento(texto)
    print(detalles_evento)
    print(type(detalles_evento))
