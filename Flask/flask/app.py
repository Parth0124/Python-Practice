from flask import Flask

app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to the Flask App."

@app.route("/index")
def index():
    return "Welcome to the index page."


if __name__=="__main__":
    app.run(port=4000, debug=True)