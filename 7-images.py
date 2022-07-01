from logging import root
import os
from flask import Flask, redirect, render_template, request, flash, url_for, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=5)
picture = os.path.join('static', 'img')
app.config['UPLOAD_FOLDER'] = picture

@app.route('/')
def index():
    images = os.path.join(app.config['UPLOAD_FOLDER'], 'img (1).jpg')
    return render_template("index.html", image=images)


@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["email"]
        session['user'] = user
        flash("Login Successful!")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash('Already logged in!')
            return redirect(url_for('user'))
        return render_template('login.html')


@app.route('/user')
def user():
    if "user" in session:
        user = session['user']
        return render_template('user.html', userEmail=user)
    else:
        flash('You are not logged in!')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    if "user" in session:
        user = session['user']
        flash(f'You are logged out, {user}!', 'info')
    session.pop('user', None)
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(debug=True)