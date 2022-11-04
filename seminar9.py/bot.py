import telebot
bot = telebot.TeleBot('5483567139:AAFOLwOJcEr_oN7xhAz82MybfR-w4RIJ--A')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '/start':
       bot.send_message(message.from_user.id,'Привет, хотите совершить выгодный обмен?\n 1 - Купить usd за rub\n 2 - Продать usd за rub')
       



        
bot.polling(none_stop=True, interval=0)