import os

import requests
from pyrogram.errors import FloodWait
from datetime import datetime
from fuzzywuzzy import fuzz
from requests import get

from my_package.GameQuest import GameQuest
from my_package.Music import Music
from my_package.Push import *
from my_package.Millionaire import Millionaire
from my_package.RockPaperScissors import RockPaperScissors
from my_package.SlotMachine import SlotMachine
from my_package.Talking import Talking
from my_package.mute import *
from statistic import *
from my_package.BlackJack import BlackJack
from my_package.Horoscope import Horoscope
from my_package.OthersGameMethods import *

# Создаем бота
isPush = False
pushAdmin = ""
addAdmin = ""
isAddQuestion = False
questionString = ""
answerString = ""
questionNumberToAdd = 0
standardPoint = 5000
masVerify = []
mas = []
masParaLove = []
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
if os.path.exists('../resources/data/masParaLove.txt'):
    f7 = open('../resources/data/masParaLove.txt', 'r', encoding='UTF-8')
    for x7 in f7:
        masParaLove.append(x7)
    f7.close()


def update(questionString, answerString):
    questionString = questionString.lower().strip()
    answerString = answerString.lower().strip()
    x = open('../resources/data/boltun.txt', 'a', encoding='UTF-8')
    x.write("u: " + questionString + '\n')
    x.write(answerString + '\n')
    x.close()
    f = open('../resources/data/boltun.txt', 'r', encoding='UTF-8')
    countMas = 0
    valumeMas = len(mas) - 1
    for x in f:
        if countMas <= valumeMas:
            mas[countMas] = x
            countMas = countMas + 1
        else:
            mas.append(x.strip().lower())
    lastString = 'u: fUnCr55Iofefsfcccраытысш'
    mas.append(lastString.strip().lower())
    f.close()


def addAnswer(text, questionNumber):
    text = text.lower().strip()
    valumeMas = len(mas)
    memoryMas = []
    countMemory = 0
    count = questionNumber + 1
    while count != valumeMas - 1:
        memoryMas.append(mas[count].strip().lower())
        count = count + 1
    count = questionNumber + 1
    while count < valumeMas + 1:
        if count == valumeMas:
            lastString = 'u: fUnCr55Iofefsfcccраытысш'
            mas.append(lastString.strip().lower())
        if count == questionNumber + 1:
            mas[count] = text
        if count < valumeMas:
            if count > questionNumber + 1:
                mas[count] = memoryMas[countMemory]
                countMemory = countMemory + 1
        count = count + 1
    x = open('../resources/data/boltun.txt', 'w', encoding='UTF-8')
    count = 0
    for z in mas:
        if count != len(mas) - 1:
            x.write(z.strip() + '\n')
        count = count + 1
    x.close()


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
    if call.data == "cancel":
        global isAddQuestion
        global isPush
        isAddQuestion = False
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
    elif call.data == "yes":
        global answerString
        global questionNumberToAdd
        global questionString
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Добавил")
        update(questionString, answerString)
    elif call.data == "no":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ну ок")
        addAnswer(answerString, questionNumberToAdd)
    elif call.data == "addQuestion":
        global addAdmin
        addAdmin = str(call.message.chat.id)
        keyotmena = types.InlineKeyboardMarkup()
        key_otmena = types.InlineKeyboardButton(text='отмена', callback_data='otmena');
        keyotmena.add(key_otmena)
        isAddQuestion = True
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Введите вопрос и ответ которые хотите добавить в формате: \nВопрос\nОтвет")
        cancelButton(call.message)
    elif call.data == "StatGame":
        db = sqlite3.connect('../resources/db/JeckaBot.db')
        cur = db.cursor()
        static = []
        staticMessage = ""
        for x in cur.execute(
                "Select count(*) from users where balance>5000 and active=1"):
            amount = x[0]
        if amount >= 10:
            for x in cur.execute(
                    "Select nickname, balance from users where balance>5000 and active=1 ORDER BY balance DESC Limit 10"):
                static.append(x[0])
                static.append(x[1])
        else:
            for x in cur.execute(
                    "Select nickname, balance from users where balance>5000 ORDER BY balance DESC Limit 10"):
                static.append(x[0])
                static.append(x[1])
        count = 0
        while count < 20:
            if count % 2 == 0:
                staticMessage = staticMessage + str((count + 1) // 2 + 1) + ". " + str(static[count])
            else:
                staticMessage = staticMessage + ": " + str(static[count]) + '\n'
            count = count + 1
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Самые успешные люди:\n" + staticMessage)
        db.close()
        updateStatistic(call.message, "StatGame")
    elif call.data == "krutkonec":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Приходи еще")
    elif call.data == "love":
        perc = random.randint(18, 23)
        while perc < 100:
            try:
                text = "😇 Поиск пары в процессе ..." + str(perc) + "%"
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text=text)

                perc += random.randint(14, 27)
                sleep(0.3)

            except FloodWait as e:
                sleep(e.x)

        lenghtMasPara = len(masParaLove)
        urlNumber = random.randint(0, lenghtMasPara - 1)
        url = masParaLove[urlNumber]
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Твоя Любовь найдена  ❤ ")
        bot.send_photo(chat_id=call.message.chat.id, photo=get(url).content)
    elif call.data == "game":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        game(call.message)
    elif call.data == "music":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        music(call.message)
    elif call.data == "weather":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        weather(call.message)
    elif call.data == "silence":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        muteunmute(call.message)
    elif call.data == "horoscope":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        Horoscope.handle_AriesMenu(call.message)
        updateStatistic(call.message, "horoscope")
        adminNotification(call.message, "Смотрит гороскоп")
    elif call.data == "para":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        hack(call.message)
        updateStatistic(call.message, "para")


