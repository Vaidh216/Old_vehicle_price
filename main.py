from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/contact")
def contact():
    return "Contact page"

if __name__ == '__main__':  
   app.run(debug=True)