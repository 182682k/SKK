from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("homepage.html")

@app.route('/profile')
def profile():
    return render_template("profile.html")

@app.route('/erpandpetrol')
def erpandpetrol():
    return render_template("erpandpetrol.html")

@app.route('/routeplanner')
def routeplanner():
    return render_template("routeplanner.html")

@app.route('/parkinglots')
def parkinglots():
    return render_template("parkinglots.html")

@app.route('/calendar')
def calendar():
    return render_template("calendar.html")

@app.route('/forum')
def forum():
    return render_template("forum.html")

@app.route('/signin')
def signin():
    return render_template("singin.html")



if __name__ == '__main__':
    app.run(debug=True)
