import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")

REMOVEBG_API = os.environ.get("REMOVEBG_API", "mUEGiJgeMHjVYNS848nzRXdh")
UNSCREEN_API = os.environ.get("UNSCREEN_API", "m5dDivDgRhrxZmmem1X6ZZ21")
