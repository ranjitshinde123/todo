import json

import requests

url = "https://gst-return-status.p.rapidapi.com/free/gstin/27AAJCM9929L1ZM"

headers = {
   "Content-Type": "application/json",
   "X-RapidAPI-Key": "9d4f704fa9mshbbd4860ea13a21ap1148c3jsn37bf0a5e92cd",
   "X-RapidAPI-Host": "gst-return-status.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)
a=response.text
json_object = json.loads(a)
print(json_object)
address=json_object['data']['adr']


if address=="":
   print("invalid Gst")
else:
   tradename = json_object['data']['lgnm']
   gstin = json_object['data']['gstin']
   address = json_object['data']['adr']

   print(tradename)
   print(gstin)
   print(address)