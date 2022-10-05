
from sys import version as pyver
from pyrogram import __version__ as pyrover
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from unicorns import ALIVE_MSG, BOT_VERSION, CHANNEL, HELP, HOSTNAME, USER
from geezram.core import (
    edit,
    extract_args,
    get_translation,
    reply,
    reply_doc,
    unicorn,
    send_log,
)
logo = "https://telegra.ph/file/4b788cea5c1413f9496a3.png"
@unicorn(pattern='^.alive$')
async def alive(client: unicorn, e: Message):
    ids = 0
    try:
        if unicorn:
            ids += 1
        Alive_msg = f"**[Unicorn-Pyrobot](https://t.me/deldelinaa):**\n\n"
        Alive_msg += f"**Python:** `{pyver.split()[0]}`\n"
        Alive_msg += f"**Pyrogram:** `{pyrover}`\n"
        Alive_msg += f"**Profiles:** [Unicorn](t.me/{USER},{HOSTNAME})\n"
        Alive_msg += f"**Unicorn Version:** `{BOT_VERSION}\n\n`"
        Alive_msg += f"**Powered By : Geez | RAM | TOD**"
        await e.reply_photo(
        photo=logo,
        caption=Alive_msg,
        reply_markup=InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton(
                        "• Geez •", url="https://t.me/GeezSupport")
                ], [
                    InlineKeyboardButton(
                        "• RAM •", url="https://t.me/ramsupportt")
                ]],
        ),
    ) 
    except Exception as lol:         
        Alive_msg = f"Unicorn-Pyrobot, Lets magic begin... \n\n"
        Alive_msg += f"**Profiles:** [Unicorn](t.me/{USER})\n"
        Alive_msg += f"**Unicorn Version:** {BOT_VERSION}\n"
        Alive_msg += f"Powered by Geez and RAM \n"
        await e.reply_photo(
        photo=logo,
        caption=Alive_msg,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton ("• Geez •", url="https://t.me/GeezSupport"),
                ],
                [
                    InlineKeyboardButton("• RAM •", url="https://t.me/ramsupportt"),
                ],
            ],
        ),
    ) 
