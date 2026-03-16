from flask import Flask, request, render_template
import subprocess

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/ping", methods=["POST"])
def ping():
    target = request.form.get("target")

    # Windows compatible vulnerable command
    command = "ping -n 2 " + target

    try:
        output = subprocess.getoutput(command)
    except Exception as e:
        output = str(e)

    return render_template("index.html", result=output)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)