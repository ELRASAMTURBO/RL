## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgBU6fwb4vjF42Xaqair0WhFNb-e5ynnTOm136BWiFyrypkCYP4SBX-n_d6ev-PbYeEBFgTe28B64v__Cuka9tnIVy1eNX8849cHR4sdFOBdo3ozDVswoIgdMv7fEZd58bRM2BlAeIrUJM0Ft9oDa7zi5HYlKy9ZPFcdSy6I5wmR1J4cai5xx3qYAwImC61Vx0LTRr_Es1Kn7g3b5P9YEe8oDO07pSkDE5BXZlhiioQUMZr6EcNqDSq18S9Jris8b0dqobQ7UHkFIzcH4xxjfrDOYbTWhUB370iV3jwFZmjvt4UnXxYHY95Y0AdiMZw1EMBR8uY6OhzO_9MDlWuYI26Oeocn9AA")
BOT_TOKEN = getenv("BOT_TOKEN", "5532726746:AAHkgu3HbQQju_J5b0C_JlS0m2wRjnnrXds")
BOT_NAME = getenv("BOT_NAME", "song")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "muntazer")
OWNER_USERNAME = getenv("OWNER_USERNAME", "rr8r9")
ALIVE_NAME = getenv("ALIVE_NAME", "muntazer")
BOT_USERNAME = getenv("BOT_USERNAME", "TiGemusicbot")
OWNER_ID = getenv("OWNER_ID", "5284259786")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Paaane")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "ZZ9Z5")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "ZZ9Z5")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5284259786").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/286b2c436bcccd74b398c.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
