import telebot

# Replace 'TOKEN' with your bot token
bot_token = '5611176803:AAHL17RUNLA_CgBSXpfifxProLl66AzXNIk'

# Replace 'GROUP_ID' with the ID of the group where the bot will save the chats
log_group_id = '-1001832126466'

# Create a TeleBot instance
bot = telebot.TeleBot(bot_token)

# Register a message handler for all incoming messages in any group
@bot.message_handler(func=lambda message: True)
def save_chat(message):
    chat_id = message.chat.id
    chat_message = f"{message.from_user.username}: {message.text}"

    # Send the formatted chat message to the log group
    bot.send_message(log_group_id, chat_message)

# Start the bot
bot.polling()
