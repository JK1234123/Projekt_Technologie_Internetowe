from flask import Blueprint, render_template, url_for
import requests
import json

views = Blueprint(__name__,"views")


@views.route("/")
def home():
    data = get_posts()
    return render_template("index.html", data=data)


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


def gohome():
    home()
