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

    if message.text:
        chat_message = f"{message.from_user.username}: {message.text}"
        bot.send_message(log_group_id, chat_message)
    
    elif message.photo:
        # Handle photo
        photo = message.photo[-1]  # Get the highest quality photo
        file_id = photo.file_id
        file_info = bot.get_file(file_id)
        file_path = file_info.file_path
        photo_url = f"https://api.telegram.org/file/bot{bot_token}/{file_path}"
        photo_caption = f"{message.from_user.username} sent a photo"
        bot.send_photo(log_group_id, photo_url, caption=photo_caption)
    
    elif message.video:
        # Handle video
        video = message.video
        file_id = video.file_id
        file_info = bot.get_file(file_id)
        file_path = file_info.file_path
        video_url = f"https://api.telegram.org/file/bot{bot_token}/{file_path}"
        video_caption = f"{message.from_user.username} sent a video"
        bot.send_video(log_group_id, video_url, caption=video_caption)
    
    elif message.sticker:
        # Handle sticker
        sticker = message.sticker
        file_id = sticker.file_id
        file_info = bot.get_file(file_id)
        file_path = file_info.file_path
        sticker_url = f"https://api.telegram.org/file/bot{bot_token}/{file_path}"
        sticker_caption = f"{message.from_user.username} sent a sticker"
        bot.send_sticker(log_group_id, sticker_url, caption=sticker_caption)
    
    elif message.animation:
        # Handle GIF
        animation = message.animation
        file_id = animation.file_id
        file_info = bot.get_file(file_id)
        file_path = file_info.file_path
        animation_url = f"https://api.telegram.org/file/bot{bot_token}/{file_path}"
        animation_caption = f"{message.from_user.username} sent a GIF"
        bot.send_animation(log_group_id, animation_url, caption=animation_caption)
    
    elif message.audio:
        # Handle audio
        audio = message.audio
        file_id = audio.file_id
        file_info = bot.get_file(file_id)
        file_path = file_info.file_path
        audio_url = f"https://api.telegram.org/file/bot{bot_token}/{file_path}"
        audio_caption = f"{message.from_user.username} sent an audio file"
        bot.send_audio(log_group_id, audio_url, caption=audio_caption)

# Start the bot
bot.polling()
