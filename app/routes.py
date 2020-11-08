from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.models import Chord, User, Song, Article
from datetime import datetime
from flask_login import current_user, login_user, login_required, logout_user


@app.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect('/index')
    if request.method == "POST":
        errors = []
        email = request.form["login"]
        password = request.form["password"]
        user = User.query.filter_by(email=email).first()
        if user is None or user.check_password(password) == False:
            errors.append("Неверно введены данные пользователя")
            return render_template("login.html", errors=errors)
        login_user(user)
        return redirect("/")
    else:
        return render_template("login.html")


@app.route('/registration', methods=["GET", "POST"])
def registration():
    if current_user.is_authenticated:
        return redirect('/index')
    if request.method == "POST":
        errors = []
        username = request.form["username"]
        email = request.form["login"]
        if User.query.filter_by(username=username).first():
            errors.append("Имя пользователя уже занято")
        if User.query.filter_by(email=email).first():
            errors.append("Почта уже занята")
        password = request.form["password"]
        password2 = request.form["password2"]
        if password != password2:
            print("Пароли не совпадают")
            errors.append("Пароли не совпадают")
        if errors:
            return render_template("registration.html", errors=errors)
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return redirect("/login")
    else:
        return render_template("registration.html")


@app.route('/logout')
def logout():
    logout_user()
    return redirect("/login")


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/chords')
def chords():
    chrds = Chord.query.all()
    return render_template("chords.html", chrds=chrds)


@app.route('/songs')
def songs():
    songs = Song.query.all()
    return render_template("songs.html", songs=songs)


@app.route('/articles')
def articles():
    return render_template("articles.html")


@app.route('/account')
@login_required
def account():
    return render_template("account.html", user=current_user)

# @app.route('/add_snkrs', methods=["GET", "POST"])
# def add_snkrs():
#     if request.method == "POST":
#         brand = request.form["brand"]
#         model = request.form["model"]
#         year = request.form["year"]
#         s = Sneakers(brand=brand, model=model, release_year=year)
#         print(s)
#         db.session.add(s)
#         db.session.commit()
#         return redirect("/all_snkrs")
#     else:
#         return render_template("add_snkrs.html")
#
#
# @app.route('/all_snkrs', methods=["GET"])
# def all_snkrs():
#     year_start = request.args.get("year_start") or 1950
#     year_finish = request.args.get("year_finish") or 2020
#     print(year_start, year_finish)
#     s = Sneakers.query.filter(Sneakers.release_year >= year_start, Sneakers.release_year <= year_finish)
#     print(s)
#     return render_template("all_snkrs.html", s=s)
