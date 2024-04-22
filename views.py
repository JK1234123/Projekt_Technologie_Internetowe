from flask import Blueprint, render_template, url_for, request
import requests
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired

posty = []

views = Blueprint(__name__,"views")


@views.route("/")
def home():
    get_posts()
    return render_template("home.html")

@views.route("/posty")
def posty():
    return render_template("index.html", data=posty)

@views.route("/albumy")
def albumy():
    data = get_albums()
    return render_template("albumy.html", data=data)


@views.route("/<post_id>")
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

#"POST"
@views.route("/limit" , methods=["POST", "GET"])
def limiterForm():
    if request.method == "POST":
        default = 0
        PostNumber = request.form.get('PostNumber', default)
        return str(PostNumber)
    return render_template('apiPopUp.html')

def get_album_by_id(album_id):
    allAlbums = get_posts()
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
    allPosts = get_posts()
    post_id = int(post_id)
    for x in allPosts:
        if x["id"] == post_id:
            return x


def get_post_comments(post_id):
    post_id = int(post_id)
    url = "https://jsonplaceholder.typicode.com/posts/"+str(post_id)+"/comments"
    response = requests.get(url)
    json = response.json()
    return json


def get_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    allPosts = response.json()
    return allPosts

def get_albums():
    url = "https://jsonplaceholder.typicode.com/albums"
    response = requests.get(url)
    allAlbums = response.json()
    return allAlbums


def get_limited_posts(limit):
    url = "http://127.0.0.1:5000/api"
    params = {"limit": int(limit)}
    response = requests.get(url, params)
    limited_posts = response.json()
    return limited_posts

def get_filtered_posts(min, max):
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    allPosts = response.json()
    filteredposts = []
    for x in allPosts:
        if int(min) <= len(x["body"]) <= int(max):
            filteredposts.append(x)
    return filteredposts

