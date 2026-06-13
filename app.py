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
@app.route("/lessons")
def lessons():
    return render_template("lessons.html")
@app.route("/lessons/algebra")
def algebra():
    return "<h1>Algebra Lesson Coming Soon</h1>"

@app.route("/lessons/fractions")
def fractions():
    return "<h1>Fractions Lesson Coming Soon</h1>"

@app.route("/lessons/geometry")
def geometry():
    return "<h1>Geometry Lesson Coming Soon</h1>"

@app.route("/lessons/integers")
def integers():
    return "<h1>Integers Lesson Coming Soon</h1>"

@app.route("/lessons/decimals")
def decimals():
    return "<h1>Decimals Lesson Coming Soon</h1>"
@app.route("/grade1")
def grade1():
    return render_template("grade1.html")
@app.route("/grade1/addition")
def grade1_addition():
    return "<h1>Grade 1 Addition Lesson Coming Soon</h1>"

@app.route("/grade1/subtraction")
def grade1_subtraction():
    return "<h1>Grade 1 Subtraction Lesson Coming Soon</h1>"

@app.route("/grade1/counting")
def grade1_counting():
    return "<h1>Grade 1 Counting Lesson Coming Soon</h1>"

@app.route("/grade1/shapes")
def grade1_shapes():
    return "<h1>Grade 1 Shapes Lesson Coming Soon</h1>"

@app.route("/grade1/placevalue")
def grade1_placevalue():
    return "<h1>Grade 1 Place Value Lesson Coming Soon</h1>"

@app.route("/grade1/addition")
def grade1_addition():
    return render_template("grade1_addition.html")

@app.route("/grade1/subtraction")
def grade1_subtraction():
    return render_template("grade1_subtraction.html")

if __name__ == "__main__":
    app.run()
