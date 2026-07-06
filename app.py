from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    if request.method == "POST":
        password = request.form.get("password")
        login = request.form.get("login")

        if login == password:
            message = "Details confirmed. Logged inside account."
        else:
            message = "Incorrect password"

    return render_template("index.html", message=message)

app.run(debug=True)
