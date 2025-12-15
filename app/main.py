from fastapi import FastAPI, Request
from app.github import handle_push_event

app = FastAPI()

@app.post("/webhook")
async def github_webhook(request: Request):
    payload = await request.json()
    event = request.headers.get("X-GitHub-Event")

    if event == "push":
        handle_push_event(payload)

    return {"status": "ok"}
