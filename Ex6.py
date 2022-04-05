import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
url_responce = 0
for i in response.history:
    url_responce += 1
print(url_responce)
print(response.url)