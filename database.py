import telebot
import sqlite3
import threading

bot = telebot.TeleBot('6420099805:AAFRb0zXxNU7X4T2HjmbU3_MNB6RAGbkMxY')


conn = sqlite3.connect('bot.db', check_same_thread=False)
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                    description TEXT)''')
conn.commit()


db_lock = threading.Lock()


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f"Привет {message.from_user.first_name}")


@bot.message_handler(commands=['add'])
def add_task(message):
    description = message.text[3:]
    if description:
        with db_lock:
            cursor.execute("INSERT INTO tasks (description) VALUES (?)", (description,))
            conn.commit()
        bot.reply_to(message, "Задача успешно добавлена!")
    else:
        bot.reply_to(message, "Пожалуйста, введите описание задачи.")


@bot.message_handler(commands=['удалить'])
def remove_task(message):
    task_id = message.text[8:]
    if task_id:
        if not task_id.isdigit():
            bot.reply_to(message, "Пожалуйста, введите корректный номер задачи для удаления.")
            return
        with db_lock:
            cursor.execute("SELECT * FROM tasks WHERE id=?", (task_id,))
            task = cursor.fetchone()
            if task:
                cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
                conn.commit()
                bot.reply_to(message, "Задача успешно удалена!")
            else:
                bot.reply_to(message, "Задача с указанным номером не найдена.")
    else:
        bot.reply_to(message, "Пожалуйста, введите номер задачи для удаления.")


@bot.message_handler(commands=['список'])
def get_task_list(message):
    with db_lock:
        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()
    if tasks:
        task_list = ""
        for t in tasks:
            task_list += f"{t[0]}. {t[1]}\n"
        bot.reply_to(message, task_list)
    else:
        bot.reply_to(message, "Список задач пуст.")


bot.infinity_polling()