from flask import Flask, render_template, abort, request, jsonify, redirect, url_for
from post import get_all_posts, get_post_by_id, create_post, load_posts
from comments import get_replies_for_post, add_reply

app = Flask(__name__)

#get feed
@app.route('/')
def feed():
    posts = get_all_posts()
    return render_template('feed.html', posts=posts)

#get post
@app.route('/post/<int:post_id>')
def view_post(post_id):
    post = get_post_by_id(post_id)
    if not post:
        return "post does not exist. 404 not found"
    comments = get_replies_for_post(post_id)
    print(comments);
    return render_template('post.html', post=post, comments=comments)

# #create post
# @app.route('/api/create', methods=['POST'])
# def api_create_post():
#     data = request.get_json()
#     title = data.get('title')
#     content = data.get('content')
#     author = data.get('author')
#     if( not title or not content or not author):
#         return jsonify({'error': 'Missing title, content or author'}), 400

#     post=create_post(title, content, author)
#     # comments = get_replies_for_post(post.id)
#     return jsonify(post), 201
#     # return render_template('post.html', post=post, comments=comments)

@app.route('/api/create', methods=['POST'])
def api_create_post():
    if request.is_json:
        # JSON body (API request)
        data = request.get_json()
        title = data.get('title')
        content = data.get('content')
        author = data.get('author')
    else:
        # Form data (HTML form)
        title = request.form.get('title')
        content = request.form.get('content')
        author = request.form.get('author')

    if not title or not content or not author:
        return jsonify({'error': 'Missing title, content or author'}), 400

    post = create_post(title, content, author)

    if request.is_json:
        return jsonify(post), 201
    else:
        # Redirect to the post page if submitted via form
        return redirect(url_for('view_post', post_id=post['id']))
#show post form
@app.route('/create', methods=['GET'])
def show_create_post_form():
    return render_template('create_post.html')

#delete post
@app.route('/api/post/delete/<int:post_id>', methods=['DELETE'])
def api_delete(post_id):
    print("helow")
    post = get_post_by_id(post_id)
    if not post:
        return "post does not exist. 404 not found"
    return post

#add reply
@app.route('/reply/<int:post_id>', methods=["POST"])
def create_reply(post_id):
    # data= request.get_json()
    # content = data.get('content')
    # author = data.get('author')
    # parent_id = data.get('parent_id')

    content = request.form.get('content')
    author = request.form.get('author')
    parent_id = request.form.get('parent_id')
    
    if( not content or not author):
        return jsonify({'error': 'Missing title, content or author'}), 400
    
    reply = add_reply(post_id, content, author, parent_id )
    return redirect(url_for('view_post', post_id=post_id))
    # return jsonify(reply), 201

if __name__ == '__main__':
    app.run(debug=True)
