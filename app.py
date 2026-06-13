from flask import Flask, render_template

app = Flask(__name__)

# -------------------------
# HOME PAGE
# -------------------------
@app.route("/")
def home():
    return render_template("index.html")


# -------------------------
# MAIN LESSONS PAGE
# -------------------------
@app.route("/lessons")
def lessons():
    return render_template("lessons.html")


# -------------------------
# PRACTICE + CATEGORIES
# -------------------------
@app.route("/practice")
def practice():
    return "<h1>Practice Page</h1>"

@app.route("/categories")
def categories():
    return "<h1>Categories Page</h1>"


# -------------------------
# LESSONS SUBPAGES (Algebra, Fractions, etc.)
# -------------------------
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


# -------------------------
# GRADE 1 MAIN PAGE
# -------------------------
@app.route("/grade1")
def grade1():
    return render_template("grade1.html")


# -------------------------
# GRADE 1 LESSON PAGES
# -------------------------
@app.route("/grade1/addition")
def grade1_addition():
    return render_template("grade1_addition.html")

@app.route("/grade1/subtraction")
def grade1_subtraction():
    return render_template("grade1_subtraction.html")

@app.route("/grade1/counting")
def grade1_counting():
    return "<h1>Grade 1 Counting Lesson Coming Soon</h1>"

@app.route("/grade1/shapes")
def grade1_shapes():
    return "<h1>Grade 1 Shapes Lesson Coming Soon</h1>"

@app.route("/grade1/placevalue")
def grade1_placevalue():
    return "<h1>Grade 1 Place Value Lesson Coming Soon</h1>"


# -------------------------
# RUN APP
# -------------------------
if __name__ == "__main__":
    app.run()
