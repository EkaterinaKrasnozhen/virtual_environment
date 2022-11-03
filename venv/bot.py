import telebot
bot = telebot.TeleBot('5483567139:AAFOLwOJcEr_oN7xhAz82MybfR-w4RIJ--A')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '/start':
       bot.send_message(message.from_user.id,'Привет, хотите совершить выгодный обмен?\n 1 - Купить usd за rub\n 2 - Продать usd за rub')
       get_new_mes(message)

def get_new_mes(mes):
    if mes.text == '1':
           bot.send_message(mes.from_user.id,'Курс на сегодняшний день 1 USD = 62 RUB')
    elif mes.text == '2':
          bot.send_message(mes.from_user.id, 'Курс на сегодняшний день 1 USD = 60 RUB')
    else:
           bot.send_message(mes.from_user.id, 'Я тебя не понимаю')
        
bot.polling(none_stop=True, interval=0)