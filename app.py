import telebot

from config import BOT_TOKEN, currencies
from exceptions import APIException
from convertor import Convert
from messages import Message


bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start', 'help', ])
def handler_start_help(message):
    bot.send_message(message.chat.id, Message.help)


@bot.message_handler(commands=['values', ])
def handler_values(message):
    currencies_text = Message.values
    list_keys = list(currencies.keys())
    for keys in list_keys:
        currencies_text += f'{keys}\n'
    bot.send_message(message.chat.id, currencies_text)


@bot.message_handler(content_types=['text', ])
def handler_text(message):
    to, from_, amount = message.text.lower().split()
    try:
        converted = Convert.get_price(to, from_, amount)
        bot.send_message(message.chat.id, converted)
    except APIException as error:
        bot.send_message(message.chat.id, str(error))


if __name__ == '__main__':
    bot.polling(none_stop=True)
