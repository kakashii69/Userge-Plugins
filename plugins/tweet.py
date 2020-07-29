""" Fun Stickers for Tweet """

# By @Krishna_Singhal

import os
import re
import requests

from PIL import Image
from validators.url import url

from userge import userge, Config, Message

CONVERTED_IMG = Config.DOWN_PATH + "img.png"
CONVERTED_STIKR = Config.DOWN_PATH + "sticker.webp"

EMOJI_PATTERN = re.compile(
    "["
    "\U0001F1E0-\U0001F1FF"  # flags (iOS)
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\U0001F700-\U0001F77F"  # alchemical symbols
    "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
    "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
    "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
    "\U0001FA00-\U0001FA6F"  # Chess Symbols
    "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
    "\U00002702-\U000027B0"  # Dingbats
    "]+")


@userge.on_cmd("trump", about={
    'header': "Custom Sticker of Trump Tweet",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}trump [text | reply to text]"})
async def trump_tweet(msg: Message):
    """ Fun sticker of Trump Tweet """
    replied = msg.reply_to_message
    if replied and not msg.filtered_input_str:
        text = replied.text
    else:
        text = msg.filtered_input_str
    if not text:
        await msg.err("```Trump Need some Text for Tweet ð```", del_in=3)
        return
    await msg.edit("```Requesting trump to tweet... ð```")
    await _tweets(text, type_="trumptweet")
    await _finalize(msg)


@userge.on_cmd("modi", about={
    'header': "Custom Sticker of Modi Tweet",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}trump [text | reply to text]"})
async def modi_tweet(msg: Message):
    """ Fun Sticker of Modi Tweet """
    replied = msg.reply_to_message
    if replied and not msg.filtered_input_str:
        text = replied.text
    else:
        text = msg.filtered_input_str
    if not text:
        await msg.err("```Modi Need some Text for Tweet ð```", del_in=3)
        return
    await msg.edit("```Requesting Modi to tweet... ð```")
    await _tweets(text, "narendramodi")
    await _finalize(msg)


@userge.on_cmd("cmm", about={
    'header': "Custom Sticker of Change My Mind",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}cmm [text | reply to text]"})
async def Change_My_Mind(msg: Message):
    """ Custom Sticker or Banner of Change My Mind """
    replied = msg.reply_to_message
    if replied and not msg.filtered_input_str:
        text = replied.text
    else:
        text = msg.filtered_input_str
    if not text:
        await msg.err("```Need some Text to Change My Mind ð```", del_in=3)
        return
    await msg.edit("```Writing Banner of Change My Mind ð```")
    await _tweets(text, type_="changemymind")
    await _finalize(msg)


@userge.on_cmd("kanna", about={
    'header': "Custom text Sticker of kanna",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}kanna [text | reply to text]"})
async def kanna(msg: Message):
    """ Fun sticker of Kanna """
    replied = msg.reply_to_message
    if replied and not msg.filtered_input_str:
        text = replied.text
    else:
        text = msg.filtered_input_str
    if not text:
        await msg.err("```Kanna Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```Kanna is writing for You ð```")
    await _tweets(text, type_="kannagen")
    await _finalize(msg)


@userge.on_cmd("salmon", about={
    'header': "Custom text Sticker of Salmon Bhai",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}salmon [text | reply to text]"})
async def BeingSalmanKhan(msg: Message):
    """ Fun Sticker of Salmon Bhai Tweet """
    replied = msg.reply_to_message
    if replied and not msg.filtered_input_str:
        text = replied.text
    else:
        text = msg.filtered_input_str
    if not text:
        await msg.err("```Salmon Bhai Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```Salmon Bhai is writing for You ð```")
    await _tweets(text, "BeingSalmanKhan")
    await _finalize(msg)

@userge.on_cmd("srk", about={
    'header': "Custom text Sticker of SRK",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}srk [text | reply to text]"})
async def iamsrk(msg: Message):
    """ Fun Sticker of SRK Tweet """
    replied = msg.reply_to_message
    if replied and not msg.filtered_input_str:
        text = replied.text
    else:
        text = msg.filtered_input_str
    if not text:
        await msg.err("```SRK Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```SRK is writing for You ð```")
    await _tweets(text, "iamsrk")
    await _finalize(msg)

@userge.on_cmd("ab", about={
    'header': "Custom text Sticker of Amitabh",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}ab [text | reply to text]"})
async def SrBachchan(msg: Message):
    """ Fun Sticker of SrBachchan Tweet """
    replied = msg.reply_to_message
    if replied and not msg.filtered_input_str:
        text = replied.text
    else:
        text = msg.filtered_input_str
    if not text:
        await msg.err("```SrBachchan Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```SrBachchan is writing for You ð```")
    await _tweets(text, "SrBachchan")
    await _finalize(msg)

@userge.on_cmd("ambani", about={
    'header': "Custom text Sticker of Ambani",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}ambani [text | reply to text]"})
async def Asliambani(msg: Message):
    """ Fun Sticker of Ambani Tweet """
    replied = msg.reply_to_message
    if replied and not msg.filtered_input_str:
        text = replied.text
    else:
        text = msg.filtered_input_str
    if not text:
        await msg.err("```ambani Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```ambani is writing for You ð```")
    await _tweets(text, "Asliambani")
    await _finalize(msg)

@userge.on_cmd("jio", about={
    'header': "Custom text Sticker of Jio",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}jio [text | reply to text]"})
async def reliancejio(msg: Message):
    """ Fun Sticker of Jio Tweet """
    replied = msg.reply_to_message
    if replied and not msg.filtered_input_str:
        text = replied.text
    else:
        text = msg.filtered_input_str
    if not text:
        await msg.err("```Jio Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```Jio is writing for You ð```")
    await _tweets(text, "reliancejio")
    await _finalize(msg)

@userge.on_cmd("ash", about={
    'header': "Custom text Sticker of Ash",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}ash [text | reply to text]"})
async def AshwariyaRai(msg: Message):
    """ Fun Sticker of Ash Tweet """
    replied = msg.reply_to_message
    if replied and not msg.filtered_input_str:
        text = replied.text
    else:
        text = msg.filtered_input_str
    if not text:
        await msg.err("```Ash Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```Ash is writing for You ð```")
    await _tweets(text, "AshwariyaRai")
    await _finalize(msg)

@userge.on_cmd("rekha", about={
    'header': "Custom text Sticker of Rekha",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}rekha [text | reply to text]"})
async def TheRekhaFanclub(msg: Message):
    """ Fun Sticker of Rekha Tweet """
    replied = msg.reply_to_message
    if replied and not msg.filtered_input_str:
        text = replied.text
    else:
        text = msg.filtered_input_str
    if not text:
        await msg.err("```Rekha Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```Rekha is writing for You ð```")
    await _tweets(text, "TheRekhaFanclub")
    await _finalize(msg)

@userge.on_cmd("telegram", about={
    'header': "Custom text Sticker of Telegram",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}telegram [text | reply to text]"})
async def telegram(msg: Message):
    """ Fun Sticker of Telegram Tweet """
    replied = msg.reply_to_message
    if replied and not msg.filtered_input_str:
        text = replied.text
    else:
        text = msg.filtered_input_str
    if not text:
        await msg.err("```Telegram Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```Telegram is writing for You ð```")
    await _tweets(text, "telegram")
    await _finalize(msg)

@userge.on_cmd("whatsapp", about={
    'header': "Custom text Sticker of Whatsapp",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}whatsapp [text | reply to text]"})
async def WhatsApp(msg: Message):
    """ Fun Sticker of Whatsapp Tweet """
    replied = msg.reply_to_message
    if replied and not msg.filtered_input_str:
        text = replied.text
    else:
        text = msg.filtered_input_str
    if not text:
        await msg.err("```Whatsapp Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```Whatsapp is writing for You ð```")
    await _tweets(text, "WhatsApp")
    await _finalize(msg)

@userge.on_cmd("ananya", about={
    'header': "Custom text Sticker of Ananya",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}ananya [text | reply to text]"})
async def ananyapandayy(msg: Message):
    """ Fun Sticker of ananya Tweet """
    replied = msg.reply_to_message
    if replied and not msg.filtered_input_str:
        text = replied.text
    else:
        text = msg.filtered_input_str
    if not text:
        await msg.err("```Ananya Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```Ananya is writing for You ð```")
    await _tweets(text, "ananyapandayy")
    await _finalize(msg)

@userge.on_cmd("sonakshi", about={
    'header': "Custom text Sticker of Sonakshi",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}sonakshi [text | reply to text]"})
async def Aslisonagold(msg: Message):
    """ Fun Sticker of Sonakshi Tweet """
    replied = msg.reply_to_message
    if replied and not msg.filtered_input_str:
        text = replied.text
    else:
        text = msg.filtered_input_str
    if not text:
        await msg.err("```Sonakshi Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```Sonakshi is writing for You ð```")
    await _tweets(text, "Aslisonagold")
    await _finalize(msg)

@userge.on_cmd("sonam", about={
    'header': "Custom text Sticker of Sonam",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}srk [text | reply to text]"})
async def sonamakapoor(msg: Message):
    """ Fun Sticker of Sonam Tweet """
    replied = msg.reply_to_message
    if replied and not msg.filtered_input_str:
        text = replied.text
    else:
        text = msg.filtered_input_str
    if not text:
        await msg.err("```Sonam Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```Sonam is writing for You ð```")
    await _tweets(text, "sonamakapoor")
    await _finalize(msg)

@userge.on_cmd("johar", about={
    'header': "Custom text Sticker of Karan Johar",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr} johar [text | reply to text]"})
async def karanjohar(msg: Message):
    """ Fun Sticker of Karan Johar Tweet """
    replied = msg.reply_to_message
    if replied and not msg.filtered_input_str:
        text = replied.text
    else:
        text = msg.filtered_input_str
    if not text:
        await msg.err("```Karan Johar Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```Karan Johar is writing for You ð```")
    await _tweets(text, "karanjohar")
    await _finalize(msg)

@userge.on_cmd("yogi", about={
    'header': "Custom text Sticker of yogi ji",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}yogi [text | reply to text]"})
async def myogiadityanath(msg: Message):
    """ Fun Sticker of  yogi jiweet """
    replied = msg.reply_to_message
    if replied and not msg.filtered_input_str:
        text = replied.text
    else:
        text = msg.filtered_input_str
    if not text:
        await msg.err("```Yogi Ji Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```Yogi Ji is writing for You ð```")
    await _tweets(text, "myogiadityanath")
    await _finalize(msg)

@userge.on_cmd("ramdev", about={
    'header': "Custom text Sticker of Baba Ramdev",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}ramdev [text | reply to text]"})
async def yogrishiramdev(msg: Message):
    """ Fun Sticker of Ramdev Tweet """
    replied = msg.reply_to_message
    if replied and not msg.filtered_input_str:
        text = replied.text
    else:
        text = msg.filtered_input_str
    if not text:
        await msg.err("```Ramdev Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```Ramdev is writing for You ð```")
    await _tweets(text, "yogrishiramdev")
    await _finalize(msg)

@userge.on_cmd("sudhir", about={
    'header': "Custom text Sticker of Sudhir",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}sudhir [text | reply to text]"})
async def sudhirchaudhary(msg: Message):
    """ Fun Sticker of Sudhir Tweet """
    replied = msg.reply_to_message
    if replied and not msg.filtered_input_str:
        text = replied.text
    else:
        text = msg.filtered_input_str
    if not text:
        await msg.err("```Sudhir Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```Sudhir is writing for You ð```")
    await _tweets(text, "sudhirchaudhary")
    await _finalize(msg)

@userge.on_cmd("arnab", about={
    'header': "Custom text Sticker of Arnab",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}arnab [text | reply to text]"})
async def ArnabGoswamiRTV(msg: Message):
    """ Fun Sticker of Arnab Tweet """
    replied = msg.reply_to_message
    if replied and not msg.filtered_input_str:
        text = replied.text
    else:
        text = msg.filtered_input_str
    if not text:
        await msg.err("```Arnab Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```Arnab is writing for You ð```")
    await _tweets(text, "ArnabGoswamiRTV")
    await _finalize(msg)

@userge.on_cmd("rahul", about={
    'header': "Custom text Sticker of rahul",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}rahul [text | reply to text]"})
async def RahulGandhi(msg: Message):
    """ Fun Sticker of Rahul Tweet """
    replied = msg.reply_to_message
    if replied and not msg.filtered_input_str:
        text = replied.text
    else:
        text = msg.filtered_input_str
    if not text:
        await msg.err("```Rahul Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```Rahul is writing for You ð```")
    await _tweets(text, "RahulGandhi")
    await _finalize(msg)

@userge.on_cmd("amitshah", about={
    'header': "Custom text Sticker of Amitshah",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}AmitShah [text | reply to text]"})
async def iamsrk(msg: Message):
    """ Fun Sticker of amit shah Tweet """
    replied = msg.reply_to_message
    if replied and not msg.filtered_input_str:
        text = replied.text
    else:
        text = msg.filtered_input_str
    if not text:
        await msg.err("```Amit Shah Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```Amit Shah is writing for You ð```")
    await _tweets(text, "AmitShah")
    await _finalize(msg)

@userge.on_cmd("rubika", about={
    'header': "Custom text Sticker of rubika",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}rubika [text | reply to text]"})
async def RubikaLiyaquat(msg: Message):
    """ Fun Sticker of rubika Tweet """
    replied = msg.reply_to_message
    if replied and not msg.filtered_input_str:
        text = replied.text
    else:
        text = msg.filtered_input_str
    if not text:
        await msg.err("```rubika Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```rubika is writing for You ð```")
    await _tweets(text, "RubikaLiyaquat")
    await _finalize(msg)

@userge.on_cmd("amish", about={
    'header': "Custom text Sticker of Amish Devgan",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}amish [text | reply to text]"})
async def AMISHDEVGAN(msg: Message):
    """ Fun Sticker of Amish Tweet """
    replied = msg.reply_to_message
    if replied and not msg.filtered_input_str:
        text = replied.text
    else:
        text = msg.filtered_input_str
    if not text:
        await msg.err("```Amish Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```Amish is writing for You ð```")
    await _tweets(text, "AMISHDEVGAN")
    await _finalize(msg)

@userge.on_cmd("deepak", about={
    'header': "Custom text Sticker of deepak",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}deepak [text | reply to text]"})
async def DChaurasia2312(msg: Message):
    """ Fun Sticker of deepak Tweet """
    replied = msg.reply_to_message
    if replied and not msg.filtered_input_str:
        text = replied.text
    else:
        text = msg.filtered_input_str
    if not text:
        await msg.err("```deepak Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```deepak is writing for You ð```")
    await _tweets(text, "DChaurasia2312")
    await _finalize(msg)

@userge.on_cmd("tweet", about={
    'header': "Tweet With Custom text Sticker",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}tweet Text , Username\n"
             "{tr}tweet Text\n"
             "{tr}tweet [Text | with reply to User]"})
async def tweet(msg: Message):
    """ Tweet with your own Username """
    replied = msg.reply_to_message
    if replied and not msg.filtered_input_str:
        text = replied.text
    else:
        text = msg.filtered_input_str
    if not text:
        await msg.err("```Give Me some text to Tweet ð```", del_in=3)
        return
    username = ''
    if ',' in text:
        text, username = text.split(',')
    if not username:
        if replied:
            username = replied.from_user.username or replied.from_user.first_name
        else:
            username = msg.from_user.username or msg.from_user.first_name
    await msg.edit("```Creating a Tweet Sticker ð```")
    await _tweets(text.strip(), username.strip())
    await _finalize(msg)


def _deEmojify(inputString: str) -> str:
    """Remove emojis and other non-safe characters from string"""
    return re.sub(EMOJI_PATTERN, '', inputString)


async def _tweets(text: str, username: str = '', type_: str = "tweet") -> None:
    api_url = f"https://nekobot.xyz/api/imagegen?type={type_}&text={_deEmojify(text)}"
    if username:
        api_url += f"&username={_deEmojify(username)}"
    res = requests.get(api_url).json()
    tweets_ = res.get("message")
    if not url(tweets_):
        return "```Invalid Syntax, Exiting...```"
    tmp_file = Config.DOWN_PATH + "temp.png"
    with open(tmp_file, "wb") as t_f:
        t_f.write(requests.get(tweets_).content)
    img = Image.open(tmp_file)
    img.save(CONVERTED_IMG)
    img.save(CONVERTED_STIKR)
    os.remove(tmp_file)


async def _finalize(msg: Message) -> None:
    await msg.delete()
    msg_id = msg.reply_to_message.message_id if msg.reply_to_message else None
    if '-s' in msg.flags:
        await msg.client.send_sticker(chat_id=msg.chat.id,
                                      sticker=CONVERTED_STIKR,
                                      reply_to_message_id=msg_id)
    else:
        await msg.client.send_photo(chat_id=msg.chat.id,
                                    photo=CONVERTED_IMG,
                                    reply_to_message_id=msg_id)
    for files in (CONVERTED_IMG, CONVERTED_STIKR):
        if files and os.path.exists(files):
            os.remove(files)
