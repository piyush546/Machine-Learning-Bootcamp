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

"""@app.route("/myself", methods = ["GET", "POST"])
def welcome():
    if request.method == "GET":
        return "greet"
    else:
        name = request.args.get('name')
        return render_template("data.html", name_data = )"""
if __name__ == '__main__':
    app.run(debug=True)



import requests

url = "http://127.0.0.1:5000/people"
data = requests.post(url, json={"name":"piyush", "age":19}).text
with open("text.html","w") as f:
    f.write(data)