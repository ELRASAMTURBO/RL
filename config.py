## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgDC-ACb5kb_ZKgFPP75qw_mz7ePWruLcgldZQZEVcPvuKLHW4UxOS8g1jEHmba6toQiwOONlBLqydGaB5P0ZGkSn7Odwa0gENqf_uS7pntcxIBlyhf0QPv7REG2Gg_aBsYsSrS7CGN_46R0ZOk6QMlip7ytQ9vpKwetul_LPz2BKAY6ewp8qlWFh4T7BVGcDU_iBH2uRObNW0N-o1WZq3itxya6oLjIs6z_hR8nBrBzlDtZ4Fsx9EOrZR3YQ1DTnXgdCHP3qBuSeTmyNHWQftwYuXwQf5ZjX1Lsxvk56xT4iQEjfxbqjXb1l0pOsmiwQ_M9d_dq0n4THVmCmKFwNV94eocn9AA")
BOT_TOKEN = getenv("BOT_TOKEN", "5532726746:AAGAnt_MgMDTzUJGvCPMfsV_uLntS8yXf7o")
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
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "ZzZzZ5")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5284259786").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/da8192651bb5f0cd0f1c6.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
