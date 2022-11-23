import mysql.connector
from flask import Flask, render_template , request ,redirect , url_for

from attendance import main1

print("Content-Type: text/html\n")
conn = mysql.connector.connect(host="localhost", database="sms", user="root")

cursor = conn.cursor()

app = Flask(__name__)



@app.route("/")
def index():
    return render_template("home.html")

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/try")
def try1():
    main1()


@app.route("/students")
def students():
    cursor.execute ("select * from students")
    value = cursor.fetchall()
    return render_template("index.html",data=value)


if __name__ == "__main__":
    app.run(debug=True)