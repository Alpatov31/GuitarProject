from flask import render_template, flash, redirect, url_for, request
from app import app, db
from datetime import datetime


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/chords')
def chords():
    return render_template("chords.html")

@app.route('/songs')
def songs():
    return render_template("songs.html")

@app.route('/articles')
def articles():
    return render_template("articles.html")

@app.route('/account')
def account():
    return render_template("account.html")


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



