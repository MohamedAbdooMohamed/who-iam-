from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def pepsi():
    return render_template('home.html')

@app.route("/socialmedia")
def about():
    return render_template("socialmedias.html")

@app.route("/skills")
def skills():
    return render_template("skills.html")


if __name__=="__main__":
    app.run(debug=True,port=2000)
