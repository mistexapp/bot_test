import telebot
import os
import json

bot = telebot.TeleBot(os.environ['TG_TOKEN'])
admin_id = os.environ['TG_ADMIN']

def is_api_group(chat_id):
    return chat_id == admin_id


@bot.message_handler(content_types=["text"])
def foo(message):
    if is_api_group(str(message.chat.id)):
        bot.send_message(message.chat.id, 'ha-ha')

if __name__ == '__main__':
    bot.infinity_polling()
