

from telebot import TeleBot, types
from random import randint
from dotenv import load_dotenv
import os

load_dotenv()
bot = TeleBot(os.getenv('TOKEN'))


@bot.message_handler(commands=['start'])
def send_welcome(message):

    markup = types.InlineKeyboardMarkup()
    btn_my_site = types.InlineKeyboardButton(text='💻РЕГИСТРАЦИЯ', url='https://www.google.com')
    btn_my_dalee = types.InlineKeyboardButton(text='ДАЛЕЕ>>', callback_data='register')
    markup.add(btn_my_site)
    markup.add(btn_my_dalee)

    bot.send_photo(message.chat.id, open('mines.png', 'rb'))
    bot.send_message(message.chat.id, '📲Для начала необходимо провести регистрацию на 1win (провайдер игры Mines). Чтобы бот успешно проверил регистрацию, нужно соблюсти важные условия:\n\n1️⃣Аккаунт обязательно должен быть НОВЫМ! Если у вас уже есть аккаунт и при нажатии на кнопку «РЕГИСТРАЦИЯ» вы попадаете на старый, необходимо выйти с него и заново нажать на кнопку «РЕГИСТРАЦИЯ», после чего по новой зарегистрироваться! \n❗️Иначе бот может давать не верные сигналы!\n\n2️⃣Чтобы бот смог проверить вашу регистрацию, обязательно нужно ввести промокод BIBKA500 при регистрации! \n❗️Иначе бот может давать не верные сигналы!\n\nПосле РЕГИСТРАЦИИ нажимайте "ДАЛЕЕ>>"✅', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'register')
def callback_register(call):
    # Код для отправки нового сообщения с кнопкой
    markup = types.InlineKeyboardMarkup()
    btn_my_site = types.InlineKeyboardButton(text='🟩ПОЛУЧИТЬ СИГНАЛ', callback_data='signalo')
    markup.add(btn_my_site)

    bot.send_message(call.message.chat.id, '💫Теперь вы можете получать сигналы! Но если вы не зарегистрировались по ссылке, то сигналы будут не верны❗️ ', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'signalo')
def callback_signalo(call):
    a = randint(0, 9)
    markup = types.InlineKeyboardMarkup()
    btn_my_site = types.InlineKeyboardButton(text='🟩ПОЛУЧИТЬ СИГНАЛ', callback_data='signalo')
    markup.add(btn_my_site)
    if a == 0:
        bot.send_photo(call.message.chat.id, open('1s.jpg', 'rb'))
    if a == 1:
        bot.send_photo(call.message.chat.id, open('2s.jpg', 'rb'))
    if a == 2:
        bot.send_photo(call.message.chat.id, open('3s.jpg', 'rb'))
    if a == 3:
        bot.send_photo(call.message.chat.id, open('4s.jpg', 'rb'))
    if a == 4:
        bot.send_photo(call.message.chat.id, open('5s.jpg', 'rb'))
    if a == 5:
        bot.send_photo(call.message.chat.id, open('6s.jpg', 'rb'))
    if a == 6:
        bot.send_photo(call.message.chat.id, open('7s.jpg', 'rb'))
    if a == 7:
        bot.send_photo(call.message.chat.id, open('8s.jpg', 'rb'))
    if a == 8:
        bot.send_photo(call.message.chat.id, open('9s.jpg', 'rb'))
    if a == 9:
        bot.send_photo(call.message.chat.id, open('10s.jpg', 'rb'))
    bot.send_message(call.message.chat.id, '⬇️Дальше⬇️', reply_markup=markup)

bot.polling()

