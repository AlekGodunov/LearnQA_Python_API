import json
import requests
import time


response1 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
time_wait = json.loads(response1.text)["seconds"]
token = json.loads(response1.text)["token"]

payload = {"token": f"{token}"}
response2 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=payload)
assert json.loads(response2.text)["status"] == 'Job is NOT ready', "Task hasn't status ready"
time.sleep(time_wait)
response3 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=payload)
assert json.loads(response3.text)["status"] == 'Job is ready', "Time execution task is not over yet"
assert json.loads(response3.text)["result"] != 0, "No result"