
import telebot
bot = telebot.TeleBot('6420099805:AAFRb0zXxNU7X4T2HjmbU3_MNB6RAGbkMxY')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "salom mening botimga xush kelibsiz!")



@bot.message_handler(content_types=['text'])
def repeat_all_message(message):
    bot.send_message(message.chat.id,message.text)

if __name__ == '__main__':
    bot.infinity_polling()