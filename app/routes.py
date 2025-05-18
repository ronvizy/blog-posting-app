from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models import Comment, Post
from app import db

main = Blueprint('main', __name__)
@main.route('/')
def feed():
    print("hello this is feed page")
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    print(posts)
    return render_template('feed.html', posts=posts)

@main.route('/post/<int:post_id>')
def view_post(post_id):
    post = Post.query.get_or_404(post_id)
    comments = Comment.query.filter_by(post_id= post_id).all()
    return render_template('post.html', post=post, comments=comments)

@main.route('/create', methods=['GET'])
def show_create_post_form():
    return render_template('create_post.html')

@main.route('/api/create', methods=['POST'])
def create_post():
    print("Hello")
    if request.is_json:
        data = request.get_json()
        title = data.get('title')
        content = data.get('content')
        author = data.get('author')
    else:
        title = request.form.get('title')
        content = request.form.get('content')
        author = request.form.get('author')

    if not title or not content or not author:
        return jsonify({'error': 'Missing title, content or author'}), 400

    post = Post(title=title, content=content, author=author)
    db.session.add(post)
    db.session.commit()
    return redirect(url_for('view_post', post_id=post_id))

@main.route('/reply/<int:post_id>', methods=["POST"])
def create_reply(post_id):
    print(post_id)
    content = request.form.get('content')
    author = request.form.get('author')
    parent_id = request.form.get('parent_id')
    if len(parent_id) < 1:
        parent_id=None
    if not content or not author:
        return "Missing content or author", 400

    reply = Comment(content=content, author=author, post_id=post_id, parent_id=parent_id)
    db.session.add(reply)
    db.session.commit()
    #return render_template('post.html', post_id=post_id)
    return view_post(post_id)