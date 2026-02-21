import os
import yt_dlp
from telegram.ext import Updater, MessageHandler, Filters

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN not set!")

def download(update, context):
    url = update.message.text
    update.message.reply_text("Downloading... ⏳")

    ydl_opts = {
        'format': 'best',
        'outtmpl': 'downloaded.%(ext)s'
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)

        update.message.reply_document(open(filename, 'rb'))
        os.remove(filename)

    except Exception as e:
        update.message.reply_text(f"Error: {e}")

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, download))

print("Bot started successfully...")
updater.start_polling()
updater.idle()
