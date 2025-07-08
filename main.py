import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Setze hier deinen echten Bot-Token ein
TOKEN = os.getenv("BOT_TOKEN")

# Aktiviere Logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# /start Kommando
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to the Ultimate Kaito Bot! Type /rank [project] to get started.")

# /rank Kommando
async def rank(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Please provide a project name. Example: /rank OpenLedger")
        return
    project = " ".join(context.args)
    user = update.effective_user.username or update.effective_user.first_name
    await update.message.reply_text(f"@{user}, your current rank for {project} is: 🥷 #238 (placeholder)")

# Hauptfunktion
def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("rank", rank))
    app.run_polling()

if __name__ == '__main__':
    main()