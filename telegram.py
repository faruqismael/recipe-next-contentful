from telegram import Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackContext,
)

# Your bot token from BotFather
BOT_TOKEN = "6644040086:AAHcdt7CZVVekYZCNSzTzCl2Ra5Wv3MNim4"

# Dictionary to store channel IDs you want to repost messages from
CHANNELS = {
    "channel1": "@javascript_Programming",
    "channel2": "@LSSYAOfficial",
    # Add more channels if needed
}


# Function to handle the /start command
def start(update: Update, _: CallbackContext) -> None:
    update.message.reply_text(
        "Bot started! Use /repost to repost messages from channels."
    )


# Function to handle the /repost command
def repost(update: Update, _: CallbackContext) -> None:
    for channel_name, channel_username in CHANNELS.items():
        messages = bot.get_chat_history(
            chat_id=channel_username, limit=10
        )  # Get last 10 messages from the channel
        for message in messages:
            # Repost messages to your channel
            update.message.reply_text(f"Reposted from {channel_name}: {message.text}")


def main() -> None:
    updater = Updater(BOT_TOKEN)

    # Register command handlers
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CommandHandler("repost", repost))

    # Start the Bot
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
