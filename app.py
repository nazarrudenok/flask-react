from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    text = random.randint(1, 100)

    return render_template("index.html", text=text)  # передайте text в шаблон

if __name__ == "__main__":
    app.run(debug=True)
