import config
import telebot

import users

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'], content_types=['text'])
def greeting_message(message):
    bot.send_message(message.chat.id, 'Отправка юзеров в Youla!\nДля вывода инструкций набери /help')

@bot.message_handler(commands=['help'], content_types=['text'])
def help_info(help):
    bot.send_message(help.chat.id, 'Шаблон: ID Username Email Phone')
    bot.send_message(help.chat.id, 'Пример: 2027246 Ашот test1@lackmail.ru 79006473639')

@bot.message_handler(content_types=['text'])
def search_query(query):
    try:
        response = users.users_data(query.text)
        bot.send_message(query.chat.id, response)
    except:
        bot.send_message(query.chat.id, 'Что-то пошло не так!')

if __name__ == '__main__':
     bot.polling(none_stop=True)