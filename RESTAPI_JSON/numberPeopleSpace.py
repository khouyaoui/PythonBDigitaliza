import requests

url = "http://api.open-notify.org/astros.json"

response = requests.request("GET", url)

print("Segun Open APIs From Space, el numero de personas que si encuentran en el espacio es: ",response.json()["number"])
