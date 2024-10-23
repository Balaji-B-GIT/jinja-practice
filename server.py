from flask import Flask, render_template
import datetime as dt
import requests

gender_api = "https://api.genderize.io"
age_api = "https://api.agify.io"

app = Flask(__name__)

now = dt.datetime.now()
current_year = now.strftime("%Y")



@app.route('/')
def func():
    return "<h1>Goto '/guess/your name' to find out your age and gender<h1>"

@app.route("/guess/<name>")
def guess(name):
    parameters = {
        "name": name
    }
    gender_response = requests.get(url=gender_api, params=parameters)
    age_response = requests.get(url=age_api, params=parameters)

    gender_data = gender_response.json()["gender"]
    age_data = age_response.json()["age"]
    return render_template("index.html",gender = gender_data,age = age_data, name = name)

if __name__ == "__main__":
    app.run(debug=True)