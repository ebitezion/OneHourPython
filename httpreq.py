import requests

resp=requests.get("https://data.fixer.io/api/latest")

print(resp.json())

#requests.post()