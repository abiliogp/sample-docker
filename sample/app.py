import os
from flask import Flask

print("Oi Docker!!!")

app = Flask(__name__)

@app.route("/")
def hello():
    return "Oi docker!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5005')
