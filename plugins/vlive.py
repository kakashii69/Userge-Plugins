from pyrogram.errors.exceptions import FileIdInvalid, FileReferenceEmpty
from pyrogram.errors.exceptions.bad_request_400 import BadRequest, ChannelInvalid, MediaEmpty

from userge import userge, Message, Config, versions, get_version

AUDIO_ID, AUDIO_REF = None, None


@userge.on_cmd("vlive", about={
    'header': "This command is just for fun"}, allow_channels=True)
async def alive(message: Message):
    await message.delete()
    await sendit(message)
    output = f"""
**==USERGE=ACTIVATED==**
"""
    await message.client.send_message(message.chat.id, output)


async def refresh_id():
    global AUDIO_ID, AUDIO_REF
    audio = (await userge.get_messages('userbotsound', 2)).voice
    AUDIO_ID = audio.file_id
    AUDIO_REF = audio.file_ref


async def send_voice(message):
    try:
        await message.client.send_voice(
            message.chat.id, AUDIO_ID, file_ref=AUDIO_REF, caption="💥USERGE is Up and Running💥\n\n       Durable as a Lawda_\n•repo: https://github.com/ravana69/Userge \n• python version : 3.8.3\n• pyrogram version : 0.17.1-async\n• userge version : 0.1.6-Ultra-Pro\n• license : GNU General Public License v3.0\n• copyright : Copyright (C) 2020 by UsergeTeam@Github")
    except MediaEmpty:
        pass


async def sendit(message):
    if AUDIO_ID:
        try:
            await send_voice(message)
        except (FileIdInvalid, FileReferenceEmpty, BadRequest):
            try:
                await refresh_id()
            except ChannelInvalid:
                pass
            else:
                await send_voice(message)
    else:
        try:
            await refresh_id()
        except ChannelInvalid:
            pass
        else:
            await send_voice(message)
