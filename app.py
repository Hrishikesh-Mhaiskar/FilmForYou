from flask import Flask, flash, redirect, render_template, request
import requests
import html

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if (request.method == 'POST'):
        return render_template("layout.html")

    return render_template("index.html")


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    if(request.method == 'POST'):
        question1 = request.form.get('question1')
        question2 = request.form.get('question2')
        question3 = request.form.get('question3')
        question4 = request.form.get('question4')
        question5 = request.form.get('question5')
        question6 = request.form.get('question6')
        question7 = request.form.get('question7')
        question8 = request.form.get('question8')
        question9 = request.form.get('question9')
        question10 = request.form.get('question10')
        question11 = request.form.get('question11')
        question12 = request.form.get('question12')

        print(question1)
        print(question2)
        print(question3)
        print(question4)
        print(question5)
        print(question6)
        print(question7)
        print(question8)
        print(question9)
        print(question10)
        print(question11)
        print(question12)

    return render_template("quiz.html")


if __name__ == "__main__":
    app.run(debug=True)
