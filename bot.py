from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

# 🔑 Bot token (BotFather dan olasan)
TOKEN = ""

# 💬 Javob matni
REPLY_TEXT = "Assalomu alaykum 👋 bu Shohjahonning avto javob bot 😉"

# 📩 Har qanday text kelganda ishlaydi
async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        await update.message.reply_text(REPLY_TEXT)

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # Hamma text xabarlarga javob
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))

    print("🤖 Bot ishga tushdi...")

    app.run_polling()

if __name__ == "__main__":
    main()