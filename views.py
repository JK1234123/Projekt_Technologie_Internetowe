from flask import Blueprint, render_template, url_for, request, redirect
import requests
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, StringField
from wtforms.validators import DataRequired

dane = []
isDaneFiltered = False

views = Blueprint(__name__, "views")


class LimitForm(FlaskForm):
    limit = IntegerField("Ile postów wyświetlić?", validators=[DataRequired()])
    submit = SubmitField("Zatwierdź")


class FiltrForm(FlaskForm):
    minZnakow = IntegerField("Podaj minimalną ilość znaków:", validators=[DataRequired()])
    maxZnakow = IntegerField("Podaj maksymalną ilość znaków:", validators=[DataRequired()])
    submit = SubmitField("Zatwierdź")

class LoginForm(FlaskForm):
    login = StringField("Login:", validators=[DataRequired()])
    haslo = StringField("Hasło:", validators=[DataRequired()])
    submit = SubmitField("Zaloguj")

@views.route("/")
def home():
    return redirect("http://127.0.0.1:5000/login")


@views.route("/posty")
def posty():
    return render_template("index.html", data=dane, isDaneFiltered=isDaneFiltered)


@views.route("/albumy")
def albumy():
    data = get_albums()
    return render_template("albumy.html", data=data)


@views.route("/posty/<post_id>")
def post(post_id):
    data = get_post_by_id(post_id)
    comments = get_post_comments(post_id)
    return render_template('post.html', data=data, comments=comments)


@views.route("/albumy/<album_id>")
def photo(album_id):
    data = get_album_by_id(album_id)
    photos = get_photos(album_id)
    return render_template('album.html', data=data, photos=photos)


@views.route("/api", methods=["GET"])
def api():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    allPosts = response.json()
    limit = request.args.get('limit', default=10, type=int)
    limited_posts = allPosts[:limit]
    return limited_posts


@views.route("/limit", methods=["GET", "POST"])
def limiterForm():
    form = LimitForm()
    if form.validate_on_submit():
        limit = form.limit.data
        get_limited_posts(limit)
        return redirect("http://127.0.0.1:5000/posty")
    return render_template('limit.html', form=form)


@views.route("/filtr", methods=["GET", "POST"])
def filterForm():
    form = FiltrForm()
    if form.validate_on_submit():
        minZnakow = form.minZnakow.data
        maxZnakow = form.maxZnakow.data
        get_filtered_posts(minZnakow, maxZnakow)
        return redirect("http://127.0.0.1:5000/posty")
    return render_template('filtr.html', form=form)


@views.route("/login", methods=["GET", "POST"])
def loginForm():
    form = LoginForm()
    if form.validate_on_submit():
        login = form.login.data
        haslo = form.haslo.data
        isCorrect = check_login(login, haslo)
        if isCorrect == 1:
            get_posts()
            return redirect("http://127.0.0.1:5000/posty")
    return render_template('login.html', form=form)


@views.route("/clear")
def clear():
    get_posts()
    return redirect("http://127.0.0.1:5000/posty")


def get_album_by_id(album_id):
    allAlbums = get_albums()
    album_id = int(album_id)
    for x in allAlbums:
        if x["id"] == album_id:
            return x


def get_photos(album_id):
    album_id = int(album_id)
    url = "https://jsonplaceholder.typicode.com/albums/"+str(album_id)+"/photos"
    response = requests.get(url)
    json = response.json()
    return json


def get_post_by_id(post_id):
    post_id = int(post_id)
    for x in dane:
        if x["id"] == post_id:
            return x


def get_post_comments(post_id):
    post_id = int(post_id)
    url = "https://jsonplaceholder.typicode.com/posts/"+str(post_id)+"/comments"
    response = requests.get(url)
    json = response.json()
    return json


def get_posts():
    global dane
    global isDaneFiltered
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    dane = response.json()
    isDaneFiltered = False
    return dane


def get_albums():
    url = "https://jsonplaceholder.typicode.com/albums"
    response = requests.get(url)
    allAlbums = response.json()
    return allAlbums


def get_limited_posts(limit):
    global dane
    global isDaneFiltered
    url = "http://127.0.0.1:5000/api"
    params = {"limit": int(limit)}
    response = requests.get(url, params)
    dane = response.json()
    isDaneFiltered = True
    return dane


def get_filtered_posts(minimum, maximum):
    global dane
    global isDaneFiltered
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    allPosts = response.json()
    filteredposts = []
    for x in allPosts:
        if int(minimum) <= len(x["body"]) <= int(maximum):
            filteredposts.append(x)
    dane = filteredposts
    isDaneFiltered = True
    return dane


def check_login(login, haslo):
    if login == "Jan" and "Tester":
        return 1
    else:
        return 0
