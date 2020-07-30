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
    text = msg.filtered_input_str
    if replied and not text:
        text = replied.text
    if not text:
        await msg.err("```Trump Need some Text for Tweet ð```", del_in=3)
        return
    await msg.edit("```Requesting trump to tweet... ð```")
    await _tweets(text, type_="trumptweet")
    

@userge.on_cmd("modi", about={
    'header': "Custom Sticker of Modi Tweet",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}modi [text | reply to text]"})
async def modi_tweet(msg: Message):
    """ Fun Sticker of Modi Tweet """
    replied = msg.reply_to_message
    text = msg.filtered_input_str
    if replied and not text:
        text = replied.text
    if not text:
        await msg.err("```Modi Need some Text for Tweet ð```", del_in=3)
        return
    await msg.edit("```Requesting Modi to tweet... ð```")
    await _tweets(text, "narendramodi")
    

@userge.on_cmd("cmm", about={
    'header': "Custom Sticker of Change My Mind",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}cmm [text | reply to text]"})
async def Change_My_Mind(msg: Message):
    """ Custom Sticker or Banner of Change My Mind """
    replied = msg.reply_to_message
    text = msg.filtered_input_str
    if replied and not text:
        text = replied.text
    if not text:
        await msg.err("```Need some Text to Change My Mind ð```", del_in=3)
        return
    await msg.edit("```Writing Banner of Change My Mind ð```")
    await _tweets(text, type_="changemymind")
    

@userge.on_cmd("kanna", about={
    'header': "Custom text Sticker of kanna",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}kanna [text | reply to text]"})
async def kanna(msg: Message):
    """ Fun sticker of Kanna """
    replied = msg.reply_to_message
    text = msg.filtered_input_str
    if replied and not text:
        text = replied.text
    if not text:
        await msg.err("```Kanna Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```Kanna is writing for You ð```")
    await _tweets(text, type_="kannagen")
    

@userge.on_cmd("salmon", about={
    'header': "Custom text Sticker of Salmon Bhai",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}salmon [text | reply to text]"})
async def BeingSalmanKhan(msg: Message):
    """ Fun Sticker of Salmon Bhai Tweet """
    replied = msg.reply_to_message
    text = msg.filtered_input_str
    if replied and not text:
        text = replied.text
    if not text:
        await msg.err("```Salmon Bhai Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```Salmon Bhai is writing for You ð```")
    await _tweets(text, "BeingSalmanKhan")
    
@userge.on_cmd("srk", about={
    'header': "Custom text Sticker of SRK",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}srk [text | reply to text]"})
async def iamsrk(msg: Message):
    """ Fun Sticker of SRK Tweet """
    replied = msg.reply_to_message
    text = msg.filtered_input_str
    if replied and not text:
        text = replied.text
    if not text:
        await msg.err("```SRK Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```SRK is writing for You ð```")
    await _tweets(text, "iamsrk")
    
@userge.on_cmd("ab", about={
    'header': "Custom text Sticker of Amitabh",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}ab [text | reply to text]"})
async def SrBachchan(msg: Message):
    """ Fun Sticker of SrBachchan Tweet """
    replied = msg.reply_to_message
    text = msg.filtered_input_str
    if replied and not text:
        text = replied.text
    if not text:
        await msg.err("```SrBachchan Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```SrBachchan is writing for You ð```")
    await _tweets(text, "SrBachchan")
    
@userge.on_cmd("ambani", about={
    'header': "Custom text Sticker of Ambani",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}ambani [text | reply to text]"})
async def Asliambani(msg: Message):
    """ Fun Sticker of Ambani Tweet """
    replied = msg.reply_to_message
    text = msg.filtered_input_str
    if replied and not text:
        text = replied.text
    if not text:
        await msg.err("```ambani Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```ambani is writing for You ð```")
    await _tweets(text, "Asliambani")
    
@userge.on_cmd("jio", about={
    'header': "Custom text Sticker of Jio",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}jio [text | reply to text]"})
async def reliancejio(msg: Message):
    """ Fun Sticker of Jio Tweet """
    replied = msg.reply_to_message
    text = msg.filtered_input_str
    if replied and not text:
        text = replied.text
    if not text:
        await msg.err("```Jio Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```Jio is writing for You ð```")
    await _tweets(text, "reliancejio")
    
@userge.on_cmd("ash", about={
    'header': "Custom text Sticker of Ash",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}ash [text | reply to text]"})
async def AshwariyaRai(msg: Message):
    """ Fun Sticker of Ash Tweet """
    replied = msg.reply_to_message
    text = msg.filtered_input_str
    if replied and not text:
        text = replied.text
    if not text:
        await msg.err("```Ash Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```Ash is writing for You ð```")
    await _tweets(text, "AshwariyaRai")
    

@userge.on_cmd("rekha", about={
    'header': "Custom text Sticker of Rekha",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}rekha [text | reply to text]"})
async def TheRekhaFanclub(msg: Message):
    """ Fun Sticker of Rekha Tweet """
    replied = msg.reply_to_message
    text = msg.filtered_input_str
    if replied and not text:
        text = replied.text
    if not text:
        await msg.err("```Rekha Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```Rekha is writing for You ð```")
    await _tweets(text, "TheRekhaFanclub")
    
@userge.on_cmd("telegram", about={
    'header': "Custom text Sticker of Telegram",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}telegram [text | reply to text]"})
async def telegram(msg: Message):
    """ Fun Sticker of Telegram Tweet """
    replied = msg.reply_to_message
    text = msg.filtered_input_str
    if replied and not text:
        text = replied.text
    if not text:
        await msg.err("```Telegram Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```Telegram is writing for You ð```")
    await _tweets(text, "telegram")
    
@userge.on_cmd("whatsapp", about={
    'header': "Custom text Sticker of Whatsapp",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}whatsapp [text | reply to text]"})
async def WhatsApp(msg: Message):
    """ Fun Sticker of Whatsapp Tweet """
    replied = msg.reply_to_message
    text = msg.filtered_input_str
    if replied and not text:
        text = replied.text
    if not text:
        await msg.err("```Whatsapp Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```Whatsapp is writing for You ð```")
    await _tweets(text, "WhatsApp")
    
@userge.on_cmd("ananya", about={
    'header': "Custom text Sticker of Ananya",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}ananya [text | reply to text]"})
async def ananyapandayy(msg: Message):
    """ Fun Sticker of ananya Tweet """
    replied = msg.reply_to_message
    text = msg.filtered_input_str
    if replied and not text:
        text = replied.text
    if not text:
        await msg.err("```Ananya Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```Ananya is writing for You ð```")
    await _tweets(text, "ananyapandayy")
    
@userge.on_cmd("sonakshi", about={
    'header': "Custom text Sticker of Sonakshi",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}sonakshi [text | reply to text]"})
async def Aslisonagold(msg: Message):
    """ Fun Sticker of Sonakshi Tweet """
    replied = msg.reply_to_message
    text = msg.filtered_input_str
    if replied and not text:
        text = replied.text
    if not text:
        await msg.err("```Sonakshi Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```Sonakshi is writing for You ð```")
    await _tweets(text, "Aslisonagold")
    
@userge.on_cmd("sonam", about={
    'header': "Custom text Sticker of Sonam",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}srk [text | reply to text]"})
async def sonamakapoor(msg: Message):
    """ Fun Sticker of Sonam Tweet """
    replied = msg.reply_to_message
    text = msg.filtered_input_str
    if replied and not text:
        text = replied.text
    if not text:
        await msg.err("```Sonam Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```Sonam is writing for You ð```")
    await _tweets(text, "sonamakapoor")
    
@userge.on_cmd("johar", about={
    'header': "Custom text Sticker of Karan Johar",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr} johar [text | reply to text]"})
async def karanjohar(msg: Message):
    """ Fun Sticker of Karan Johar Tweet """
    replied = msg.reply_to_message
    text = msg.filtered_input_str
    if replied and not text:
        text = replied.text
    if not text:
        await msg.err("```Karan Johar Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```Karan Johar is writing for You ð```")
    await _tweets(text, "karanjohar")

@userge.on_cmd("yogi", about={
    'header': "Custom text Sticker of yogi ji",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}yogi [text | reply to text]"})
async def myogiadityanath(msg: Message):
    """ Fun Sticker of  yogi jiweet """
    replied = msg.reply_to_message
    text = msg.filtered_input_str
    if replied and not text:
        text = replied.text
    if not text:
        await msg.err("```Yogi Ji Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```Yogi Ji is writing for You ð```")
    await _tweets(text, "myogiadityanath")
    
@userge.on_cmd("ramdev", about={
    'header': "Custom text Sticker of Baba Ramdev",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}ramdev [text | reply to text]"})
async def yogrishiramdev(msg: Message):
    """ Fun Sticker of Ramdev Tweet """
    replied = msg.reply_to_message
    text = msg.filtered_input_str
    if replied and not text:
        text = replied.text
    if not text:
        await msg.err("```Ramdev Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```Ramdev is writing for You ð```")
    await _tweets(text, "yogrishiramdev")
    
@userge.on_cmd("sudhir", about={
    'header': "Custom text Sticker of Sudhir",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}sudhir [text | reply to text]"})
async def sudhirchaudhary(msg: Message):
    """ Fun Sticker of Sudhir Tweet """
    replied = msg.reply_to_message
    text = msg.filtered_input_str
    if replied and not text:
        text = replied.text
    if not text:
        await msg.err("```Sudhir Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```Sudhir is writing for You ð```")
    await _tweets(text, "sudhirchaudhary")
    
@userge.on_cmd("arnab", about={
    'header': "Custom text Sticker of Arnab",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}arnab [text | reply to text]"})
async def ArnabGoswamiRTV(msg: Message):
    """ Fun Sticker of Arnab Tweet """
    replied = msg.reply_to_message
    text = msg.filtered_input_str
    if replied and not text:
        text = replied.text
    if not text:
        await msg.err("```Arnab Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```Arnab is writing for You ð```")
    await _tweets(text, "ArnabGoswamiRTV")
    
@userge.on_cmd("rahul", about={
    'header': "Custom text Sticker of rahul",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}rahul [text | reply to text]"})
async def RahulGandhi(msg: Message):
    """ Fun Sticker of Rahul Tweet """
    replied = msg.reply_to_message
    text = msg.filtered_input_str
    if replied and not text:
        text = replied.text
    if not text:
        await msg.err("```Rahul Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```Rahul is writing for You ð```")
    await _tweets(text, "RahulGandhi")
    
@userge.on_cmd("amitshah", about={
    'header': "Custom text Sticker of Amitshah",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}AmitShah [text | reply to text]"})
async def iamsrk(msg: Message):
    """ Fun Sticker of amit shah Tweet """
    replied = msg.reply_to_message
    text = msg.filtered_input_str
    if replied and not text:
        text = replied.text
    if not text:
        await msg.err("```Amit Shah Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```Amit Shah is writing for You ð```")
    await _tweets(text, "AmitShah")
    
@userge.on_cmd("rubika", about={
    'header': "Custom text Sticker of rubika",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}rubika [text | reply to text]"})
async def RubikaLiyaquat(msg: Message):
    """ Fun Sticker of rubika Tweet """
    replied = msg.reply_to_message
    text = msg.filtered_input_str
    if replied and not text:
        text = replied.text
    if not text:
        await msg.err("```rubika Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```rubika is writing for You ð```")
    await _tweets(text, "RubikaLiyaquat")
    
@userge.on_cmd("amish", about={
    'header': "Custom text Sticker of Amish Devgan",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}amish [text | reply to text]"})
async def AMISHDEVGAN(msg: Message):
    """ Fun Sticker of Amish Tweet """
    replied = msg.reply_to_message
    text = msg.filtered_input_str
    if replied and not text:
        text = replied.text
    if not text:
        await msg.err("```Amish Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```Amish is writing for You ð```")
    await _tweets(text, "AMISHDEVGAN")
    
@userge.on_cmd("deepak", about={
    'header': "Custom text Sticker of deepak",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}deepak [text | reply to text]"})
async def DChaurasia2312(msg: Message):
    """ Fun Sticker of deepak Tweet """
    replied = msg.reply_to_message
    text = msg.filtered_input_str
    if replied and not text:
        text = replied.text
    if not text:
        await msg.err("```deepak Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```deepak is writing for You ð```")
    await _tweets(text, "DChaurasia2312")
    
@userge.on_cmd("elon", about={
    'header': "Custom text Sticker of elon musk",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}elon [text | reply to text]"})
async def elonmusk(msg: Message):
    """ Fun Sticker of elonmusk Tweet """
    replied = msg.reply_to_message
    text = msg.filtered_input_str
    if replied and not text:
        text = replied.text
    if not text:
        await msg.err("```elonmusk Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```deepak is writing for You ð```")
    await _tweets(text, "elonmusk")
        
@userge.on_cmd("spacex", about={
    'header': "Custom text Sticker of SpaceX",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}spacex [text | reply to text]"})
async def SpaceX(msg: Message):
    """ Fun Sticker of SpaceX Tweet """
    replied = msg.reply_to_message
    text = msg.filtered_input_str
    if replied and not text:
        text = replied.text
    if not text:
        await msg.err("```SpaceX Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```deepak is writing for You ð```")
    await _tweets(text, "SpaceX")
        
@userge.on_cmd("isro", about={
    'header': "Custom text Sticker of isro",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}isro [text | reply to text]"})
async def isro(msg: Message):
    """ Fun Sticker of isro Tweet """
    replied = msg.reply_to_message
    text = msg.filtered_input_str
    if replied and not text:
        text = replied.text
    if not text:
        await msg.err("```isro Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```isro is writing for You ð```")
    await _tweets(text, "isro")
        
@userge.on_cmd("gandhi", about={
    'header': "Custom text Sticker of gandhi",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}gandhi [text | reply to text]"})
async def gandhi(msg: Message):
    """ Fun Sticker of gandhi Tweet """
    replied = msg.reply_to_message
    text = msg.filtered_input_str
    if replied and not text:
        text = replied.text
    if not text:
        await msg.err("```gandhi Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```gandhi is writing for You ð```")
    await _tweets(text, "gandhi")
        
@userge.on_cmd("mia", about={
    'header': "Custom text Sticker of mia",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}mia [text | reply to text]"})
async def miakhalifa(msg: Message):
    """ Fun Sticker of miakhalifa Tweet """
    replied = msg.reply_to_message
    text = msg.filtered_input_str
    if replied and not text:
        text = replied.text
    if not text:
        await msg.err("```miakhalifa Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```miakhalifa is writing for You ð```")
    await _tweets(text, "miakhalifa")
        
@userge.on_cmd("johnny", about={
    'header': "Custom text Sticker of johnny",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}johnny [text | reply to text]"})
async def JohnnnyyySins(msg: Message):
    """ Fun Sticker of johnny Tweet """
    replied = msg.reply_to_message
    text = msg.filtered_input_str
    if replied and not text:
        text = replied.text
    if not text:
        await msg.err("```johnny Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```johnny is writing for You ð```")
    await _tweets(text, "JohnnnyyySins")
        
@userge.on_cmd("krk", about={
    'header': "Custom text Sticker of krk",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}krk [text | reply to text]"})
async def kamaalrkhan(msg: Message):
    """ Fun Sticker of krk Tweet """
    replied = msg.reply_to_message
    text = msg.filtered_input_str
    if replied and not text:
        text = replied.text
    if not text:
        await msg.err("```krk Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```krk is writing for You ð```")
    await _tweets(text, "kamaalrkhan")
        
@userge.on_cmd("vivek", about={
    'header': "Custom text Sticker of vivek",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}vivek [text | reply to text]"})
async def vivekoberoi(msg: Message):
    """ Fun Sticker of vivek Tweet """
    replied = msg.reply_to_message
    text = msg.filtered_input_str
    if replied and not text:
        text = replied.text
    if not text:
        await msg.err("```vivek Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```vivek is writing for You ð```")
    await _tweets(text, "vivekoberoi")
        
@userge.on_cmd("boring", about={
    'header': "Custom text Sticker of boringcompany",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}boring [text | reply to text]"})
async def boringcompany(msg: Message):
    """ Fun Sticker of boringcompany Tweet """
    replied = msg.reply_to_message
    text = msg.filtered_input_str
    if replied and not text:
        text = replied.text
    if not text:
        await msg.err("```boringcompany Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```boringcompany is writing for You ð```")
    await _tweets(text, "boringcompany")
        
@userge.on_cmd("sanjay", about={
    'header': "Custom text Sticker of sanjay",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}sanjay [text | reply to text]"})
async def duttsanjay(msg: Message):
    """ Fun Sticker of sanjay Tweet """
    replied = msg.reply_to_message
    text = msg.filtered_input_str
    if replied and not text:
        text = replied.text
    if not text:
        await msg.err("```sanjay Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```sanjay is writing for You ð```")
    await _tweets(text, "duttsanjay")
        
@userge.on_cmd("ajay", about={
    'header': "Custom text Sticker of ajay",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}ajay [text | reply to text]"})
async def ajaydevgn(msg: Message):
    """ Fun Sticker of ajay Tweet """
    replied = msg.reply_to_message
    text = msg.filtered_input_str
    if replied and not text:
        text = replied.text
    if not text:
        await msg.err("```ajay Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```ajay is writing for You ð```")
    await _tweets(text, "ajaydevgn")
        
@userge.on_cmd("tesla", about={
    'header': "Custom text Sticker of tesla",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}tesla [text | reply to text]"})
async def tesla(msg: Message):
    """ Fun Sticker of tesla Tweet """
    replied = msg.reply_to_message
    text = msg.filtered_input_str
    if replied and not text:
        text = replied.text
    if not text:
        await msg.err("```tesla Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```tesla is writing for You ð```")
    await _tweets(text, "tesla")
        
@userge.on_cmd("albert", about={
    'header': "Custom text Sticker of albert",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}albert [text | reply to text]"})
async def AlbertEinstein(msg: Message):
    """ Fun Sticker of albert Tweet """
    replied = msg.reply_to_message
    text = msg.filtered_input_str
    if replied and not text:
        text = replied.text
    if not text:
        await msg.err("```albert Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```albert is writing for You ð```")
    await _tweets(text, "AlbertEinstein")
        
@userge.on_cmd("bear", about={
    'header': "Custom text Sticker of BearGrylls",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}bear [text | reply to text]"})
async def BearGrylls(msg: Message):
    """ Fun Sticker of BearGrylls Tweet """
    replied = msg.reply_to_message
    text = msg.filtered_input_str
    if replied and not text:
        text = replied.text
    if not text:
        await msg.err("```BearGrylls Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```BearGrylls is writing for You ð```")
    await _tweets(text, "BearGrylls")
        
@userge.on_cmd("rajni", about={
    'header': "Custom text Sticker of rajinikanth",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}rajni [text | reply to text]"})
async def rajinikanth(msg: Message):
    """ Fun Sticker of rajinikanth Tweet """
    replied = msg.reply_to_message
    text = msg.filtered_input_str
    if replied and not text:
        text = replied.text
    if not text:
        await msg.err("```rajinikanth Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```rajinikanth is writing for You ð```")
    await _tweets(text, "rajinikanth")
        
@userge.on_cmd("apple", about={
    'header': "Custom text Sticker of apple",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}apple [text | reply to text]"})
async def apple(msg: Message):
    """ Fun Sticker of apple Tweet """
    replied = msg.reply_to_message
    text = msg.filtered_input_str
    if replied and not text:
        text = replied.text
    if not text:
        await msg.err("```apple Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```apple is writing for You ð```")
    await _tweets(text, "apple")
        
@userge.on_cmd("durov", about={
    'header': "Custom text Sticker of durov",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}durov [text | reply to text]"})
async def durov(msg: Message):
    """ Fun Sticker of durov Tweet """
    replied = msg.reply_to_message
    text = msg.filtered_input_str
    if replied and not text:
        text = replied.text
    if not text:
        await msg.err("```durov Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```durov is writing for You ð```")
    await _tweets(text, "durov")
        
@userge.on_cmd("fb", about={
    'header': "Custom text Sticker of facebook",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}fb [text | reply to text]"})
async def facebook(msg: Message):
    """ Fun Sticker of facebook Tweet """
    replied = msg.reply_to_message
    text = msg.filtered_input_str
    if replied and not text:
        text = replied.text
    if not text:
        await msg.err("```facebook Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```facebook is writing for You ð```")
    await _tweets(text, "facebook")
        
@userge.on_cmd("bjp", about={
    'header': "Custom text Sticker of bjp",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}bjp [text | reply to text]"})
async def bjp4india(msg: Message):
    """ Fun Sticker of bjp Tweet """
    replied = msg.reply_to_message
    text = msg.filtered_input_str
    if replied and not text:
        text = replied.text
    if not text:
        await msg.err("```bjp Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```bjp is writing for You ð```")
    await _tweets(text, "bjp4india")
        
@userge.on_cmd("sambit", about={
    'header': "Custom text Sticker of sambit",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}sambit [text | reply to text]"})
async def sambitswaraj(msg: Message):
    """ Fun Sticker of rajinikanth Tweet """
    replied = msg.reply_to_message
    text = msg.filtered_input_str
    if replied and not text:
        text = replied.text
    if not text:
        await msg.err("```sambit Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```sambit is writing for You ð```")
    await _tweets(text, "sambitswaraj")
        
@userge.on_cmd("nirmala", about={
    'header': "Custom text Sticker of nirmala",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}nirmala [text | reply to text]"})
async def nsitharaman(msg: Message):
    """ Fun Sticker of nirmala Tweet """
    replied = msg.reply_to_message
    text = msg.filtered_input_str
    if replied and not text:
        text = replied.text
    if not text:
        await msg.err("```nirmala Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```nirmala is writing for You ð```")
    await _tweets(text, "nsitharaman")
        
@userge.on_cmd("youtube", about={
    'header': "Custom text Sticker of youtube",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}youtube [text | reply to text]"})
async def youtube(msg: Message):
    """ Fun Sticker of youtube Tweet """
    replied = msg.reply_to_message
    text = msg.filtered_input_str
    if replied and not text:
        text = replied.text
    if not text:
        await msg.err("```youtube Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```youtube is writing for You ð```")
    await _tweets(text, "youtube")
        
@userge.on_cmd("tiktok", about={
    'header': "Custom text Sticker of tiktok",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}tiktok [text | reply to text]"})
async def tiktok_in(msg: Message):
    """ Fun Sticker of tiktok Tweet """
    replied = msg.reply_to_message
    text = msg.filtered_input_str
    if replied and not text:
        text = replied.text
    if not text:
        await msg.err("```tiktok Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```tiktok is writing for You ð```")
    await _tweets(text, "tiktok_in")
        
@userge.on_cmd("google", about={
    'header': "Custom text Sticker of google",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}google [text | reply to text]"})
async def google(msg: Message):
    """ Fun Sticker of google Tweet """
    replied = msg.reply_to_message
    text = msg.filtered_input_str
    if replied and not text:
        text = replied.text
    if not text:
        await msg.err("```google Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```google is writing for You ð```")
    await _tweets(text, "google")
        
@userge.on_cmd("kangana", about={
    'header': "Custom text Sticker of kangana",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}kangana [text | reply to text]"})
async def thekangana(msg: Message):
    """ Fun Sticker of kangana Tweet """
    replied = msg.reply_to_message
    text = msg.filtered_input_str
    if replied and not text:
        text = replied.text
    if not text:
        await msg.err("```kangana Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```kangana is writing for You ð```")
    await _tweets(text, "thekangana")
        
@userge.on_cmd("hrithik", about={
    'header': "Custom text Sticker of hrithik",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}hrithik [text | reply to text]"})
async def ihrithik(msg: Message):
    """ Fun Sticker of hrithik Tweet """
    replied = msg.reply_to_message
    text = msg.filtered_input_str
    if replied and not text:
        text = replied.text
    if not text:
        await msg.err("```hrithik Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```hrithik is writing for You ð```")
    await _tweets(text, "ihrithik")
        
@userge.on_cmd("nirmal", about={
    'header': "Custom text Sticker of nirmalbabaji",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}nirmal [text | reply to text]"})
async def nirmalbabaji(msg: Message):
    """ Fun Sticker of nirmalbabaji Tweet """
    replied = msg.reply_to_message
    text = msg.filtered_input_str
    if replied and not text:
        text = replied.text
    if not text:
        await msg.err("```nirmalbabaji Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```nirmalbabaji is writing for You ð```")
    await _tweets(text, "nirmalbabaji")
        
@userge.on_cmd("ramrahim", about={
    'header': "Custom text Sticker of ram rahim singh",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}ramrahim [text | reply to text]"})
async def gurmeetHoneyS(msg: Message):
    """ Fun Sticker of ram rahim singh Tweet """
    replied = msg.reply_to_message
    text = msg.filtered_input_str
    if replied and not text:
        text = replied.text
    if not text:
        await msg.err("```ram rahim singh Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```ram rahim singh is writing for You ð```")
    await _tweets(text, "gurmeetHoneyS")
        
@userge.on_cmd("cook", about={
    'header': "Custom text Sticker of tim cook",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}cook [text | reply to text]"})
async def tim_cook(msg: Message):
    """ Fun Sticker of tim cook Tweet """
    replied = msg.reply_to_message
    text = msg.filtered_input_str
    if replied and not text:
        text = replied.text
    if not text:
        await msg.err("```tim coom Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```tim cook is writing for You ð```")
    await _tweets(text, "tim_cook")
        
@userge.on_cmd("steve", about={
    'header': "Custom text Sticker of steve jobs",
    'flags': {
        '-s': "To get tweet in Sticker"},
    'usage': "{tr}steve [text | reply to text]"})
async def stevejobsceo(msg: Message):
    """ Fun Sticker of steve Tweet """
    replied = msg.reply_to_message
    text = msg.filtered_input_str
    if replied and not text:
        text = replied.text
    if not text:
        await msg.err("```steve Need some text to Write ð```", del_in=3)
        return
    await msg.edit("```steve is writing for You ð```")
    await _tweets(text, "stevejobsceo")
            
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
    text = msg.filtered_input_str
    if replied and not text:
        text = replied.text
    if not text:
        await msg.err("Give Me some text to Tweet 😕")
        return
    username = ''
    if ',' in text:
        text, username = text.split(',')
    if not username:
        if replied:
            username = replied.from_user.username or replied.from_user.first_name
        else:
            username = msg.from_user.username or msg.from_user.first_name
    await msg.edit("```Creating a Tweet Sticker 😏```")
    await _tweets(msg, text.strip(), username.strip())


def _deEmojify(inputString: str) -> str:
    """Remove emojis and other non-safe characters from string"""
    return re.sub(EMOJI_PATTERN, '', inputString)


async def _tweets(msg: Message, text: str, username: str = '', type_: str = "tweet") -> None:
    api_url = f"https://nekobot.xyz/api/imagegen?type={type_}&text={_deEmojify(text)}"
    if username:
        api_url += f"&username={_deEmojify(username)}"
    res = requests.get(api_url).json()
    tweets_ = res.get("message")
    if not url(tweets_):
        await msg.err("Invalid Syntax, Exiting...")
        return
    tmp_file = Config.DOWN_PATH + "temp.png"
    with open(tmp_file, "wb") as t_f:
        t_f.write(requests.get(tweets_).content)
    img = Image.open(tmp_file)
    img.save(CONVERTED_IMG)
    img.save(CONVERTED_STIKR)
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
    os.remove(tmp_file)
    os.remove(CONVERTED_IMG)
    os.remove(CONVERTED_STIKR)
