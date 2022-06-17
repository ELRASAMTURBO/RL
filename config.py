## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQA2ESbOO6tvPuQBaePhnOcYUceBsg8t-ddb0m65MGGm02qKLf-2odvQBqJ-JC69hXmhu_3iwIGnyWDiVMBdyK4PSa2STqERTqKgak_26RsNT8FoLhS0OKQ9TBqeUAl_Nx2WJ_SEJUEdDvtl1HZZVZL9H2G80zJ_9FvFNL6Q3gwSF0ndjAr3127BS_kqclXykr7BiDRAfc9kutYsiFbjOLHLbFqwCRB2rUeYWzepZMsva7nbp8Vc8Ci39mQkmAQFe9DK1hOE4s4hdaZiyo2eXlGbisIIRyo8o8ODvLG4bGHQ5suZi7lwOoPAlwxF67oDH9td6M1k3J2lkLsWnbQaBi8HAAAAAUGzJkUA")
BOT_TOKEN = getenv("BOT_TOKEN", "5414854623:AAFur9r3eyxcgR8NX5Dc28yoLKDVY2N-MCg")
BOT_NAME = getenv("BOT_NAME", "song")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "muntazer")
OWNER_USERNAME = getenv("OWNER_USERNAME", "rr8r9")
ALIVE_NAME = getenv("ALIVE_NAME", "muntazer")
BOT_USERNAME = getenv("BOT_USERNAME", "TiGXbot")
OWNER_ID = getenv("OWNER_ID", "1854384004")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Paaane")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "G6_9R")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "G6_9R")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/286b2c436bcccd74b398c.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
