import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Përshëndetje! Unë jam Avokati AI ⚖️\n"
        "Më bëj një pyetje rreth ligjeve shqiptare."
    )


async def answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    await update.message.reply_text(
        f"Pyetja jote u mor:\n\n{text}\n\n"
        "Jam duke u zhvilluar. Baza e ligjeve do të shtohet së shpejti."
    )


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, answer)
)

print("Avokati AI u nis!")

app.run_polling()