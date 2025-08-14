# First, you'll need to install the required library.
# Open your terminal or command prompt and run:
# pip install python-telegram-bot

import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext

# Enable logging to see errors and bot activity
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# The token for your bot, which you get from BotFather
BOT_TOKEN = "7475854737:AAF8gqbsPLEXVwqty05-PLWr-r4FmfdyQok" # IMPORTANT: Replace this with your actual bot token

# The URL you want to send
WEBSITE_URL = "https://friendsacademy.my.canva.site/watch-tutorial"

# This function is called when a user sends the /start command
def start(update: Update, context: CallbackContext) -> None:
    """Sends a message with a button that links to your website."""
    
    # Create a button that opens the URL
    keyboard = [
        [InlineKeyboardButton("Watch Tutorial", url=WEBSITE_URL)]
    ]
    
    # Create the InlineKeyboardMarkup object
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # The message to send back to the user
    message = "Welcome! Click the button below to watch the tutorial."
    
    # Send the message with the button
    update.message.reply_text(message, reply_markup=reply_markup)

def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(BOT_TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register the command handler for the /start command
    dispatcher.add_handler(CommandHandler("start", start))

    # Start the Bot
    print("Bot is running...")
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
