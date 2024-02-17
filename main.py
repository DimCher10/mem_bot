import telebot
from telebot import apihelper, types
import os 
from db import save_photo

apihelper.ENABLE_MIDDLEWARE = True

bot = telebot.TeleBot("6654387910:AAGc5P45RbZ76PtYR6yVAIJ2t5v9XIDPdrw")

command1 = types.BotCommand(command='memes', description='😜 Получить мемы')
command2 = types.BotCommand(command='info', description='Информация о боте')

bot.set_my_commands([command1, command2])


@bot.middleware_handler(update_types=['message'])
def modify_message(bot_instance, message):
    user_id = message.from_user.id
    print("User ID:", user_id)

    if hasattr(message, 'text') and message.text:
        message.text += f' (Ваш ID: {user_id})'

@bot.message_handler(commands = ['memes'])
def memes_send(message):
    user_id = message.from_user.id
    

@bot.message_handler(content_types=['photo'])
def handle_photos(message):
    file_id = message.photo[-1].file_id
    file_info = bot.get_file(file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    filename = save_photo(file_id)
    with open(os.path.join("images", f"{filename}.jpg"), "wb") as f:
        f.write(downloaded_file)





@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_id = message.from_user.id
    bot.reply_to(message, message.text)


bot.infinity_polling()