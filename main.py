import logging
import telebot

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Telegram Bot Token
TOKEN = '5611176803:AAHL17RUNLA_CgBSXpfifxProLl66AzXNIk'

# Private group ID to forward messages
PRIVATE_GROUP_ID = '-1001832126466'  # Replace with the actual private group ID

# Create bot instance
bot = telebot.TeleBot(TOKEN)

# Handler to forward messages to private group
@bot.message_handler(func=lambda message: True)
def forward_message(message):
    # Forward message to private group
    bot.forward_message(chat_id=PRIVATE_GROUP_ID,
                        from_chat_id=message.chat.id,
                        message_id=message.message_id)

# Handler for /start command
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello! I will forward all messages to the private group.')

# Handler for unknown commands
@bot.message_handler(func=lambda message: True)
def unknown(message):
    bot.reply_to(message, "Sorry, I didn't understand that command.")

# Start the Bot
bot.polling()
