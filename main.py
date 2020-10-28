from flask import Flask, send_from_directory, render_template

app = Flask(__name__)

@app.route("https://ozgurblog.herokuapp.com/")
@app.route("https://ozgurblog.herokuapp.com/home")
def home():
    return render_template("index.html")
@app.route("https://ozgurblog.herokuapp.com/hakkimizda")
def hakkimizda():
    return render_template("error.html")
@app.route("https://ozgurblog.herokuapp.com/yardim")
def yardim():
    return render_template("error.html")
@app.route("https://ozgurblog.herokuapp.com/yazi_yayinlama")
def yazi_yayinlama():
    return render_template("error.html")
if __name__ == "__main__":
    app.run(debug=True)
