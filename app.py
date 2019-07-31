from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
	list1 =["pasta", "sushi", "fish"]
    return render_template("index.html", food=list1)

if __name__ == '__main__':
   app.run(debug = True)