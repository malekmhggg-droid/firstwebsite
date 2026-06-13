from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/lessons")
def lessons():
    return "<h1>Lessons Page</h1>"

@app.route("/practice")
def practice():
    return "<h1>Practice Page</h1>"

@app.route("/categories")
def categories():
    return "<h1>Categories Page</h1>"


if __name__ == "__main__":
    app.run()
