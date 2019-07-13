# -*- coding: utf-8 -*-

# Step3 ----> Functional GUI
from flask import Flask, render_template, request, url_for
from data import years, result

app = Flask(__name__)

@app.route("/home", methods=["GET"])
def home():
    season = request.form.get("Season")
    year = years(season)
    return render_template("home.html", year=year)

@app.route("/medal_tally")
def medal_tally():
    data = request.form
    Season = data["Season"]
    year = int(data["year"])
    tally = result(Season, year)
    return render_template("result.html", data=tally.to_html())

if __name__ == "__main__":
    app.run(debug=True)