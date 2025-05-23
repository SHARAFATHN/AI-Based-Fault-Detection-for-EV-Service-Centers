from flask import Flask, render_template
from scripts.predict_fault import predict_fault
import json

app = Flask(__name__)

@app.route("/")
def index():
    pred, data = predict_fault()
    return render_template("dashboard.html", data=data, fault=pred)

if __name__ == "__main__":
    app.run(debug=True)
