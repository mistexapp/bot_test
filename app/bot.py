import telebot

bot = telebot.TeleBot('5054086490:AAHHt6-CCOCfV2O_QLQqlrRG9-qwBGsde2Y')
chat_id_c = '360873310'

def is_api_group(chat_id):
    return chat_id_c == chat_id


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли
    if is_api_group(str(message.chat.id)):
        bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
    bot.infinity_polling()