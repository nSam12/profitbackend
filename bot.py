import telebot
from telebot import types


token='5623499060:AAHyNVRlwBD5MQ3ld6vuyoniI800qfPvq4k'

bot = telebot.TeleBot(token);

@bot.message_handler(content_types='text')
def message_reply(message):
    bot.send_message(message.from_user.id, "Твой код: 2387")


bot.infinity_polling()