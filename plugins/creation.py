from pyrogram.errors.exceptions.bad_request_400 import YouBlockedUser

from userge import userge, Message
from userge.utils.exceptions import StopConversation


@userge.on_cmd("cr", about={
    'header': "Creation gives you user's last updated names and usernames.",
    'flags': {
        '-u': "To get Username history of a User"},
    'usage': "{tr}cr [Reply to user]\n"
             "{tr}cr -u [Reply to user]"})
async def creation_(message: Message):
    """ Get User's Created Date """
    replied = message.reply_to_message
    if not replied:
        await message.err("```Reply to get creation History...```", del_in=5)
        return
    user = replied.from_user.id
    chat = "@creationdatebot"
    await message.edit("```Getting info, Wait plox ...```")
    msgs = []
    ERROR_MSG = "For your kind information, you blocked @creationdatebot, Unblock it"
    try:
        async with userge.conversation(chat) as conv:
            try:
                await conv.send_message("/id {}".format(user))
            except YouBlockedUser:
                await message.err(f"**{ERROR_MSG}**", del_in=5)
                return
            msgs.append(await conv.get_response(mark_read=True))
            msgs.append(await conv.get_response(mark_read=True))
            msgs.append(await conv.get_response(timeout=3, mark_read=True))
    except StopConversation:
        pass
    message = "Message"
    message = "Message"
    for msg in msgs:
        if '-u' in message.flags:
            if msg.text.startswith("No records found"):
                await message.edit("```User is alien...```", del_in=5)
                return
            if msg.text.startswith(message):
                await message.edit(f"`{msg.text}`")
        else:
            if msg.text.startswith("No records found"):
                await message.edit("```User is alien...```", del_in=5)
                return
            if msg.text.startswith(message):
                await message.edit(f"`{msg.text}`")
