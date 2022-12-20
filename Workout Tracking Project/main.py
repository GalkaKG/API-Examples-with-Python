import requests
from datetime import datetime

APP_ID = "98f18746"
APP_KEY = "41311b21e5e2da0a03b2c6236edfe327"
GENDER = "female"
WEIGHT_KG = 57
HEIGHT_SM = 169
AGE = 32

post_url = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("What exercise did you do today/for how long? ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    "x-remote-user-id": "0"
}
post_request_body = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_SM,
    "age": AGE
}

response = requests.post(post_url, json=post_request_body, headers=headers).json()

sheet_post_url = "https://api.sheety.co/18bd71949a555718927f71eb28779c41/workoutTracking/workouts"
date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%H:%M:%S")
exercise = response['exercises'][0]['user_input']
duration = response['exercises'][0]['duration_min']
calories = response['exercises'][0]['nf_calories']

sheet_inputs = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories
    }
}

# Bearer Token Authentication
bearer_headers = {
    "Authorization": "Bearer XMXM"
}
sheet_response = requests.post(sheet_post_url, json=sheet_inputs, headers=bearer_headers)

print(sheet_response.text)
