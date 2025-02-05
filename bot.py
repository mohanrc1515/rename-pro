from pyrogram import Client
import os

TOKEN = os.environ.get("TOKEN", "7696984863:AAEiUA76NTYiQ2dYlCzxEAaymT_FMnnkKpM")

APP_ID = int(os.environ.get("APP_ID", "12655645"))

API_HASH = os.environ.get("API_HASH", "05c4cafe00b81ed83207bb4365e0053b")

if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    app = Client(
        "renamer",
        bot_token=TOKEN,
        api_id=APP_ID,
        api_hash=API_HASH,
        plugins=plugins
    )
    app.run()
