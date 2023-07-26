from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def roo():
    return render_template("ind.html")

@app.route("/home")
def home():
    return "hewss"


if __name__=="__main__":
    app.run(debug=True)
# if__name=="__main__":
#     app.run(debug=True)