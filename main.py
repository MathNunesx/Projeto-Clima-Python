 # projeto clima
import requests

API_KEY = "fa7012548c245791a8d06c6081c56394"

city = "Guarulhos"

link = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&lang=pt_br"

request = requests.get(link)
# print(request) funcionou a requisição! (código 200)
request_dicionario = request.json()
descricao = request_dicionario['weather'][0]['description']
temperatura = request_dicionario['main']['temp'] - 273.15
print(descricao, f"{temperatura}°C")
