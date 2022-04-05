import requests

response1 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response1.text, response1.status_code)

response2 = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response2.text, response2.status_code)

payload = {"method": "POST"}
response3 = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload)
print(response3.text, response3.status_code)

method = ["GET", "PUT", "POST", "DELETE"]
result = []
for i in method:
    payloads = {"method": i}
    response4 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=payloads)
    response5 = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payloads)
    response6 = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payloads)
    response7 = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payloads)
    result.extend((i, response4.text, response5.text, response6.text, response7.text))
print(result)