# Музыка
@bot.message_handler(commands=["music", "музыка"])
def music(message, res=False):
    keymusic = types.InlineKeyboardMarkup()
    key_musicStart = types.InlineKeyboardButton(text='Включить музыку', callback_data='musicStart')
    keymusic.add(key_musicStart)
    key_musicList = types.InlineKeyboardButton(text='Мой плейлист', callback_data='musicList')
    keymusic.add(key_musicList)
    bot.send_message(message.chat.id, 'Что хотите послушать ?',
                     reply_markup=keymusic)
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
def game(message, res=False):
    db = sqlite3.connect('../resources/db/JeckaBot.db')
    cur = db.cursor()
    try:
        cur.execute(
            "UPDATE Users SET (nickname) = '" + str(message.chat.first_name) + "'" + " WHERE userId = " + str(
                message.chat.id))
        db.commit()
    except:
        print("error update nickname")
    db.close()
    keygame = types.InlineKeyboardMarkup()
    key_Game0 = types.InlineKeyboardButton(text='Кто хочет стать миллионером?', callback_data='millionaire')
    keygame.add(key_Game0)
    key_Game1 = types.InlineKeyboardButton(text='Камень,Ножницы,Бумага', callback_data='GameSSP')
    keygame.add(key_Game1)
    key_Game2 = types.InlineKeyboardButton(text='Слот-машина', callback_data='SlotMachine')
    keygame.add(key_Game2)
    key_Game3 = types.InlineKeyboardButton(text='Блекджек', callback_data='BlackJack')
    keygame.add(key_Game3)
    key_Quest = types.InlineKeyboardButton(text='Путешествие Жеки', callback_data='Quest')
    keygame.add(key_Quest)
    key_StatGame = types.InlineKeyboardButton(text='Статистика', callback_data='StatGame')
    keygame.add(key_StatGame)
    bot.send_message(message.chat.id, 'Во что сыграем ?\nВаш Баланс: ' + str(getBalance(message)), reply_markup=keygame)
    adminNotification(message, "Пошел играть")
    updateStatistic(message, "game")


# Команда «Старт»
@bot.message_handler(commands=["start", "старт"])
def start(message, res=False):
    UserId = 0
    db = sqlite3.connect('../resources/db/JeckaBot.db')
    cur = db.cursor()
    pl = open('../resources/usersPlayLists/music' + str(message.chat.id) + '.txt', 'a', encoding='UTF-8')
    si = str(message.from_user.first_name)
    sz = message.chat.id
    for s in cur.execute("SELECT * FROM Users WHERE userId =" + str(message.chat.id)):
        UserId = s[0]
    if UserId == 0:
        global standardPoint
        cur.execute("INSERT INTO Users (userId, nickname, balance, active) VALUES (?, ?, ?, ?);",
                    (sz, f"{si}", standardPoint, 1))
        db.commit()
    db.close()
    pl.close()
    bot.send_message(message.chat.id,
                     '{}, привет, меня зовут ЖекаБот. Напиши мне Привет :)\nОбязательно введи /help что бы увидеть '
                     'что я умею'.format(
                         message.from_user.first_name))


