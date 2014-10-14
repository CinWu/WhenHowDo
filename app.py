from flask import Flask, render_template, request
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("input.html")

@app.route("/answer")
def answer():
   question= request.args.get("question_input")
   print question
   #need to figure out which file to send it to
   answer= search.find(question)
   return render_template("output.html", question = question, answer= answer) 



if __name__ == "__main__":
    app.debug = True
    app.run()
