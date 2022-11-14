import telebot
import datetime
import os
from dotenv import load_dotenv # pip install python-dotenv - безопасно ипсользовать свои пароли и токены
load_dotenv()
token = os.getenv('token_tg')

#спрятать токен
bot = telebot.TeleBot(f'{token}')


#создаем кнопки
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Купить USD за RUB', 'Продать USD за RUB')

# /start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, """Привет, нажми нужную кнопку.
                     \n Вернуться в меню - нажми /start""", reply_markup=keyboard1)    
    
    
#скрытая от клиента команда, чтобы задать курс
@bot.message_handler(commands=['r', 'R'])
def get_rub_1(message):
    msg1 = bot.send_message(message.chat.id, 'Привет, какой сегодня курс продажи USD за RUB?')
    id_1 = 1
    bot.register_next_step_handler(msg1, log_course, id_1)


#скрытая от клиента команда, чтобы задать курс 
@bot.message_handler(commands=['u', 'U'])
def get_us_1(message):
    msg = bot.send_message(message.chat.id, 'Привет, какой сегодня курс покупки USD за RUB?')
    id_2 = 2
    bot.register_next_step_handler(msg, log_course, id_2)
  
    
#лог значений курса, 1 файл хранит все установленные ранее курсы, 2 - только последний
def log_course(message, num):
    course = {}
    to_day = f'{datetime.datetime.now():%d/%m/%y %H.%M.%S}'
    err = message.text.replace(",", "").replace(".", "")
    course[to_day] = message.text.replace(",", ".")
    if not err.isnumeric():
        bot.send_message(message.chat.id,'Нужно ввести число!')
        bot.register_next_step_handler(message, log_course, num)
    else:
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


def get_course_today_rub():
    data = open('cours_today_rub.cvs', 'r', encoding='utf-8')
    file = data.read().replace("{", "").replace(
        "}", "").replace("'", "").replace(",", ".").split("\n")[:-1]
    data.close()
    for item in file:
        value = item.split(':')[1]
        data.close()
        return value


#получаем актуальный курс для пользователя
def get_course_today_us():
    data = open('cours_today_us.cvs', 'r', encoding='utf-8')
    file = data.read().replace("{", "").replace(
        "}", "").replace("'", "").replace(",", ".").split("\n")[:-1]
    data.close()
    for item in file:
        value = item.split(':')[1]
        data.close()
        return value


@bot.message_handler(commands=['/calc'])
def get_sum_us(message, id_num):
    msg = bot.send_message(message.chat.id, 'Какая сумма?')
    bot.register_next_step_handler(msg, calc, id_num)
        
    
#выводим курс на экран, в зависимости от usd или rub
@bot.message_handler(content_types=['text'])
def message_reply(message):
    if message.text == 'Купить USD за RUB':
        bot.send_message(message.chat.id, f'Курс сегодня = {get_course_today_us()}')
        msg = bot.send_message(message.chat.id, f'Могу посчитать на калькуляторе, \n нажми /calc')
        id_u = 1
        bot.register_next_step_handler(msg, get_sum_us, id_u)
        return
    if message.text == 'Продать USD за RUB':
        bot.send_message(message.chat.id, f'Курс сегодня = {get_course_today_rub()}')
        msg1 = bot.send_message(message.chat.id, f'Могу посчитать на калькуляторе, \n нажми /calc')
        id_r = 2
        bot.register_next_step_handler(msg1, get_sum_us, id_r)
        return
     
    elif message.text != '/calc':
        bot.send_message(message.chat.id, """Я тебя не понимаю, 
                         \n нажми /start и выбери нужную кнопку меню.""")


@bot.message_handler(content_types=['text'])    
def calc(message, id_n):
    sum = message.text
    if not sum.isdigit():
        bot.send_message(message.chat.id,'Нужно ввести число!')
        bot.register_next_step_handler(message, calc, id_n)    
    else:    
        if id_n == 1:
            course1 = get_course_today_us()
            
            res = float(sum) * float(course1)
            bot.send_message(message.chat.id, f'Купить {sum} USD по {course1} = {res} RUB')
        if id_n == 2:
            course2 = get_course_today_rub()
            res = int(sum) * float(course2)
            bot.send_message(message.chat.id, f'Продать {sum} USD по {course2} = {res} RUB')
        


bot.polling(none_stop=True, interval=0)