# Команда "ХЕЛП"
@bot.message_handler(commands=["help"])
def help(message, res=False):
    bot.send_message(message.chat.id,
                     'Привет, вот что я умею' + '\n❕ Список Команд ❕\n/menu - Вызвать меню\n/apps - вызвать '
                                                'панель приложений\n/settings - вызвать панель настроек\n/off - '
                                                'установить мут\n/on - снять мут\nЕще '
                                                'я могу отвечать на твои сообщения, картинки, стикеры.\nИ каждый день '
                                                'учусь новому.')


# Команда "Бот меню"
@bot.message_handler(commands=["menu"])
def menu(message, res=False):
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
def botFunny(message, res=False):
    botPanel = types.InlineKeyboardMarkup()
    key_game = types.InlineKeyboardButton(text='Играть', callback_data='game')
    key_music = types.InlineKeyboardButton(text='Музыка', callback_data='music')
    key_weather = types.InlineKeyboardButton(text='Погода', callback_data='weather')
    key_horoscope = types.InlineKeyboardButton(text='Гороскоп', callback_data='horoscope')
    key_para = types.InlineKeyboardButton(text='Пара дня', callback_data='para')
    botPanel.row(key_game, key_weather)
    botPanel.row(key_music, key_horoscope)
    botPanel.row(key_para)
    bot.send_message(message.chat.id, 'Чем желаешь заняться?', reply_markup=botPanel)
    adminNotification(message, "Вызвал панель приложений")


@bot.message_handler(commands=["настройки", "settings"])
def botSettings(message, res=False):
    muteStatus = 2
    db = sqlite3.connect('../resources/db/JeckaBot.db')
    cur = db.cursor()
    for x in cur.execute("SELECT mute FROM Users WHERE userId=" + str(message.chat.id)):
        muteStatus = x[0]
    db.close()
    botPanel = types.InlineKeyboardMarkup()
    if muteStatus == 0:
        key_silence = types.InlineKeyboardButton(text='Установить мут', callback_data='silence')
    else:
        key_silence = types.InlineKeyboardButton(text='Снять мут', callback_data='silence')
    botPanel.add(key_silence)
    bot.send_message(message.chat.id, 'Доступные тебе настройки', reply_markup=botPanel)
    adminNotification(message, "Вызвал панель настроек")


# Команда "Погода"
@bot.message_handler(commands=["погода", "weather"])
def weather(message, res=False):
    db = sqlite3.connect('../resources/db/JeckaBot.db')
    cur = db.cursor()
    cur.execute("UPDATE Users SET weather = 1 WHERE userId = " + str(message.chat.id))
    db.commit()
    db.close()
    bot.send_message(chat_id=message.chat.id, text='В Каком городе тебя интересует погода ?')
    updateStatistic(message, "weather")


def textCity(message):
    try:
        bot.send_message(chat_id=message.chat.id, text=get_weather(message.text, open_weather_token))
    except:
        bot.send_message(chat_id=message.chat.id,
                         text="К сожалению, пока не могу подсказать погоду. Что-то поломалось(")


def get_weather(message, open_weather_token):
    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorn": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }
    try:
        City = message
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={City}&appid={open_weather_token}&units=metric"
        )
        data = r.json()

        cur_city = data["name"]
        cur_weather = data["main"]["temp"]
        cur_humidity = data["main"]["humidity"]
        cur_pressure = data["main"]["pressure"]
        cur_wind = data["wind"]["speed"]
        cur_sunrise = datetime.fromtimestamp(data["sys"]["sunrise"])
        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Не пойму что там, посмотри в окно"
        text = (f"Погода в городе: {cur_city}\nТемпература: {cur_weather}C° {wd}\n"
                f"Влажность: {cur_humidity}%\nДавление: {cur_pressure} мм.рт.ст\nВетер: {cur_wind}\n"
                f"Закат Солнца: {cur_sunrise}")
        return text

    except Exception as ex:
        text2 = 'я не знаю такого города'
        return text2


# Команда "Пара дня"
def hack(message):
    keylove = types.InlineKeyboardMarkup()
    key_love = types.InlineKeyboardButton(text='Поиск пары дня', callback_data='love')
    keylove.add(key_love)
    bot.send_message(message.chat.id, 'Ну что найдем для тебя пару дня ?', reply_markup=keylove)
    adminNotification(message, "Смотрит пару дня")


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
    if isAdmin == True:
        bot.send_message(message.chat.id, ' {}, вы авторизованы! \n\n'.format(message.from_user.first_name),
                         reply_markup=keyadmin)
    else:
        bot.send_message(message.chat.id, ' {}, у Вас нет прав администратора'.format(message.from_user.first_name))
        for x in admin:
            try:
                bot.send_message(x, message.from_user.first_name + " - Попытался вызвать панель админа")
            except:
                print('Не удалось отправить сообщение администратору')


