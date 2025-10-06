from flask import Flask, render_template, request
import requests

app = Flask(__name__)
API_KEY = "c44727b431e8a12e8b019b9fdf9bb4a4"

@app.route("/", methods=["GET", "POST"])
def home():
    weather_data = ""


    return render_template("index.html", weather_data=weather_data)

if __name__ == "__main__":
    app.run(debug=True)
