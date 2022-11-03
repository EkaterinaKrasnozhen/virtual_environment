import telebot

bot = telebot.TeleBot("5612465487:AAEOLElRIYrar9GXEeEgp5zDk1huUNPb0Bw")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Привет, хотите совершить выгодный обмен?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message,'1 хочу продать usd за рубли\n 2 хочу купить usd за рубли')
    if message == '1':
        bot.reply_to('курс на сегодня 1 usd = 60 rub')


bot.infinity_polling()