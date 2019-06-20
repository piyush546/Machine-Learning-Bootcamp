"""
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/hello/people', methods=['GET','POST'])
def greet():
    return render_template('main.html')


@app.route('/hello/<name>/<int:age>')
def demo(name, age):
    return "Welcome {0} of {1} years of age".format(name,age)

@app.route('/people', methods=['GET','POST'])
def sample():
    if request.method == 'GET':
        name = request.args.get('name')
        return 'This is '+name
    else:
        name = request.json.get('name')
        age = request.json.get('age')
        return "<h3 style = 'background-color:orange'>New Person added. Welcome {0}, You are {1} years old</h3>".format(name,age)

@app.route("/myself", methods = ["GET", "POST"])
def welcome():
    if request.method == "GET":
        return "greet"
    else:
        name = request.args.get('name')
        return render_template("data.html", name_data = )
if __name__ == '__main__':
    app.run(debug=True)
"""
#-----------------------------------------------------------------------------
"""
import requests

url = "http://127.0.0.1:5000/people"
data = requests.post(url, json={"name":"piyush", "age":19}).text
with open("text.html","w") as f:
    f.write(data)"""
#-----------------------------------------------------------------------------
"""
# Importing the required module for creating an web app
from flask import Flask


app = Flask(__name__)

@app.route("/hello")
def myname():
	return "Hello Piyush"

if __name__ == "__main__":
	app.run(debug=True)
"""
#-----------------------------------------------------------------------------
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/myprofile")
def profile():
	return render_template("profile.html")

if __name__ == "__main__":
	app.run(debug=True)
"""
#-----------------------------------------------------------------------------    
"""
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/posttesting", methods=["POST"])
def data():
	name = request.json.get('name')
	age = request.json.get('age')
	return f"Hello {name} your age is {age}"

if __name__ == "__main__":
	app.run(debug=True)
"""
#-----------------------------------------------------------------------------
"""
from flask import Flask, render_template, request
from newfile import mod_

app = Flask(__name__)

@app.route("/function")
def fun():
	response = mod_("piyush", 20)
	return response

if __name__ == "__main__":
	app.run(debug=True)
"""
#-----------------------------------------------------------------------------

from flask import Flask, render_template, request, url_for
from validator import name_validator
app = Flask(__name__)

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/validation", methods=["POST"])
def form_data():
	data = request.form
	name = data["name"]
	age = data["age"]
	response = name_validator(name,age)
	return render_template("response.html", response=response)

if __name__=="__main__":
    app.run(debug=True)