import os
from dotenv import load_dotenv
import requests
from send_email import send_email

load_dotenv()

api_key = str(os.getenv("API_KEY"))

url = f"https://newsdata.io/api/1/latest?apikey={api_key}&country=fr"

response = requests.get(url)
data = response.json()
content = []
body = ""

for article in data["results"] :
    body = body + article["title"] + "\n" + article["description"] + "\n"*2

body = body.encode("utf-8")
send_email(content=body)