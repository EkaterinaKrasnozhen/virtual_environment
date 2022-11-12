import telebot
from telebot import types
import datetime
import time
     
        
bot = telebot.TeleBot('5483567139:AAFOLwOJcEr_oN7xhAz82MybfR-w4RIJ--A')

keyboard1 = telebot.types.ReplyKeyboardMarkup(True,True)
keyboard1.row('Купить USD за RUB', 'Продать USD за RUB')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, """Привет, нажми нужную кнопку.
                     \n Для выхода в главное меню - нажми \n/start""", reply_markup=keyboard1)


@bot.message_handler(commands=['u'])
def get_us(message):
    msg = bot.send_message(message.chat.id, 'Привет, какой сегодня курс USD/RUB?')
    bot.register_next_step_handler(msg, log_course_us)
    

@bot.message_handler(commands=['r'])
def get_rub(message):
    msg1 = bot.send_message(message.chat.id, 'Привет, какой сегодня курс RUB/USD?')
    bot.register_next_step_handler(msg1, log_course_rub)
    

def log_course_us(message):
    course_us_rub = {}
    to_day = f'{datetime.datetime.now():%d/%m/%y %H.%M.%S}'
    course_us_rub[to_day] = {message.text}
    with open('cours_us.cvs', 'a', encoding='utf-8') as c:
        c.write(f'{course_us_rub}\n')
    with open('cours_today_us.cvs', 'w', encoding='utf-8') as c:
        c.write(f'{course_us_rub}\n')
        
        
def log_course_rub(message):
    course_rub_us = {}
    to_day = f'{datetime.datetime.now():%d/%m/%y %H.%M.%S}'
    course_rub_us[to_day] = {message.text}
    with open('cours_rub.cvs', 'a', encoding='utf-8') as c:
        c.write(f'{course_rub_us}\n')
    with open('cours_today_rub.cvs', 'w', encoding='utf-8') as c:
        c.write(f'{course_rub_us}\n')
        

def get_course_today_us():
    dict1 = dict()
    data = open('cours_today_us.cvs', 'r', encoding='utf-8')
    file = data.read().replace("{","").replace("}","").replace("'","").split("\n")[:-1]
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
    file = data.read().replace("{","").replace("}","").replace("'","").split("\n")[:-1]
    data.close
    for item in file:
        key = item.split(':')[0]
        value = item.split(':')[1]
        dict1[key] = value
        data.close()
        return value


@bot.message_handler(content_types=['text'])
def message_reply(message):
    if message.text == 'Купить USD за RUB':
        bot.send_message(message.chat.id, f'курс сегодня = {get_course_today_us()}')
        return
    if message.text == 'Продать USD за RUB':
        bot.send_message(message.chat.id, f'курс сегодня = {get_course_today_rub()}')
        return
    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю, нажми /start и выбери нужную кнопку меню.')
 

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Приветик')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    elif message.text.lower() == 'спасибо':
        bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')


@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)


bot.polling(none_stop=True, interval=0)

