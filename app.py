from flask import Flask, render_template, url_for

app = Flask(__name__) # Refers to this current file 

# Home Page
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add")
def add():
    return render_template("add.html")
    
if __name__ == "__app__":
    app.run(debug=True)