## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgDC-ACb5kb_ZKgFPP75qw_mz7ePWruLcgldZQZEVcPvuKLHW4UxOS8g1jEHmba6toQiwOONlBLqydGaB5P0ZGkSn7Odwa0gENqf_uS7pntcxIBlyhf0QPv7REG2Gg_aBsYsSrS7CGN_46R0ZOk6QMlip7ytQ9vpKwetul_LPz2BKAY6ewp8qlWFh4T7BVGcDU_iBH2uRObNW0N-o1WZq3itxya6oLjIs6z_hR8nBrBzlDtZ4Fsx9EOrZR3YQ1DTnXgdCHP3qBuSeTmyNHWQftwYuXwQf5ZjX1Lsxvk56xT4iQEjfxbqjXb1l0pOsmiwQ_M9d_dq0n4THVmCmKFwNV94eocn9AA")
BOT_TOKEN = getenv("BOT_TOKEN", "5404573328:AAEWDehRkEhql6xc3S3oCdhPkqT8dzjZkOY")
BOT_NAME = getenv("BOT_NAME", "song")
API_ID = int(getenv("API_ID", "14940919"))
API_HASH = getenv("API_HASH", "a66bbdd32ce6fee0b3004a83a6f6e47b")
OWNER_NAME = getenv("OWNER_NAME", "Elrasam7")
OWNER_USERNAME = getenv("OWNER_USERNAME", "E_R_S_A_M1")
ALIVE_NAME = getenv("ALIVE_NAME", "Elrasam7")
BOT_USERNAME = getenv("BOT_USERNAME", "Elrasam11111bot")
OWNER_ID = getenv("OWNER_ID", "2125600195")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Paaane")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "EL_RASA")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "EL_RASA")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2125600195").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/2fbfedf9ae631c9c591ae.jpg")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/6e1cb97beb53c9c51c2d5.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
