import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

bot = telebot.TeleBot('6420099805:AAFRb0zXxNU7X4T2HjmbU3_MNB6RAGbkMxY')


def buttons():
     kb =ReplyKeyboardMarkup(resize_keyboard=True)




@bot.message_handler(commands=['/start'])
def message_echo(message):
     bot.send_message(message.chat.id, 'Привет я эхо бот ')  
     con = con.connect()



