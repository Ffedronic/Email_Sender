import requests
from send_email import send_email

api_key = "pub_8f605b616676486aad6ca5f2d706bbf7"
url = f"https://newsdata.io/api/1/latest?apikey={api_key}&country=fr"

response = requests.get(url)
data = response.json()
content = []
body = ""

for index, article in enumerate(data["results"]) :
    body = body + "\n" + article["title"] + "\n" + article["description"] + "\n"*2

body = body.encode("utf-8")
send_email(content=body)