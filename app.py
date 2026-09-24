from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask Jenkins!"

if __name__ == "_main_":
    app.run()