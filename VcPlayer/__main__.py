import requests
from pyrogram import Client as Bot

from VcPlayer.config import API_HASH, API_ID, BG_IMAGE, BOT_TOKEN
from VcPlayer.services.callsmusic import run

response = requests.get(BG_IMAGE)
file = open("VcPlayer/20211130_223431.jpg", "wb")
file.write(response.content)
file.close()

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="VcPlayer.modules"),
)

bot.start()
run()
