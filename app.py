from flask import Flask, render_template, request
from bs4 import BeautifulSoup

import search

app = Flask(__name__)

@app.route("/", methods = ["GET","POST"])
@app.route("/error", methods = ["GET","POST"])
def home(error = None):
    if (request.method == "POST"):
        return redirect(url_for('answer'))
    return render_template("input.html")
        
@app.route("/answer", methods = ["GET","POST"])
def answer(question = None, answer = None, error = None):
    question = request.form["question_input"]
    if ("who" not in question.lower() and "when" not in question.lower()):
        return render_template("input.html", error = "Error: Invalid question. Must contain who or when.")
    s = search.find(question)
    answer = s
    return render_template("output.html", question=question, answer=answer)


if __name__ == "__main__":
    app.debug = True
    app.run()