def cancelButton(message):
    keyCancel = types.InlineKeyboardMarkup()  # наша клавиатура
    key_cancel = types.InlineKeyboardButton(text='Отменить операцию', callback_data='cancel')  # кнопка «Да»
    keyCancel.add(key_cancel)  # добавляем кнопку в клавиатуру
    bot.send_message(message.chat.id, "Нажмите, если хотите отменить операцию", reply_markup=keyCancel)


# Команда добавления
def addQuestion(message):
    degreeOfSimilarity = 0
    maximumSimilarity = 0
    elementNumber = 0
    global questionNumberToAdd
    questionNumberToAdd = 0
    index = message.text.find("\n")
    global questionString
    global answerString
    questionString = message.text[:index]
    answerString = message.text[index + 1:]
    for q in mas:
        if 'u: ' in q:
            degreeOfSimilarity = (fuzz.token_sort_ratio(q.replace('u: ', ''), questionString))
            if degreeOfSimilarity > maximumSimilarity:
                maximumSimilarity = degreeOfSimilarity
                questionNumberToAdd = elementNumber
        elementNumber = elementNumber + 1
    if maximumSimilarity > 70:
        questionOfSimilary = "В базе есть похожий вопрос:\n" + mas[questionNumberToAdd].replace('u: ',
                                                                                                '') + "\n" + "ты уверен, что хочешь добавить новый? "
        keyboard = types.InlineKeyboardMarkup()  # наша клавиатура
        key_yes = types.InlineKeyboardButton(text='Добавить', callback_data='yes')  # кнопка «Да»
        keyboard.add(key_yes)  # добавляем кнопку в клавиатуру
        key_no = types.InlineKeyboardButton(text='Добавить ответ к существующему', callback_data='no')
        keyboard.add(key_no)
        bot.send_message(message.chat.id, questionOfSimilary, reply_markup=keyboard)
    else:
        update(questionString, answerString)


def handle_UserId(message):
    # Запись userId
    UserId = 0
    db = sqlite3.connect('../resources/db/JeckaBot.db')
    cur = db.cursor()
    pl = open('../resources/usersPlayLists/music' + str(message.chat.id) + '.txt', 'a', encoding='UTF-8')
    si = str(message.from_user.first_name)
    sz = message.chat.id
    for s in cur.execute("SELECT * FROM Users WHERE userId =" + str(message.chat.id)):
        UserId = s[0]
    if UserId == 0:
        global standardPoint
        cur.execute("INSERT INTO Users (userId, nickname, balance, active) VALUES (?, ?, ?, ?);",
                    (sz, f"{si}", standardPoint, 1))
        db.commit()
    db.close()
    pl.close()


@bot.message_handler(content_types=["text"])
def handle_text(message):
    global isPush
    global isAddQuestion
    global addAdmin
    global pushAdmin
    ignoreListParameter = False
    isAdmin = False
    for x in admin:
        if message.chat.id == x:
            isAdmin = True
    for x in ignoreList:
        if message.chat.id == x:
            ignoreListParameter = True
    muteStatus = 2
    db = sqlite3.connect('../resources/db/JeckaBot.db')
    cur = db.cursor()
    for x in cur.execute("SELECT mute FROM Users WHERE userId=" + str(message.chat.id)):
        muteStatus = x[0]
    db.close()
    handle_UserId(message)
    isStandardAnswer = True
    db = sqlite3.connect('../resources/db/JeckaBot.db')
    cur = db.cursor()
    for x in cur.execute("SELECT weather FROM Users WHERE userId=" + str(message.chat.id)):
        weatherStatus = x[0]
        if weatherStatus == 1:
            textCity(message)
            cur.execute("UPDATE Users SET weather = 0 WHERE userId = " + str(message.chat.id))
            db.commit()
            isStandardAnswer = False
    db.close()
    if isAddQuestion:
        if isAdmin:
            if addAdmin == str(message.chat.id):
                addQuestion(message)
                isStandardAnswer = False
                isAddQuestion = False
                addAdmin = "0"
    if isPush:
        if isAdmin:
            if pushAdmin == str(message.chat.id):
                push(message.text)
                pushAdmin = "0"
                isStandardAnswer = False
                isPush = False
    Music.audio_text_set(message, musicList)
    if muteStatus == 0:
        if isStandardAnswer:
            realAnswer, Similarity = Talking.answer(message.text, mas)
            bot.send_message(message.chat.id, realAnswer)


# Запускаем бота
bot.polling(none_stop=True, interval=0)
