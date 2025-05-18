import json 
import os
from datetime import datetime

REPLIES_FILE = "replies.json"

def load_replies():
    if not os.path.exists(REPLIES_FILE):
        with open(REPLIES_FILE, 'w') as f: #opening replies file as 'f'  in write mode
            json.dump([], f)   #dumping a list in replies.json file
    
    try:
        with open(REPLIES_FILE, 'r') as f: #opening replies file as 'f' in read mode
            replies = json.load(f) #loading the relies file into python list from json format

            for reply in replies:#traversing each reply
                reply['timestamp'] = datetime.fromisoformat(reply['timestamp']) #converting each iso format timestamp string to datetime object
            return replies
    except(json.JSONDecodeError, ValueError):
        #if file is curropt or empty, return empty list
        return []
        
def save_replies(replies):
    with open(REPLIES_FILE, 'w') as f:
        json.dump([ #dumping the replies into REPLIES_JSON whole converting the timestamp into iso string
            {**reply, 'timestamp':reply['timestamp'].isoformat()}
            for reply in replies
        ], f, indent=2)
    
REPLIES = load_replies()
def get_replies_for_post(post_id):
    replies = load_replies()
    return [reply for reply in replies if reply['post_id'] == post_id]

def add_reply(post_id, content, author, parent_id=None):
    REPLIES = load_replies()
    new_id = REPLIES[-1]["id"] + 1 if REPLIES else 1
    timestamp = datetime.now()
    
    reply = {
        'id':new_id,
        "post_id":post_id,
        "content":content,
        "author":author,
        "timestamp":timestamp,
        "parent_id": int(parent_id) if parent_id and parent_id.isdigit() else None
    }
    REPLIES.append(reply)
    save_replies(REPLIES)
    return reply