from webbrowser import get
from flask import render_template, request, Blueprint
from flaskblog.models import Post
import time

from flask import Blueprint

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(
        Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template("home.html", posts=posts)


@main.route("/about")
def about():
    return render_template("about.html", title='About')

trending_posts = None

def get_trending_posts():
    posts = Post.query.all()
    posts = sorted(posts, key=lambda i: len(i.likes), reverse=True)
    trending_posts = {'posts': posts, 'date_created': time.time()}
    time.sleep(2)
    return trending_posts

@main.route("/trending")
def trending():
    global trending_posts
    if trending_posts is None:
        trending_posts = get_trending_posts()
        print("generating trending post first time")
    elif time.time() - trending_posts['date_created']  > 50:
        trending_posts = get_trending_posts()
        print("trending not None but expired")

    return render_template("trending.html", title='Trending', posts=trending_posts['posts'])