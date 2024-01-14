from flask import Flask, render_template, request
import pymysql
import random

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'test228'

connection = pymysql.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    db=app.config['MYSQL_DB']
)

cursor = connection.cursor()

@app.route('/', methods=['GET', 'POST'])
def index():
    text = random.randint(1, 100)

    return render_template("index.html", text=text)  # передайте text в шаблон

if __name__ == "__main__":
    app.run(debug=True)
