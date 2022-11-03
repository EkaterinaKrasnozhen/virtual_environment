from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def hello(update: Update, contex: CallbackContext) -> None:
    update.message.reply_text(f'Привет, хотите выгодно обменять валюту?{update.effective_user.first_name}')
    
updater = Updater('5717266163:AAHZrdJfDETJCYjuvMg8F79q9TSK6ihcVK4')
updater.dispatcher.add_handler(CommandHandler('Hello', hello))
updater.start_polling()
updater.idle()