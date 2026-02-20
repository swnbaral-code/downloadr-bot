import os
import yt_dlp
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = os.getenv(8547077194:AAGp53o356G1sFAg1-levnSnAviaANbXTFk)

async def download_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text
    await update.message.reply_text("Downloading... ⏳")

    ydl_opts = {
        'format': 'best',
        'outtmpl': 'downloaded.%(ext)s'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)

    await update.message.reply_document(document=open(filename, 'rb'))
    os.remove(filename)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, download_handler))
app.run_polling()
