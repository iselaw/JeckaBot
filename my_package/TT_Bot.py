import os
from random import random

from telebot import types

from my_package.BlackJack import BlackJack
from my_package.GameQuest import GameQuest
from my_package.Horoscope import Horoscope
from my_package.Love import Love
from my_package.Millionaire import Millionaire
from my_package.Music import Music
from my_package.Push import *
from my_package.RockPaperScissors import RockPaperScissors
from my_package.SlotMachine import SlotMachine
from my_package.Talking import Talking
from my_package.User import User
from my_package.Weather import Weather
from statistic import *

# Создаем бота
isPush = False
pushAdmin = ""
addAdmin = ""
questionString = ""
answerString = ""
questionNumberToAdd = 0
standard_point = 5000
masVerify = []
mas = []
massive_love = []
masstiker = []
musicList = []
db = sqlite3.connect('../resources/db/JeckaBot.db')
cur = db.cursor()
for s in cur.execute('SELECT Performer||Title FROM Music where Performer is not null AND Title IS NOT NULL'):
    musicList.append(s[0])
db.close()
if os.path.exists('../resources/data/boltun.txt'):
    f = open('../resources/data/boltun.txt', 'r', encoding='UTF-8')
    for x in f:
        if len(x.strip()) > 2:
            mas.append(x.strip().lower())
    lastString = 'u: fUnCr55Iofefsfcccраытысш'
    mas.append(lastString.strip().lower())
    f.close()
if os.path.exists('../resources/data/stiker.txt'):
    f3 = open('../resources/data/stiker.txt', 'r', encoding='UTF-8')
    for x3 in f3:
        if len(x3.strip()) > 2:
            masstiker.append(x3.strip())
    f3.close()
if os.path.exists('../resources/data/massive_love.txt'):
    f7 = open('../resources/data/massive_love.txt', 'r', encoding='UTF-8')
    for x7 in f7:
        massive_love.append(x7)
    f7.close()

# Отправка фото на фото
@bot.message_handler(content_types=["photo"])
def handle_photo(message):
    muteStatus = 2
    db = sqlite3.connect('../resources/db/JeckaBot.db')
    cur = db.cursor()
    for x in cur.execute("SELECT mute FROM Users WHERE userId=" + str(message.chat.id)):
        muteStatus = x[0]
    db.close()
    if muteStatus == 0:
        photo = open('../resources/photos/1.jpg', 'rb')
        bot.send_photo(chat_id=message.chat.id, photo=photo,
                       caption='Крутая фотка, а это я в Америке')
    isAdmin = False
    for x in admin:
        if message.chat.id == x:
            isAdmin = True
    if not isAdmin:
        for x in admin:
            try:
                bot.send_message(x, message.from_user.first_name + " - Отправил картинку в чат")
                bot.send_photo(x, message.photo[len(message.photo) - 1].file_id)
            except:
                print('Не удалось отправить сообщение администратору')


# Отправка Стикеров на Стикер
@bot.message_handler(content_types=["sticker"])
def handle_sticker(message):
    muteStatus = 2
    db = sqlite3.connect('../resources/db/JeckaBot.db')
    cur = db.cursor()
    for x in cur.execute("SELECT mute FROM Users WHERE userId=" + str(message.chat.id)):
        muteStatus = x[0]
    db.close()
    if muteStatus == 0:
        lenghtMasStiker = len(masstiker)
        stiker = random.randint(0, lenghtMasStiker - 1)
        stikerr = masstiker[stiker]
        bot.send_sticker(message.chat.id, stikerr)
    isAdmin = False
    for x in admin:
        if message.chat.id == x:
            isAdmin = True
    if not isAdmin:
        for x in admin:
            try:
                bot.send_message(x, message.from_user.first_name + " - Отправил стикер в чат")
                bot.send_sticker(x, message.sticker.file_id)
            except:
                print('Не удалось отправить сообщение администратору')


# Отправка Сообщения на голосовое
@bot.message_handler(content_types=['voice'])
def voice_processing(message):
    muteStatus = 2
    db = sqlite3.connect('../resources/db/JeckaBot.db')
    cur = db.cursor()
    for x in cur.execute("SELECT mute FROM Users WHERE userId=" + str(message.chat.id)):
        muteStatus = x[0]
    db.close()
    if muteStatus == 0:
        bot.send_message(message.chat.id,
                         "Прости, я пока не могу слушать, напиши текстом")
    isAdmin = False
    for x in admin:
        if message.chat.id == x:
            isAdmin = True
    if not isAdmin:
        for x in admin:
            try:
                bot.send_message(x, message.from_user.first_name + " - Отправил голосовое в чат")
                bot.send_voice(x, message.voice.file_id)
            except:
                print('Не удалось отправить сообщение администратору')


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    GameQuest.gameQuest_handler(call)
    BlackJack.bj_handler(call)
    Millionaire.millionaire_handler(call)
    Horoscope.horoscope_handler(call)
    SlotMachine.sm_handler(call)
    RockPaperScissors.rps_handler(call)
    Music.music_handler(call)
    Love.love_handler(call, massive_love)
    User.user_handler(call)
    if call.data == "cancel":
        global isPush
        isPush = False
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Операция отменена")
    elif call.data == "spam":
        global pushAdmin
        pushAdmin = str(call.message.chat.id)
        isPush = True
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Введите текст который хотите отправить")
        cancelButton(call.message)
    elif call.data == "stat":
        getStatistic(call.message)
    elif call.data == "game":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        game(call.message)
    elif call.data == "music":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        music(call.message)
    elif call.data == "weather":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        weather(call.message)
    elif call.data == "horoscope":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        Horoscope.handle_AriesMenu(call.message)
        updateStatistic(call.message, "horoscope")
        adminNotification(call.message, "Смотрит гороскоп")


