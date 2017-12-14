import config
import telebot
import time

import search

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'], content_types=['text'])
def greeting_message(message):
    bot.send_message(message.chat.id, 'AMRU бот приветствует тебя!\nДля вывода инструкций набери /help')

@bot.message_handler(commands=['help'], content_types=['text'])
def help_info(help):
    bot.send_message(help.chat.id, 'Шаблон: Регион Марка Модель Кузов')
    bot.send_message(help.chat.id, 'Пример: Санкт-Петербург Renault Logan Седан')

@bot.message_handler(content_types=['text'])
def search_query(query):
    try:
        adverts = search.search_advert(query.text)
        for item in range(len(adverts)):
            bot.send_message(query.chat.id, adverts[item])
            time.sleep(1)
    except:
        bot.send_message(query.chat.id, 'К сожалению, объявлений по вашему запросу не нашлось.')

if __name__ == '__main__':
     bot.polling(none_stop=True)