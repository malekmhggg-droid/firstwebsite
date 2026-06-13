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
def grade1_countin():
    return "<h1>Grade 1 Counting Lesson Coming Soon</h1>"

@app.route("/grade1/shapes")
def grade1_shapes():
    return "<h1>Grade 1 Shapes Lesson Coming Soon</h1>"

@app.route("/grade1/placevalue")
def grade1_placevalue():
    return "<h1>Grade 1 Place Value Lesson Coming Soon</h1>"

@app.route("/elementary")
def elementary():
    return render_template("elementary.html")

@app.route("/middle")
def middle():
    return render_template("middle.html")

@app.route("/high")
def high():
    return render_template("high.html")

@app.route("/grade2")
def grade2():
    return "<h1>Grade 2 Coming Soon</h1>"

@app.route("/grade3")
def grade3():
    return "<h1>Grade 3 Coming Soon</h1>"

@app.route("/grade4")
def grade4():
    return "<h1>Grade 4 Coming Soon</h1>"

@app.route("/grade5")
def grade5():
    return "<h1>Grade 5 Coming Soon</h1>"

@app.route("/grade6")
def grade6():
    return "<h1>Grade 6 Coming Soon</h1>"

@app.route("/grade1/counting")
def grade1_counting():
    return render_template("grade1_counting.html")

@app.route("/grade1/shapes")
def grade1_shapes():
    return render_template("grade1_shapes.html")

@app.route("/grade1/placevalue")
def grade1_placevalue():
    return render_template("grade1_placevalue.html")

from flask import Flask, render_template, request
import random

app = Flask(__name__)

# -------------------------
# GRADE 1 QUIZ QUESTIONS
# -------------------------
grade1_questions = [
    {"question": "What is 1 + 1?", "options": ["1", "2", "3"], "answer": "2"},
    {"question": "What is 5 - 2?", "options": ["2", "3", "4"], "answer": "3"},
    {"question": "Count: What comes after 7?", "options": ["6", "8", "9"], "answer": "8"},
    {"question": "Which shape has 3 sides?", "options": ["Circle", "Triangle", "Square"], "answer": "Triangle"},
    {"question": "In 12, what is the tens digit?", "options": ["1", "2", "0"], "answer": "1"},
    {"question": "What is 3 + 2?", "options": ["4", "5", "6"], "answer": "5"},
    {"question": "What is 9 - 1?", "options": ["7", "8", "9"], "answer": "8"},
    {"question": "Count: What number comes before 10?", "options": ["8", "9", "11"], "answer": "9"},
    {"question": "Which shape is round?", "options": ["Square", "Circle", "Triangle"], "answer": "Circle"},
    {"question": "In 35, what is the ones digit?", "options": ["3", "5", "0"], "answer": "5"}
]

# -------------------------
# QUIZ PAGE
# -------------------------
@app.route("/grade1/quiz")
def grade1_quiz():
    questions = random.sample(grade1_questions, 10)
    return render_template("grade1_quiz.html", questions=questions)

# -------------------------
# QUIZ SUBMISSION
# -------------------------
@app.route("/grade1/quiz/submit", methods=["POST"])
def grade1_quiz_submit():
    score = 0

    for i, q in enumerate(grade1_questions[:10], start=1):
        user_answer = request.form.get(f"q{i}")
        if user_answer == q["answer"]:
            score += 1

    # Grade calculation
    if score == 10:
        grade = "A+"
    elif score >= 8:
        grade = "A"
    elif score >= 6:
        grade = "B"
    elif score >= 4:
        grade = "C"
    else:
        grade = "F"

    passed = score >= 6

    return render_template("grade1_quiz_results.html", score=score, grade=grade, passed=passed)

# -------------------------
# RUN APP
# -------------------------
if __name__ == "__main__":
    app.run()
