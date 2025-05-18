import json
import os
from datetime import datetime



POSTS_FILE = 'posts.json'
def load_posts():
    if not os.path.exists(POSTS_FILE):
        with open (POSTS_FILE, 'w') as f:
            json.dump([], f)
        
    try:
        with open(POSTS_FILE, 'r') as f:
            posts = json.load(f)
            for post in posts:
                post['timestamp'] = datetime.fromisoformat(post['timestamp'])
            return posts
    except (json.JSONDecodeError, ValueError):
        return []

def save_posts(posts):
    with open (POSTS_FILE, 'w') as f:
        json.dump([
            {**post, 'timestamp': post['timestamp'].isoformat()}
            for post in posts
        ], f, indent=2)

POSTS = load_posts()

def get_all_posts():
    return POSTS

def get_post_by_id(post_id):
    return next((post for post in POSTS if post['id'] == post_id), None)

def create_post(title, content, author):
    print(title)
    new_id = POSTS[-1]['id'] + 1 if POSTS else 1
    timestamp = datetime.now()
    post = {'id':new_id, 'title':title, 'content':content, 'author':author, 'timestamp':timestamp}
    POSTS.append(post)
    save_posts(POSTS)
    print(POSTS)
    
    return post

def delete_post(post_id):
    Post=[]
    POSTS = [ post for post in POSTS if post['id']!=post_id ]
    save_posts(POSTS)
    print (Post)
    return


