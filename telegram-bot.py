import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

WELCOME_MESSAGE = (
    "👋 Welcome to the BuggyCoin Community!\n\n"
    "🐞 We're thrilled to have you join the Buggy Army!\n\n"
    "🚀 Please make sure to read the pinned rules to keep the chat friendly and fun.\n\n"
    "👉 Follow our official announcements channel: @BuggyCoinOfficial\n"
    "💬 Introduce yourself and let’s make crypto fun together!\n\n"
    "Fun. Fast. Buggy."
)

async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for member in update.message.new_chat_members:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=WELCOME_MESSAGE)

def main():
    TOKEN = os.environ["TOKEN"]

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))

    app.run_polling()

if __name__ == '__main__':
    main()