# Музыка
@bot.message_handler(commands=["music", "музыка"])
def music(message):
    Music.start_music(message)
    adminNotification(message, "Пошел слушать музыку")
    updateStatistic(message, "music")


def adminNotification(message, text):
    isAdmin = False
    for x in admin:
        if message.chat.id == x:
            isAdmin = True
    if not isAdmin:
        for x in admin:
            try:
                bot.send_message(x, message.chat.first_name + " - " + text)
            except:
                bot.send_message(x, message.chat.title + " - " + text)


# Добавление Аудио
@bot.message_handler(content_types=['audio'])
def audio_record(message):
    Music.audio_record(message, musicList)


# Команда "Игра"
@bot.message_handler(commands=["game", "игра"])
def game(message):
    User.game_menu(message)
    adminNotification(message, "Пошел играть")
    updateStatistic(message, "game")


# Команда «Старт»
@bot.message_handler(commands=["start", "старт"])
def start(message):
    User.insert_user_id(message, standard_point)
    bot.send_message(message.chat.id,
                     'Привет, {},меня зовут Жека бот.\nОбязательно введи /help'.format(
                         message.from_user.first_name))


# Команда "ХЕЛП"
@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id,
                     'Привет, вот что я умею' + '\n❕ Список Команд ❕\n/menu - Вызвать меню\n/apps - вызвать '
                                                'панель приложений\n/settings - вызвать панель настроек\n/off - '
                                                'установить мут\n/on - снять мут\nЕще '
                                                'я могу отвечать на твои сообщения, картинки, стикеры.\nИ каждый день '
                                                'учусь новому.')


# Команда "Бот меню"
@bot.message_handler(commands=["menu"])
def menu(message):
    keyboardgame = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn3 = types.KeyboardButton('/музыка')
    btn4 = types.KeyboardButton('/игра')
    btn2 = types.KeyboardButton('/настройки')
    btn5 = types.KeyboardButton('/приложения')
    btn6 = types.KeyboardButton('/admin')
    isAdmin = False
    for x in admin:
        if message.chat.id == x:
            isAdmin = True
    if not isAdmin:
        keyboardgame.add(btn3, btn4, btn2, btn5)
    else:
        keyboardgame.add(btn3, btn4, btn2, btn5, btn6)
    bot.send_message(message.chat.id, 'Что нужно?', reply_markup=keyboardgame)


@bot.message_handler(commands=["приложения", "apps"])
def apps_menu(message):
    User.apps_menu(message)
    adminNotification(message, "Вызвал панель приложений")


@bot.message_handler(commands=["настройки", "settings"])
def settings_menu(message):
    User.settings_menu(message)
    adminNotification(message, "Вызвал панель настроек")


# Команда "Погода"
@bot.message_handler(commands=["погода", "weather"])
def weather(message):
    Weather.weather_start(message)
    updateStatistic(message, "weather")


# Команда "Админ"
@bot.message_handler(commands=['admin'])
def startadm(message: types.Message):
    keyadmin = types.InlineKeyboardMarkup()
    key_stat = types.InlineKeyboardButton(text='Статистика Бота', callback_data='stat')
    keyadmin.add(key_stat)
    key_spam = types.InlineKeyboardButton(text='Отправить Сообщение Всем ', callback_data='spam')
    keyadmin.add(key_spam)
    key_addQuestion = types.InlineKeyboardButton(text='Добавить вопрос ', callback_data='addQuestion')
    keyadmin.add(key_addQuestion)
    isAdmin = False
    for x in admin:
        if message.chat.id == x:
            isAdmin = True
    if isAdmin:
        bot.send_message(message.chat.id, '{}, вы авторизованы! \n\n'.format(message.from_user.first_name),
                         reply_markup=keyadmin)
    else:
        bot.send_message(message.chat.id, '{}, у Вас нет прав администратора'.format(message.from_user.first_name))


@bot.message_handler(commands=["молчанка"])
def mute_tumbler(message):
    User.mute_tumbler(message)


@bot.message_handler(commands=["off"])
def mute(message):
    User.mute(message)


@bot.message_handler(commands=["on"])
def un_mute(message):
    User.un_mute(message)

def cancelButton(message):
    keyCancel = types.InlineKeyboardMarkup()  # наша клавиатура
    key_cancel = types.InlineKeyboardButton(text='Отменить операцию', callback_data='cancel')  # кнопка «Да»
    keyCancel.add(key_cancel)  # добавляем кнопку в клавиатуру
    bot.send_message(message.chat.id, "Нажмите, если хотите отменить операцию", reply_markup=keyCancel)

@bot.message_handler(content_types=["text"])
def handle_text(message):
    global standard_point
    global isPush
    global addAdmin
    global pushAdmin
    User.insert_user_id(message, standard_point)
    isAdmin = False
    for x in admin:
        if message.chat.id == x:
            isAdmin = True
    if isPush:
        if isAdmin:
            if pushAdmin == str(message.chat.id):
                push(message.text)
                pushAdmin = "0"
                isPush = False
    isAnswered = Love.love_text_set(message)
    if isAnswered:
        return
    isAnswered = Weather.get_weather_text(message)
    if isAnswered:
        return
    isAnswered = Music.audio_text_set(message, musicList)
    if isAnswered:
        return
    Talking.answer(message, mas)


# Запускаем бота
bot.polling(none_stop=True, interval=0)
