from pyrogram import Client as Bot
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


START_TEXT = """𝐇𝐞𝐥𝐥𝐨 {} 🧸❤️,

🇮🇳 𝐈 𝐚𝐦 𝐚 𝐦𝐞𝐝𝐢𝐚 𝐛𝐚𝐜𝐤𝐠𝐫𝐨𝐮𝐩 𝐫𝐞𝐦𝐨𝐯𝐞𝐫 𝐛𝐨𝐭. \
𝐒𝐞𝐧𝐝 𝐦𝐞 𝐚 𝐩𝐡𝐨𝐭𝐨 𝐢 𝐰𝐢𝐥𝐥 𝐬𝐞𝐧𝐝 𝐭𝐡𝐞 𝐩𝐡𝐨𝐭𝐨 𝐰𝐢𝐭𝐡𝐨𝐮𝐭 𝐁𝐚𝐜𝐤𝐠𝐫𝐨𝐮𝐧𝐝.


⚔️ ᴘᴏᴡᴇʀᴇᴅ ʙʏ  @synaxnetwork 🦋"""

HELP_TEXT = """--**𝐌𝐨𝐫𝐞 𝐇𝐞𝐥𝐩**--

➩ ᴊᴜsᴛ sᴇɴᴅ ᴍᴇ ᴀ ᴘʜᴏᴛᴏ ᴏʀ ᴠɪᴅᴇᴏ .
➩ ɪ ᴡɪʟʟ ᴅᴏᴡɴʟᴏᴀᴅ ɪᴛ .
➩ ɪ ᴡɪʟʟ sᴇɴᴅ ᴛʜᴇ ᴘʜᴏᴛᴏ ᴏʀ ᴠɪᴅᴇᴏ ᴡɪᴛʜᴏᴜᴛ ʙᴀᴄᴋɢʀᴏᴜɴᴅ .

⚔️ ᴘᴏᴡᴇʀᴇᴅ ʙʏ  @synaxnetwork 🦋"""

ABOUT_TEXT = """**𝐀𝐛𝐨𝐮𝐭 𝐌𝐞 :**

➩ **𝐁𝐨𝐭 🇮🇳 :** `ʙᴀᴄᴋɢʀᴏᴜɴᴅ ʀᴇᴍᴏᴠᴇʀ 🦄`
➩ **𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 ☘️ :** [ɪɴsᴛᴀɢʀᴀᴍ ](https://instagram.com/sanatanisynax) | [ᴛᴇʟᴇɢʀᴀᴍ ](https://telegram.me/synaxbots)
➩ **𝐒𝐨𝐮𝐫𝐜𝐞 :** [ᴄʟɪᴄᴋ ᴋʀ 🐰](https://t.me/synaxnetwork)
➩ **𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞 :** [ᴘʏᴛʜᴏɴ 3 🦜](https://python.org)
➩ **𝐋𝐢𝐛𝐫𝐚𝐫𝐲 :** [ᴘʏʀᴏɢʀᴀᴍ 🌸](https://pyrogram.org)"""

START_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('🌷 𝐇𝐞𝐥𝐩 🌷', callback_data='help'),
            InlineKeyboardButton('🌴 𝐀𝐛𝐨𝐮𝐭 🌴', callback_data='about'),
            InlineKeyboardButton('🌿 𝐂𝐥𝐨𝐬𝐞 🌿', callback_data='close')
        ],
        [
            InlineKeyboardButton('🍂 𝐅𝐞𝐞𝐝𝐛𝐚𝐜𝐤 🍂', url='https://telegram.me/synaxchatrobot')
        ]
    ]
)

HELP_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('❄️ 𝐇𝐨𝐦𝐞 ❄️', callback_data='home'),
            InlineKeyboardButton('🌴 𝐀𝐛𝐨𝐮𝐭 🌴', callback_data='about'),
            InlineKeyboardButton('🌿 𝐂𝐥𝐨𝐬𝐞 🌿', callback_data='close')
        ]
    ]
)

ABOUT_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('❄️ 𝐇𝐨𝐦𝐞 ❄️', callback_data='home'),
            InlineKeyboardButton('🌷 𝐇𝐞𝐥𝐩 🌷', callback_data='help'),
            InlineKeyboardButton('🌿 𝐂𝐥𝐨𝐬𝐞 🌿', callback_data='close')
        ]
    ]
)

BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('🇮🇳 𝐉𝐨𝐢𝐧 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 🇮🇳', url='https://telegram.me/synaxnetwork')
        ]
    ]
)


@Bot.on_callback_query()
async def cb_data(bot, update):
    if update.data == "home":
        await start(bot, update, cb=True)
    elif update.data == "help":
        await help(bot, update, cb=True)
    elif update.data == "about":
        await about(bot, update, cb=True)
    else:
        await update.message.delete()


@Bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update, cb=False):
    text=START_TEXT.format(update.from_user.mention)
    if cb:
        await update.message.edit_text(
            text=text,
            reply_markup=START_BUTTONS,
            disable_web_page_preview=True
        )
    else:
        await update.reply_text(
            text=text,
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS,
            quote=True
        )


@Bot.on_message(filters.private & filters.command(["help"]))
async def help(bot, update, cb=False):
    if cb:
        await update.message.edit_text(
            text=HELP_TEXT,
            reply_markup=HELP_BUTTONS,
            disable_web_page_preview=True
        )
    else:
        await update.reply_text(
            text=HELP_TEXT,
            reply_markup=HELP_BUTTONS,
            disable_web_page_preview=True,
            quote=True
        )


@Bot.on_message(filters.private & filters.command(["about"]))
async def about(bot, update, cb=False):
    if cb:
        await update.message.edit_text(
            text=ABOUT_TEXT,
            reply_markup=ABOUT_BUTTONS,
            disable_web_page_preview=True
        )
    else:
        await update.reply_text(
            text=ABOUT_TEXT,
            reply_markup=ABOUT_BUTTONS,
            disable_web_page_preview=True,
            quote=True
        )
