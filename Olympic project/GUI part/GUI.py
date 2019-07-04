# -*- coding: utf-8 -*-

# Step3 ----> Functional GUI
from flask import Flask, render_templates, request, url_for
from data import years

app = Flask(__name__)

@app.route("/home", methods=["GET"])
def home():
    season = request.form.get("Season")
    year = years(season)
    return render_templates("home.html", year=year)

@app.route("/medal_tally")
def medal_tally():
    data = request.form
    Season = data["]