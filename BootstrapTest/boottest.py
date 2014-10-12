from flask import Flask, render_template

from flask_bootstrap import Bootstrap

def create_app(configfile=None):
    app = Flask(__name__)
    Bootstrap(app)

    @app.route('/')
    def index():
        return render_template("boots.html")
    return app

if __name__ == "__main__":
    create_app().run(debug = True)
