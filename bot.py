# First, you'll need to install the required library.
# Open your terminal or command prompt and run:
# pip install python-telegram-bot

import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes
from flask import Flask
import threading



# --- FLASK APP FOR RENDER HEALTH CHECK ---
app = Flask(__name__)

@app.route("/")
def home():
    return "Quiz Bot is running!"

# Function to start Flask in a separate thread
def start_flask():
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)


# Enable logging to see errors and bot activity
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# The token for your bot, which you get from BotFather
BOT_TOKEN = "7475854737:AAF8gqbsPLEXVwqty05-PLWr-r4FmfdyQok"

# The URL you want to send
WEBSITE_URL = "https://friendsacademy.my.canva.site/watch-tutorial"

# This function is called when a user sends the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
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
    await update.message.reply_text(message, reply_markup=reply_markup)

def main() -> None:
    """Start the bot."""

    """Start Flask in a thread and the bot using polling."""
    # Start Flask server in a background thread
    threading.Thread(target=start_flask, daemon=True).start()

    # Create the Application and pass it your bot's token.
    application = Application.builder().token(BOT_TOKEN).build()

    # Register the command handler for the /start command
    application.add_handler(CommandHandler("start", start))

    # Start the Bot by polling for updates
    print("Bot is running...")
    application.run_polling()

if __name__ == '__main__':
    main()
