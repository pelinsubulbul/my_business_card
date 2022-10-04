from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == '__main__':
    # use debug mode so you  dont open close server constantly
    app.run(debug=True)

    # Just another fine responsive site template designed by <a href="http://html5up.net">HTML5 UP</a><br />
    # 							and released for free under the <a href="http://html5up.net/license">Creative Commons</a>.