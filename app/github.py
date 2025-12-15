from app.bot import send_message

def handle_push_event(payload):
    repo = payload['repository']['full_name']
    pusher = payload['pusher']['name']
    commits = len(payload['commits'])

    msg = f"🚀 *New Push*\nRepo: {repo}\nBy: {pusher}\nCommits: {commits}"
    send_message(msg)
