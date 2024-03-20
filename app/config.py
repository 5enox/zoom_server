import requests
import json
import requests
import json

url = "http://127.0.0.1:5000/schedule_meeting"
payload = {
    "meeting_id": '554654654658',
    "password": '12Abdocv@',
    "time": '2:21',
    "date": '20',
    "duration": '10'
}

try:
    response = requests.post(url, json=payload)
    response.raise_for_status()  # Raise an exception if the request was unsuccessful
    print(response.text)  # Print the response content
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
