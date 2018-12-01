import random

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/omikuji")
def fortune():
    idx = random.choice(["凶", "大吉", "吉"])
    return render_template("omikuji.html", idx=idx)


if __name__ == "__main__":
    app.run(debug=True)
