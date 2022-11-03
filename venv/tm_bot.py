from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def hello(update:Update, contex: CallbackContext) -> None:
    update.message.reply_text(f'Привет, хотите выгодно обменять валюту?{update.effective_user.first_name}')
    
updater = Updater('5612465487:AAEOLElRIYrar9GXEeEgp5zDk1huUNPb0Bw')
updater.dispatcher.add_handler(CommandHandler('Hello', hello))
updater.start_polling()
updater.idle()