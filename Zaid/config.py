##Config
import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


load_dotenv()
SESSION_NAME = getenv('SESSION_NAME', 'AQBul61AHnDv3YLqEkynIx0C-JYpoDsk_QEMJg1k-lGKSSLvCIAy_Ws5THJBJ_VfpH12vWq8w8THHEITuniaQyfWYLCAodWNSvHb5SMBzp79XUo62V12DLxy9eyY00X6vmbZkuTUj-ALB9V13ZJ4In0OPBsiVY02m0D7c7V2MP65TBRo7RD6Aat-1PuipzEHD5StY4BA75VnfQJ2iNk9klQnH2PG8-Fgc804hm_-bMWM27dGZ-MWCm3mP8ytdi7WmT0_l0PmkDJiMS6JFe6-djmNuD0GdsbJFOv1qE4Zp7e3aFmoe3MWlKACVO7Z_s5FwFN8KeQ01DHULfc17I2WDW_1AAAAAUW0OVUA')
BOT_TOKEN = getenv('BOT_TOKEN', '5877944792:AAESum5hHafq5uHhZE38WMqY-ZgC0oJHXTI')
API_ID = int(getenv("API_ID", "28187851"))
API_HASH = getenv('API_HASH', '9846014bd1d5705a4171f0954bf0e4e1')
DURATION_LIMIT = int(getenv('DURATION_LIMIT', '540000'))
COMMAND_PREFIXES = list(getenv('COMMAND_PREFIXES', '/ !').split())
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Ajju:Ajaysahu@cluster0.lpts5lo.mongodb.net/?retryWrites=true&w=majority")
SUDO_USERS = list(map(int, getenv('SUDO_USERS', '5464406357').split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", '-1001689509291'))
ASS_ID = int(getenv("ASS_ID"))
OWNER_ID = list(map(int, getenv('OWNER_ID', '5464406357').split()))
RESULT_PIC = getenv('RESULT_PIC', "https://telegra.ph/file/62c6a23532aed6f4def02.jpg")
PLAYLIST_PIC = getenv('PLAYLIST_PIC', "https://telegra.ph/file/cf12b3276d8b2f1aefe48.jpg")
PING_IMG = getenv('PING_IMG', "https://telegra.ph/file/85c226cce124d25c5b2ad.jpg")
AUTO_LEAVE_TIME = int(getenv("AUTO_LEAVE_ASSISTANT_TIME", "5400"))
AUTO_LEAVE = getenv('AUTO_LEAVING_ASSISTANT', 'none')
