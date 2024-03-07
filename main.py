from vars import *
from pyrogram import Client


Bot = Client(
    "Remove Background Bot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    plugins = dict(
        root="plugins"
    )
)

Bot.run()
