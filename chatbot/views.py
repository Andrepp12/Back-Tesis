from django.http import JsonResponse
import google.generativeai as genai
import json  # Importa json para manejar el cuerpo de la solicitud
from django.views.decorators.csrf import csrf_exempt

# Configura la API de Gemini
genai.configure(api_key="AIzaSyAzPWlk3Bqek9FDrDY0CPLm4ZgcbR7XAQU")

@csrf_exempt
def ask_question(request):
    if request.method == "POST":
        try:
            # Cargar el cuerpo de la solicitud como JSON
            body = json.loads(request.body)
            text = body.get("content", "").strip()  # Obtén 'content' y elimina espacios en blanco

            if not text:
                return JsonResponse({"error": "El contenido no puede estar vacío."}, status=400)

            model = genai.GenerativeModel("gemini-pro")
            chat = model.start_chat()
            response = chat.send_message(text)

            # Extraer datos necesarios de la respuesta
            response_data = {
                "text": response.text,  # Asumiendo que response.text contiene la respuesta relevante
                # Agrega otros datos relevantes de la respuesta si es necesario
            }

            print(response.text)

            return JsonResponse({"data": response_data})

        except json.JSONDecodeError:
            return JsonResponse({"error": "Error al decodificar el JSON."}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    else:
        return JsonResponse({"error": "Invalid request method."}, status=400)
