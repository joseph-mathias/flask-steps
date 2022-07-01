from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        user = request.form["email"]
        return redirect(url_for("user", userPage=user))
    else:
        return render_template('login.html')


@app.route('/<userPage>')
def user(userPage):
    return render_template('user.html', userEmail=userPage)


if __name__ == "__main__":
    app.run(debug=True)