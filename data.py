import requests

gender_api = "https://api.genderize.io"
age_api = "https://api.agify.io"

parameters = {
    "name":"balaji"
}

gender_response = requests.get(url=gender_api,params=parameters)
gender_data = gender_response.json()["gender"]

age_response = requests.get(url=age_api,params=parameters)
age_data = age_response.json()["age"]

print(age_data)
print(gender_data)

