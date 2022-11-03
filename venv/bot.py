import telebot
bot = telebot.TeleBot('5483567139:AAFOLwOJcEr_oN7xhAz82MybfR-w4RIJ--A')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Привет':
        bot.send_message(message.from_user.id,'Привет, чем я могу помочь?')
    elif message.text == '/help':
        bot.send_message(message.from_user.id, 'Напиши привет')
    else:
        bot.send_message(message.from_user.id, 'Я тебя не понимаю')
        
bot.polling(none_stop=True, interval=0)