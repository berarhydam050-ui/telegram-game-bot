import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Replace 'YOUR_BOT_TOKEN_HERE' with the HTTP API Token you got from BotFather,
# or set it up using environment variables.
TOKEN = "8817231774:AAEtWWCrogFCMV7LO6vAmjy0bY2A0JS0Ogs"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    await update.message.reply_text(
        f"Hello {user_name}! 👋 Welcome to your new Telegram bot. How can I help you today?"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send /start to begin interacting with the bot.")

def main():
    # Build the application with your token
    application = ApplicationBuilder().token(TOKEN).build()

    # Register command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # Start the Bot
    print("Bot is up and running...")
    application.run_polling()

if __name__ == '__main__':
    main()
  
