import telebot
bot = telebot.TeleBot('5483567139:AAFOLwOJcEr_oN7xhAz82MybfR-w4RIJ--A')
# @bot.message_handler(content_types=['text'])
# def get_text_messages(message):
#     if message.text == '/start':
#        bot.send_message(message.from_user.id,'Привет, хотите совершить выгодный обмен?\n 1 - Купить usd за rub\n 2 - Продать usd за rub')
#        bot.register_next_step_handler(message, get_course_usd)

course_usd_rub = 0
course_rub_usd = 0

@bot.message_handler(content_types=['text'])
def get_course_usd(message):
    if message.text == '/u':
        bot.send_message(message.from_user.id,'Какой сегодня курс обмена usd на rub?')
        bot.register_next_step_handler(message,multi_course)


def multi_course(message):
    course_usd_rub = message.text
    bot.send_message(message.from_user.id, 10000 * int(course_usd_rub))


def set_course_usd(message):
    course_usd_rub = message.text
    return course_usd_rub
        
def get_course_rub(message):
    if message.text == 'r':
        bot.send_message('Какой сегодня курс покупки usd за rub?')
        bot.register_next_step_handler(message,set_course_rub)
        
def set_course_rub(message):
    course_rub_usd = message.text
    return course_rub_usd

bot.polling(none_stop=True, interval=0)

