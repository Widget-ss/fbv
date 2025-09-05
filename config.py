#(©)CodeXBotz

import os
import logging
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv()

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7741860033:AAERjUiuUNQsjztlHeL1Px2zgc8zYaGFQsE")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "26788480"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "858d65155253af8632221240c535c314")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002992676853"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "7845991207"))

#Port
PORT = os.environ.get("PORT", "8045")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://k2link:K2link123@k2link.oq3vz.mongodb.net/?retryWrites=true&w=majority&appName=k2link")
DB_NAME = os.environ.get("DATABASE_NAME", "k2link")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))
JOIN_REQUEST_ENABLE = os.environ.get("JOIN_REQUEST_ENABLED", None)

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_PIC = os.environ.get("START_PIC","")
START_MSG = os.environ.get("START_MESSAGE", "Just a file bot !")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "7835791027").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else True

# Auto delete time in seconds.
AUTO_DELETE_TIME = int(os.getenv("AUTO_DELETE_TIME", "600"))
AUTO_DELETE_MSG = os.environ.get("AUTO_DELETE_MSG", "This is DEMO videos for Buying all videos in cheap price DM - @VerifiedPopo\n\nये सिर्फ डेमो है, वीडियो का पैकेज खरीदने के लिए DM करे !")
AUTO_DEL_SUCCESS_MSG = os.environ.get("AUTO_DEL_SUCCESS_MSG", "Video Deleted. for buying our service in cheap price. DM - @VerifiedPopo\n\nये सिर्फ डेमो है, वीडियो का पैकेज खरीदने के लिए DM करे !")

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(7572277094)
ADMINS.append(6517098590)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
