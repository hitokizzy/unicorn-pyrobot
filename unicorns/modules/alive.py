import asyncio

from sys import version as pyver
from pyrogram import __version__ as pyrover
from pyrogram.types import Message
from unicorns import ALIVE_MSG, BOT_VERSION, CHANNEL, HELP, HOSTNAME, SUPPORT_GROUP, USER
from geezram.core import (
    edit,
    extract_args,
    get_translation,
    reply,
    reply_doc,
    unicorn,
    send_log,
)

async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time

def ReplyCheck(message: Message):
    reply_id = None

    if message.reply_to_message:
        reply_id = message.reply_to_message.id

    elif not message.from_user.is_self:
        reply_id = message.id

    return reply_id

async def edit_or_reply(message: Message, *args, **kwargs) -> Message:
    apa = (
        message.edit_text
        if bool(message.from_user and message.from_user.is_self or message.outgoing)
        else (message.reply_to_message or message).reply_text
    )
    return await apa(*args, **kwargs)


eor = edit_or_reply


Client : unicorn
alive_logo = "https://telegra.ph/file/4b788cea5c1413f9496a3.png"

@unicorn(pattern='^.alive$')
async def alive(client: Client, message: Message):
    xx = await eor(message)
    await asyncio.sleep(2)
    send = client.send_video if alive_logo.endswith(".mp4") else client.send_photo
    man = (
        f"**[Unicorn's](https://xnxx.com) is Online!.**\n\n"
        f"<b>{ALIVE_MSG}</b>\n\n"
        f"<b>Master :</b> {client.me.mention} \n"
        f"<b>Bot Version :</b> <code>{BOT_VERSION}</code> \n"
        f"<b>Python Version :</b> <code>{pyver()}</code> \n"
        f"<b>Pyrogram Version :</b> <code>{pyrover}</code> \n"
        f"    **[𝗦𝘂𝗽𝗽𝗼𝗿𝘁](https://t.me/{SUPPORT_GROUP})** | **[𝗖𝗵𝗮𝗻𝗻𝗲𝗹](https://t.me/{CHANNEL})** | **[𝗢𝘄𝗻𝗲𝗿](tg://user?id={client.me.id})**"
    )
    try:
        await asyncio.gather(
            xx.delete(),
            send(
                message.chat.id,
                alive_logo,
                caption=man,
                reply_to_message_id=ReplyCheck(message),
            ),
        )
    except BaseException:
        await xx.edit(man, disable_web_page_preview=True)
