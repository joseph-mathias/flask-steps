from flask import Flask, render_template

# Template Rendering 
app = Flask(__name__)

@app.route("/<name>/")
def index(name):
    return render_template("index.html", content=name, description="This Page Man!")

@app.route('/list')
def list():
    return render_template('list.html', context=["Moses", "Royd", "Mulonda", "Sharon"])

if __name__ == "__main__":
    app.run()