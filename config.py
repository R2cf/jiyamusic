## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AQBul61AHnDv3YLqEkynIx0C-JYpoDsk_QEMJg1k-lGKSSLvCIAy_Ws5THJBJ_VfpH12vWq8w8THHEITuniaQyfWYLCAodWNSvHb5SMBzp79XUo62V12DLxy9eyY00X6vmbZkuTUj-ALB9V13ZJ4In0OPBsiVY02m0D7c7V2MP65TBRo7RD6Aat-1PuipzEHD5StY4BA75VnfQJ2iNk9klQnH2PG8-Fgc804hm_-bMWM27dGZ-MWCm3mP8ytdi7WmT0_l0PmkDJiMS6JFe6-djmNuD0GdsbJFOv1qE4Zp7e3aFmoe3MWlKACVO7Z_s5FwFN8KeQ01DHULfc17I2WDW_1AAAAAUW0OVUA")
BOT_TOKEN = getenv("BOT_TOKEN", "5877944792:AAESum5hHafq5uHhZE38WMqY-ZgC0oJHXTI")
BOT_NAME = getenv("BOT_NAME", "sahumusic")
API_ID = int(getenv("API_ID", "28187851"))
API_HASH = getenv("API_HASH", "9846014bd1d5705a4171f0954bf0e4e1")
OWNER_NAME = getenv("OWNER_NAME", "vijay")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Timesisnotwaiting")
ALIVE_NAME = getenv("ALIVE_NAME", "vijay sahu")
BOT_USERNAME = getenv("BOT_USERNAME", "sahumusic1bot")
OWNER_ID = getenv("OWNER_ID", "5464406357")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "sahumusic")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . ").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/a414e2cdfeaa7d4414b89.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/c540aac0249486854787b.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6f1cfec700087f6fcb391.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/c3547532105a0cb67229d.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/c3401a572375b569138c3.png")
