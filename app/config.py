import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# =========================
# Telegram Configuration
# =========================
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# =========================
# GitHub Configuration
# =========================
GITHUB_SECRET = os.getenv("GITHUB_SECRET")

# =========================
# Validation (Fail Fast)
# =========================
missing_vars = []

if not BOT_TOKEN:
    missing_vars.append("BOT_TOKEN")
if not CHAT_ID:
    missing_vars.append("CHAT_ID")
if not GITHUB_SECRET:
    missing_vars.append("GITHUB_SECRET")

if missing_vars:
    raise EnvironmentError(
        f"Missing required environment variables: {', '.join(missing_vars)}"
    )
