import telebot
import datetime

import os
from dotenv import load_dotenv # pip install python-dotenv - безопасно ипсользовать свои пароли и токены
load_dotenv()
token = os.getenv('token_tg')

#спрятать коин
bot = telebot.TeleBot(f'{token}')


#создаем кнопки
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Купить USD за RUB', 'Продать USD за RUB')

# /start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, """Привет, нажми нужную кнопку.
                     \n Для выхода в главное меню - нажми 
                     \n/start""", reply_markup=keyboard1)


#скрытая от клиента команда, чтобы задать курс
@bot.message_handler(commands=['r'])
def get_rub_1(message):
    msg1 = bot.send_message(message.chat.id, """Привет, какой 
                            сегодня курс продажи USD за RUB?""")
    id_1 = 1
    bot.register_next_step_handler(msg1, log_course, id_1)


#скрытая от клиента команда, чтобы задать курс
@bot.message_handler(commands=['u'])
def get_us_1(message):
    msg = bot.send_message(message.chat.id, 'Привет, какой сегодня курс покупки USD за RUB?')
    id_2 = 2
    bot.register_next_step_handler(msg, log_course, id_2)


#лог значений курса, 1 файл хранит все установленные ранее курсы, 2 - только последний
def log_course(message, num):
    course = {}
    to_day = f'{datetime.datetime.now():%d/%m/%y %H.%M.%S}'
    course[to_day] = {message.text}
    if num == 2:
        with open('cours_us.cvs', 'a', encoding='utf-8') as c:
            c.write(f'{course}\n')
        with open('cours_today_us.cvs', 'w', encoding='utf-8') as c:
            c.write(f'{course}\n')
    elif num == 1:
        with open('cours_rub.cvs', 'a', encoding='utf-8') as c:
            c.write(f'{course}\n')
        with open('cours_today_rub.cvs', 'w', encoding='utf-8') as c:
            c.write(f'{course}\n')


#получаем актуальный курс для пользователя
def get_course_today_us():
    dict1 = dict()
    data = open('cours_today_us.cvs', 'r', encoding='utf-8')
    file = data.read().replace("{", "").replace(
        "}", "").replace("'", "").split("\n")[:-1]
    data.close
    for item in file:
        key = item.split(':')[0]
        value = item.split(':')[1]
        dict1[key] = value
        data.close()
        return value


def get_course_today_rub():
    dict1 = dict()
    data = open('cours_today_rub.cvs', 'r', encoding='utf-8')
    file = data.read().replace("{", "").replace(
        "}", "").replace("'", "").split("\n")[:-1]
    data.close
    for item in file:
        key = item.split(':')[0]
        value = item.split(':')[1]
        dict1[key] = value
        data.close()
        return value


#выводим курс на экран, в зависимости от usd или rub
@bot.message_handler(content_types=['text'])
def message_reply(message):
    if message.text == 'Купить USD за RUB':
        bot.send_message(message.chat.id, f'курс сегодня = {get_course_today_us()}')
        return
    if message.text == 'Продать USD за RUB':
        bot.send_message(message.chat.id, f'курс сегодня = {get_course_today_rub()}')
        return
    else:
        bot.send_message(message.chat.id, """Я тебя не понимаю, 
                         нажми /start и выбери нужную кнопку меню.""")


bot.polling(none_stop=True, interval=0)
