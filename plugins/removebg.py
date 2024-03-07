import os
import requests
from vars import *
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


ERROR_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('Help', callback_data='help'),
            InlineKeyboardButton('Close', callback_data='close')
        ]
    ]
)

@Client.on_message(filters.private & (filters.photo | filters.video | filters.document | filters.animation))
async def remove_background(bot, update):
    if not (REMOVEBG_API or UNSCREEN_API):
        await update.reply_text(
            text="Error :- API not found",
            quote=True,
            disable_web_page_preview=True,
            reply_markup=ERROR_BUTTONS
        )
        return
    await update.reply_chat_action(enums.ChatAction.TYPING)
    message = await update.reply_text(
        text="Processing",
        quote=True,
        disable_web_page_preview=True
    )
    try:
        
        new_file_name = "./downloads/"
        
        if (
            update.photo or (
                update.document and "image" in update.document.mime_type
            )
        ):
            new_file_name += f"{str(update.from_user.id)}.png"
            file = await update.download()
            await message.edit_text(
                text="Photo downloaded successfully. Now removing background.",
                disable_web_page_preview=True
            )
            new_document = removebg_image(file)
            
        elif (
            update.video or update.animation or (
                update.document and "video" in update.document.mime_type
            )
        ):
            file = await update.download()
            await message.edit_text(
                text="Video downloaded successfully. Now removing background.",
                disable_web_page_preview=True
            )
            id, new_document = removebg_video(file)
            new_file_name += id+".mp4"
            
        else:
            await message.edit_text(
                text="Media not supported",
                disable_web_page_preview=True,
                reply_markup=ERROR_BUTTONS
            )
        try:
            os.remove(file)
        except:
            pass
    except Exception as error:
        await message.edit_text(
            text=error,
            disable_web_page_preview=True
        )
    try:
        with open(new_file_name, "wb") as file:
            file.write(new_document.content)
        await update.reply_chat_action(enums.ChatAction.UPLOAD_DOCUMENT)
    except Exception as error:
        await message.edit_text(
           text=error,
           reply_markup=ERROR_BUTTONS
        )
        return
    try:
        await update.reply_document(
            document=new_file_name,
            quote=True
        )
        try:
            os.remove(new_file_name)
        except:
            pass
    except Exception as error:
        await message.edit_text(
            text=f"Error:- `{error}`",
            disable_web_page_preview=True,
            reply_markup=ERROR_BUTTONS
        )


def removebg_image(file):
    api = "https://api.remove.bg/v1.0/removebg"
    files = {"image_file": open(file, "rb")}
    data = {"size": "auto"}
    headers = {"X-Api-Key": REMOVEBG_API}
    r = requests.post(api, files=files, data=data, headers=headers)
    return r


def removebg_video(file):
    api = "https://api.unscreen.com/v1.0/videos"
    files = {"video_file": open(file, "rb")}
    headers = {"X-Api-Key": UNSCREEN_API}
    response = requests.post(api, files=files, headers=headers)
    id = response.json()["data"]["id"]
    r = requests.get(response.json()["data"]["attributes"]["result_url"])
    return id, r

