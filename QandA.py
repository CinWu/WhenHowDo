from flask import Flask, render_template
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def home():
    
@app.route("/answer")
def answer():


if __name__ == "__main__":
    app.debug = True
    app.run()
