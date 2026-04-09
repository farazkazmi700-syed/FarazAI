from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # Python code to run
    result = 5 + 3
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)