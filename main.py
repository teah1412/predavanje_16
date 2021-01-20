from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about-me")
def index():
    return render_template("about-me.html")


if __name__ == "__main__":
    app.run()