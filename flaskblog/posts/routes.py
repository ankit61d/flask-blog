from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Like, Post
from flaskblog.posts.forms import PostForm


from flask import Blueprint

posts = Blueprint('posts', __name__)

# dummy comments data

comments = [
    {
        'author': 'Ankit',
        'content': 'First comment',
        'date_commented': '07-05-2022'
    },
    {
        'author': 'Aish',
        'content': 'Second comment',
        'date_commented': '09-05-2022'
    }
]


@posts.route("/post/new", methods=['GET', 'POST'])
@login_required  # creating a post requires login
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data,
                    content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post created', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title="Post new stuff", form=form, legend='New Post')


@posts.route("/post/<int:post_id>")
def post(post_id):
    # print(type(post_id))
    post = Post.query.get_or_404(post_id)
    like_state = None
    #print(f"{Like.query.filter_by(post_id=post_id, author=current_user.id)}")
    if not current_user.is_authenticated:
        like_state = 1
    elif Like.query.filter_by(post_id=post_id, author=current_user.id).count():
        like_state = 2
    else:
        like_state = 3
    return render_template('post.html', title=post.title, post=post, like_state=like_state, comments=comments)


@posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        # db.session.add(post).
        db.session.commit()
        flash('Your Post has been updated', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post', form=form, legend='Update Post')


@posts.route("/post/<int:post_id>/delete", methods=['POST'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted', 'success')
    return redirect(url_for('main.home'))


@posts.route("/post/<int:post_id>/like", methods=['POST'])
@login_required
def like(post_id):
    like = Like.query.filter_by(
        post_id=post_id, author=current_user.id).first()
    print(f"{like}")
    if like:
        db.session.delete(like)
        db.session.commit()
    else:
        like = Like(author=current_user.id, post_id=post_id, like=True)
        db.session.add(like)
        db.session.commit()
    
    return redirect(url_for('posts.post', post_id=post_id))
