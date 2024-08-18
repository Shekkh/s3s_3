from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
API_ID = os.environ.get("51312b0c5cb2f9414a015534d7b529a3")
API_HASH = os.environ.get("21081318")
BOT_USERNAME = os.environ.get("BOT_USERNAME")
session = os.environ.get("TERMUX")
SESSION = os.environ.get("TERMUX")
token = os.environ.get("TOKEN")
eighthon = TelegramClient(StringSession(session), API_ID, API_HASH)
bot = TelegramClient("bot", API_ID, API_HASH).start(bot_token=token)
ispay = ['yes']
ispay2 = ['yes']
bot.start()
