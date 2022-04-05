import json
import requests
import time

status_response = "Job is NOT ready"
result_response = "Job is ready"
error_response = "No job linked to this token"

response1 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
time_wait = json.loads(response1.text)["seconds"]
token = json.loads(response1.text)["token"]

payload = {"token": token}
response2 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=payload)
if json.loads(response2.text)["status"] == status_response:
    print("Passed status")
else:
    print("Failed status")

time.sleep(time_wait)

response3 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=payload)
if json.loads(response3.text)["status"] == status_response:
    print("Passed status")
else:
    print("Failed status")


if json.loads(response3.text)["result"] == result_response:
    print("Passed result")
else:
    print("Failed result")