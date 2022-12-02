import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}

SESSION_NAME = getenv("SESSION_NAME")

if str(getenv("STRING_SESSION2")).strip() == "":
    SESSION2 = str(None)
else:
    SESSION2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    SESSION3 = str(None)
else:
    SESSION3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    SESSION4 = str(None)
else:
    SESSION4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    SESSION5 = str(None)
else:
    SESSION5 = str(getenv("STRING_SESSION5"))

BOT_TOKEN = getenv("BOT_TOKEN", "")
BOT_NAME = getenv("BOT_NAME", "Umk")

API_ID = int(getenv("API_ID", "10386742"))
API_HASH = getenv("API_HASH", "f16d95af09c7fb1f2516a77f40147d0d")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://Cloner:Cloner@cluster0.cgc6t.mongodb.net/?retryWrites=true&w=majority")
OWNER_NAME = getenv("OWNER_NAME", "Floch")
OWNER_USERNAME = getenv("OWNER_USERNAME", "ddk_sempai40")
ALIVE_NAME = getenv("ALIVE_NAME", "Tjk")
BOT_USERNAME = getenv("BOT_USERNAME", "@mongo_db_url_bot")
OWNER_ID = getenv("OWNER_ID", "5051948773")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "TheTjkChat")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "tjk_legendbots")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1669178360").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/9d6f09ba6c4a194e137e6.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/9d6f09ba6c4a194e137e6.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/itz-pro-ddk/Mongodb-bot")
