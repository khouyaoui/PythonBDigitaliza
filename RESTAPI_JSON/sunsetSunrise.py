import requests

url = "https://api.sunrise-sunset.org/json"

# latitud y longitud de Barcelona Spain
querystring = {"lat":"41.3828939","lng":"2.1774322"}

response = requests.request("GET", url, params=querystring)

resultado=response.json()["results"]

#print("Las horas obtenidas para latitud y longitud de barcelona son: ",response.text)

print("Datos obtenidos:\n")

print("{} ==> {}".format(querystring,"Barcelona"),"\n")

for item in resultado:
#    if(resultado[item]!="OK"):
#       print("\n")
#       print(resultado[item],"\n")
    print("{} = {}".format(item, resultado[item],"\n"))