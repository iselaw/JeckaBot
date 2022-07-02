import telebot
import gspread
import os
import time
from time import sleep
import random
from pyrogram.errors import FloodWait
from datetime import datetime
from requests import get
from telebot import types
from fuzzywuzzy import fuzz
import pytz
import requests
import re
import xmltodict
import urllib.request as urllib2
from telebot.types import InputMediaAudio
from typing import Any
from GameQvest import *
from Films import *
from Login import *
from Music import *
# Создаем бота
isPush = False
pushAdmin = ""
addAdmin = ""
isAddQuestion = False
questionString = ""
answerString = ""
questionNumberToAdd = 0
worksheet = sh.sheet1
# Загружаем в массив
standatPoint = 5000
weatherStatus = []
UseridMas = []
masVerify = []
mas = []
masurl = []
masParaLove = []
masstiker = []
masScore = []
if os.path.exists('data/boltun.txt'):
    f = open('data/boltun.txt', 'r', encoding='UTF-8')
    for x in f:
        if (len(x.strip()) > 2):
            mas.append(x.strip().lower())
    lastString = 'u: fUnCr55Iofefsfcccраытысш'
    mas.append(lastString.strip().lower())
    f.close()
if os.path.exists('data/masurl.txt'):
    f2 = open('data/masurl.txt', 'r', encoding='UTF-8')
    for x2 in f2:
        masurl.append(x2)
    f2.close()
if os.path.exists('data/stiker.txt'):
    f3 = open('data/stiker.txt', 'r', encoding='UTF-8')
    for x3 in f3:
        if (len(x3.strip()) > 2):
            masstiker.append(x3.strip())
    f3.close()
if os.path.exists('data/UseridMas.txt'):
    f4 = open('data/UseridMas.txt', 'r', encoding='UTF-8')
    for x4 in f4:
        UseridMas.append(x4.strip())
        weatherStatus.append(0)
    f4.close()
if os.path.exists('data/balls.txt'):
    f5 = open('data/balls.txt', 'r', encoding='UTF-8')
    for x5 in f5:
        masScore.append(int(x5))
    f5.close()
if os.path.exists('data/masParaLove.txt'):
    f7 = open('data/masParaLove.txt', 'r', encoding='UTF-8')
    for x7 in f7:
        masParaLove.append(x7)
    f7.close()

def update(questionString, answerString):
    questionString = questionString.lower().strip()
    answerString = answerString.lower().strip()
    x = open('data//boltun.txt', 'a', encoding='UTF-8')
    x.write("u: " + questionString + '\n')
    x.write(answerString + '\n')
    x.close()
    f = open('data/boltun.txt', 'r', encoding='UTF-8')
    countMas = 0
    valumeMas = len(mas) - 1
    for x in f:
        if (countMas <= valumeMas):
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
        if (count == valumeMas):
            lastString = 'u: fUnCr55Iofefsfcccраытысш'
            mas.append(lastString.strip().lower())
        if (count == questionNumber + 1):
            mas[count] = text
        if (count < valumeMas):
            if (count > questionNumber + 1):
                mas[count] = memoryMas[countMemory]
                countMemory = countMemory + 1
        count = count + 1
    x = open('data//boltun.txt', 'w', encoding='UTF-8')
    count = 0
    for z in mas:
        if (count != len(mas) - 1):
            x.write(z.strip() + '\n')
        count = count + 1
    x.close()

def push(text):
    for s in UseridMas:
        try:
            bot.send_message(s, text)
        except:
            print("Не удалось отправить сообщение")

def answer(text):
    text = text.lower().strip()
    try:
        valumeMas = len(mas) - 1
        if os.path.exists('data/boltun.txt'):
            maximumSimilarity = 0
            elementNumber = 0
            questionNumber = 0
            for q in mas:
                if ('u: ' in q):
                    # С помощью fuzzywuzzy получаем, насколько похожи две строки
                    degreeOfSimilarity = (fuzz.token_sort_ratio(q.replace('u: ', ''), text))
                    if (degreeOfSimilarity > maximumSimilarity):
                        maximumSimilarity = degreeOfSimilarity
                        if (elementNumber != valumeMas):
                            questionNumber = elementNumber
                elementNumber = elementNumber + 1
            isQuestion = False
            count = 1
            while isQuestion == False:
                if ('u: ' not in mas[questionNumber + count]):
                    count = count + 1
                if ('u: ' in mas[questionNumber + count]):
                    isQuestion = True
            answerNumber = random.randint(1, count - 1)
            answer = mas[questionNumber + answerNumber]
            return answer
        else:
            return 'Не понял, перефразируй'
    except:
        return 'Не совсем понял вопрос'

# Отправка фото на фото
@bot.message_handler(content_types=["photo"])
def handle_photo(message):
    lenghtMasUrl = len(masurl)
    urlNumber = random.randint(0, lenghtMasUrl - 1)
    url = masurl[urlNumber]
    bot.send_photo(message.chat.id, get(url).content)
    from pathlib import Path
    Path(f'files/{message.chat.id}/').mkdir(parents=True, exist_ok=True)
    if message.content_type == 'photo':
        file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        src = f'files/{message.chat.id}/' + file_info.file_path.replace('photos/', '')
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)

# Отправка Стикеров на Стикер
@bot.message_handler(content_types=["sticker"])
def handle_sticker(message):
    lenghtMasStiker = len(masstiker)
    stiker = random.randint(0, lenghtMasStiker - 1)
    stikerr = masstiker[stiker]
    bot.send_sticker(message.chat.id, stikerr)

# Отправка Сообщения на голосовое
@bot.message_handler(content_types=['voice'])
def voice_processing(message):
    bot.send_message(message.chat.id,
                     "{} Прости, я пока не могу слушать, напиши текстом".format(message.from_user.first_name))

# Команда "Курс"
@bot.message_handler(commands=["курс", "course"])
def startcourse(message, res=False):
    keycoursemenu = types.InlineKeyboardMarkup()
    key_rub = types.InlineKeyboardButton(text='Курс Валюты', callback_data='rub')
    keycoursemenu.add(key_rub)
    key_crip = types.InlineKeyboardButton(text='Курс Криптовалюты', callback_data='crip')
    keycoursemenu.add(key_crip)
    bot.send_message(message.chat.id, 'Что именно тебя интересует ?', reply_markup=keycoursemenu)

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    if call.data == "cancel":
        global isAddQuestion
        global isPush
        isAddQuestion = False
        isPush = False
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Операция отменена")
    elif call.data == "dollar":
        resd = worksheet.get('A2')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Доллар стоит сейчас " + str(resd))
    elif call.data == "Euro":
        rese = worksheet.get('B2')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Евро сейчас стоит" + str(rese))
    elif call.data == "Hryvnia":
        resh = worksheet.get('C2')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Гривна сейчас стоит" + str(resh))
    elif call.data == "spam":
        global pushAdmin
        pushAdmin = str(call.message.chat.id)
        isPush = True
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Введите текст который хотите отправить")
        cancelButton(call.message)
    elif call.data == "stat":
        number_of_elements = len(UseridMas)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="❕ Информация:\n\n❕ Пользовователей в боте - " + str(number_of_elements))
    elif call.data == "rub":
        keycourse = types.InlineKeyboardMarkup()
        key_dollar = types.InlineKeyboardButton(text='Доллар', callback_data='dollar')
        keycourse.add(key_dollar)
        key_Euro = types.InlineKeyboardButton(text='Евро', callback_data='Euro')
        keycourse.add(key_Euro)
        key_Hryvnia = types.InlineKeyboardButton(text='Гривна', callback_data='Hryvnia')
        keycourse.add(key_Hryvnia)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Какая валюта тебя интересует ?', reply_markup=keycourse)
    elif call.data == "crip":
        keycoursecrip = types.InlineKeyboardMarkup();
        key_Bitcoin = types.InlineKeyboardButton(text='Bitcoin', callback_data='Bitcoin')
        keycoursecrip.add(key_Bitcoin)
        key_Ethereum = types.InlineKeyboardButton(text='Ethereum', callback_data='Ethereum')
        keycoursecrip.add(key_Ethereum)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Какой курс криптовалюты тебя интересует ?', reply_markup=keycoursecrip)
    elif call.data == "Bitcoin":
        resbit = worksheet.get('C10')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Bitcoin в долларах сейчас стоит " + str(resbit))
    elif call.data == "Ethereum":
        reseth = worksheet.get('C11')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Ethereum в долларах сейчас стоит " + str(reseth))
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
    elif call.data == "GameSSP":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Выбрано: Камень, Ножницы, Бумага\nВаш баланс: " + getBalance(call.message))
        GameSSP(call.message, "first")
    elif call.data == "StatGame":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Статистика еще не готова")
    elif call.data == "Scissors":
        choice = random.choice(['Камень🤜', 'Ножницы✌️', 'Бумага✋'])
        Scissors = 'Ножницы✌️'
        if Scissors == choice:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='Боевая ничья!')
            itog = "Боевая ничья!"
        else:
            if choice == 'Бумага✋':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Поздравляю с победой! У меня была {}.'.format(
                                          choice))
                itog = 'Поздравляю с победой! У меня была {}.'.format(choice)
            else:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Извините, но Вы проиграли 😢. У меня  {}.'.format(
                                          choice))
                itog = 'Поздравляю с победой! У меня была {}.'.format(choice)
        GameSSP(call.message, itog)
    elif call.data == "Stone":
        choice = random.choice(['Камень🤜', 'Ножницы✌️', 'Бумага✋'])
        Stone = 'Камень🤜'
        if Stone == choice:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='Боевая ничья!')
            itog = "Боевая ничья!"
        else:
            if choice == 'Ножницы✌️':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Поздравляю с победой! У меня была {}.'.format(choice))
                itog = 'Поздравляю с победой! У меня была {}.'.format(choice)
            else:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Извините, но Вы проиграли 😢. У меня  {}.'.format(choice))
                itog = 'Извините, но Вы проиграли 😢. У меня  {}.'.format(choice)
        GameSSP(call.message, itog)
    elif call.data == "Paper":
        choice = random.choice(['Камень🤜', 'Ножницы✌️', 'Бумага✋'])
        Paper = 'Бумага✋'
        if Paper == choice:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='Боевая ничья!')
            itog = "Боевая ничья!"
        else:
            if choice == 'Камень🤜':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Поздравляю с победой! У меня была {}.'.format(
                                          choice))
                itog = 'Поздравляю с победой! У меня была {}.'.format(choice)
            else:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Извините, но Вы проиграли 😢. У меня  {}.'.format(
                                          choice))
                itog = 'Извините, но Вы проиграли 😢. У меня  {}.'.format(choice)
        GameSSP(call.message, itog)
    elif call.data == "gameexit":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Приходи еще")
    elif call.data == "SlotMachine":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Выбрано: Слот-машина\nВаш баланс: " + getBalance(call.message))
        SlotBet(call.message, "first")
    elif call.data == "SlotBet10":
        itog = slotMachine(call.message, 10)
        SlotBet(call.message, itog)
    elif call.data == "SlotBet50":
        itog = slotMachine(call.message, 50)
        SlotBet(call.message, itog)
    elif call.data == "GetCardYes":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Жека-крупье вытаскивает карту из колоды")
        BlackJackNext(call.message, True)
    elif call.data == "GetCardNo":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Очередь Жеки-крупье тянуть карты")
        BlackJackNext(call.message, False)
    elif call.data == "BlackJack50":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Ставка 50\nВаш баланс: " + str(int(getBalance(call.message)) - 50))
        BlackJackFirst(call.message, 50)
    elif call.data == "BlackJack100":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Ставка 100\nВаш баланс: " + str(int(getBalance(call.message)) - 100))
        BlackJackFirst(call.message, 100)
    elif call.data == "BlackJack200":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Ставка 200\nВаш баланс: " + str(int(getBalance(call.message)) - 200))
        BlackJackFirst(call.message, 200)
    elif call.data == "BlackJack":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Выбрано: Блекджек\nВаш баланс: " + getBalance(call.message))
        BJBet(call.message, "first")
    elif call.data == "krutkonec":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Приходи еще")
    # Игра с жекой
    elif call.data == "qvest":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Поиграем?")
        GameQvest(call.message)
    elif call.data == "startqvest":
        photo1 = open('GameQvest/putnic.jpg', 'rb')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Добро пожаловать в мир приключений")
        bot.send_photo(chat_id=call.message.chat.id, photo=photo1)
        Qvestt(call.message)
    elif call.data == "exitqvest":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Очень печально, приходи к нам еще:(")
    elif call.data == "askTraveler":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Путник поведал:\n\"Зря ты без оружия гуляешь по этим местам, Заброшенный Замок неподалеку заселили силы зла во главе с темным рыцарем Листатом. За все время нахождения в замке, прислужники Листата уже похитили 5 девушек из местных деревень и убили 4 торговцев\n\n... Когда я проходил мимо Замка, я наткнулся на группу скелетов-гоблинов, которые начали атаковать меня, я еле убежал от них. Может мне показалось, но еще в небе я увидел огромного красного дракона...\n\n"
                                   "И вроде бы он что-то держал в лапах, что-то похожее на мешки с золотом. Советую тебе быть осторожным, лучше купи снаряжение у Кузница в городе\"")
        Qvest2(call.message, True)
    elif call.data == "blacksmith":
        photo2 = open('GameQvest/kuznec.jpg', 'rb')
        bot.send_photo(chat_id=call.message.chat.id, photo=photo2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы увидели кузнеца у себя в кузнице")
        QvestBlacksith1(call.message, 'Привет. Я кузнец этого города, чем могу тебе помочь?')

    elif call.data == "Market":
        photo3 = open('GameQvest/Рынок.jpg', 'rb')
        bot.send_photo(chat_id=call.message.chat.id, photo=photo3)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Хммм странно, почему-то сегодня на рынке никого нет, куда же все подевались?")
        Qvest2(call.message, False)
    elif call.data == "Castle":
        photo4 = open('GameQvest/замокбездоспехов.jpg', 'rb')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Кажется замок уже близко")
        bot.send_photo(chat_id=call.message.chat.id, photo=photo4)
        bot.send_message(chat_id=call.message.chat.id,
                         text="Хммм вы видите замок рядом с которым обитает дракон")
        QvestCastle1(call.message)
    elif call.data == "CastleOver":
        photo5 = open('GameQvest/gameOver.jpg', 'rb')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Кажется впереди опасные скелеты-гоблины про которых предупреждал путник")
        bot.send_photo(chat_id=call.message.chat.id, photo=photo5)
        bot.send_message(chat_id=call.message.chat.id,
                         text="Вы наткнулись на группу опасных скелетов-гоблинов, они атаковали вас. Вы были очень сильно ранены, тк были без доспехов, и погибли.\n\n\n Попробуйте начать с начала")
        GameQvest(call.message)
    elif call.data == "CastleDracon":
        photo6 = open('GameQvest/dragonOver.jpg', 'rb')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Кажется дракон вас заметил, нужно что-то делать")
        bot.send_photo(chat_id=call.message.chat.id, photo=photo6)
        bot.send_message(chat_id=call.message.chat.id,
                         text="Вас увидел дракон, влюбился вас, заставил вас жениться на себе, посадил вас на цепь и теперь вы будете до конца жизни жить с драконом\n\n\n Попробуйте начать с начала")
        GameQvest(call.message)
    elif call.data == "CastleBlacksith":
        QvestBlacksith1(call.message,
                        "Это жуткое место, которое охраняют толпы скелетов и злобный дракон. Говорят, что тот дракон охраняет большую кучу золота, но не кто так и не рискнул побороть его и забрать богатства.")
    elif call.data == "MarketBlacksith":
        QvestBlacksith1(call.message,
                        "Мэр города дал всем выходной в связи с частыми нападками бандитов, которые находятся за городом. Сегодня работаю только я")
    elif call.data == "ArmorBlacksith":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Я могу Продать тебе готовые, либо сделать новые бесплатно если ты принесешь мне дерево или металл")
        BlacksithPurchase(call.message, False)
    elif call.data == "PriceArmor":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Доспехи стоят 100 монет, а у тебя, к сожалению, есть только 30. За 30 монет могу продать тебе только хороший острый меч и сказать как можно раздобыть деньги")
        Outlaw(call.message)
    elif call.data == "WoodMetal":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Я дам тебе кирку и топор, отправляйся для добычи ресурсов и потом ко мне.")
        ResourceExtraction(call.message)
    elif call.data == "TreeMining":
        photo6 = open('GameQvest/лес.jpg', 'rb')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы пришли в лес")
        bot.send_photo(chat_id=call.message.chat.id, photo=photo6)
        TreeMining(call.message)
    elif call.data == "MetalMining":
        photo7 = open('GameQvest/shahta.jpg', 'rb')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы пришли в шахту")
        bot.send_photo(chat_id=call.message.chat.id, photo=photo7)
        MetalMining(call.message)
    elif call.data == "BuyArmor":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Хорошо")
        BlacksithPurchase(call.message, False)
    elif call.data == "OutlawNo":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Хорошо")
        BlacksithPurchase(call.message, False)
    elif call.data == "OutlawYes":
        photo8 = open('GameQvest/bandit.jpg', 'rb')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы пришли в лагерь бандитов")
        bot.send_photo(chat_id=call.message.chat.id, photo=photo8)
        BanditBattle(call.message)
    elif call.data == "BanditDogovor":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Кажется разговор не состоится")
        BanditDogovor(call.message)
    elif call.data == "BanditBattle":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Главарь Бандитов достал меч")
        BanditBattleExit(call.message)
    elif call.data == "DieBandit":
        photo9 = open('GameQvest/banditубил.jpg', 'rb')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы отдали золото и развернулись, чтобы идти  к  Кузнецу. Но глава Бандитов ударил мечом вас в спину.\n\n\n\nВы умерли!!! Попробуйте начать сначала")
        bot.send_photo(chat_id=call.message.chat.id, photo=photo9)
    elif call.data == "BanditBattle2":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Главарь Бандитов достал меч")
        BanditBattleExit(call.message)
    elif call.data == "BlowHead":
        photo10 = open('GameQvest/banditубил.jpg', 'rb')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Весь урон на себя взял шлем, Бандит не пострадал и ударил мечом вас в шею.\n\n\n\nВы умерли!!! Попробуйте начать сначала")
        bot.send_photo(chat_id=call.message.chat.id, photo=photo10)
    elif call.data == "HeartBeat":
        photo11 = open('GameQvest/мертвбандит.jpg', 'rb')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы нанесли сокрушительный урон Главе бандитов, вы убили его, а его подчиненые быстро сбежали увидив такой расклад.")
        bot.send_photo(chat_id=call.message.chat.id, photo=photo11)
        ReceivingMoney(call.message)
    elif call.data == "ReceivingMoney":
        photo12 = open('GameQvest/nagrada.jpg', 'rb')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы пришли к Мэру города ")
        bot.send_photo(chat_id=call.message.chat.id, photo=photo12)
        bot.send_message(chat_id=call.message.chat.id,
                         text="Мэр поблагодарил вас за помощь городу, дал вам положенную награду.\nФуууух теперь можно отправиться к кузнецу и купить у него доспехи для похода к жуткому заброшенному замку")
        BlacksmithArmorPayment(call.message)
    elif call.data == "QvestCastle1NO":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы вернулись назад")
        Qvest2(call.message, False)
    elif call.data == "BlacksmithArmorPayment":
        photo13 = open('GameQvest/Куз2нец.jpg', 'rb')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы пришли к Кузнецу")
        bot.send_photo(chat_id=call.message.chat.id, photo=photo13)
        bot.send_message(chat_id=call.message.chat.id,
                         text="Привет-\nСпасибо что прогнал бандитов. Вот держи свои доспехи. Пожелаю успехов тебе в твоем путешествии")
        Castle(call.message)
    elif call.data == "CastleArmor":
        photo14 = open('GameQvest/pal.jpg', 'rb')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы пришли к Жуткому заброшеному замку. ")
        bot.send_photo(chat_id=call.message.chat.id, photo=photo14)
        bot.send_message(chat_id=call.message.chat.id,
                         text="Вы увидели небольшую группу скелетов около заброшенного замка, пойти к ним ?\n\n\nВы заметили куда полетел Большой красный дракон, в лапах у него сверкала куча золота, пойти к нему?")
        СhoosePath(call.message)
    elif call.data == "MetalMiningExit":
        photo15 = open('GameQvest/brokenкирка.jpg', 'rb')
        bot.send_photo(chat_id=call.message.chat.id, photo=photo15)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы сломали свою Кирку")
        MistakeBroken(call.message)
    elif call.data == "MistakeBroken":
        photo16 = open('GameQvest/kuznec.jpg', 'rb')
        bot.send_photo(chat_id=call.message.chat.id, photo=photo16)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Привет, очень печально что ты сломал инструмент")
        BlacksithPurchase(call.message, True)
    elif call.data == "TreeMiningExit":
        photo17 = open('GameQvest/brogenaxe.jpg', 'rb')
        bot.send_photo(chat_id=call.message.chat.id, photo=photo17)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы сломали свой Топор")
        MistakeBroken(call.message)
    elif call.data == "MetalMiningON":
        photo18 = open('GameQvest/цфвфц.jpg', 'rb')
        bot.send_photo(chat_id=call.message.chat.id, photo=photo18)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы Добыли металл")
        GotIt(call.message)
    elif call.data == "TreeMiningON":
        photo18 = open('GameQvest/дерево.jpg', 'rb')
        bot.send_photo(chat_id=call.message.chat.id, photo=photo18)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы Добыли Дерево")
        GotIt(call.message)
    elif call.data == "GotIt":
        photo19 = open('GameQvest/Куз2нец.jpg', 'rb')
        bot.send_photo(chat_id=call.message.chat.id, photo=photo19)
        bot.send_message(chat_id=call.message.chat.id,
                         text="Привет, я очень рад что ты все добыл, вот держи свои доспехи ")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы прибыли к кузнецу")
        Castle(call.message)
    elif call.data == "СhoosePathDragon":
        photo19 = open('GameQvest/драконзолото.jpg', 'rb')
        bot.send_photo(chat_id=call.message.chat.id, photo=photo19)
        bot.send_message(chat_id=call.message.chat.id,
                         text="Вы приблизлись к логову дракона и увидели, что у него в логове полно золота\nДракон смотрит на вас, Но вроде бы не собираеться атаковать вас")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы прибыли к логову дракона")
        DragonDialogue(call.message)
    elif call.data == "DragonDialogue":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Приветствую тебя, Путник. Ты достаточно храбр, чтобы подойти ко мне. Так и быть, исполню одно твое жилание.")
        DragonExit(call.message)
    elif call.data == "DragonExitGold":
        photo20 = open('GameQvest/жеказолото.png', 'rb')
        bot.send_photo(chat_id=call.message.chat.id, photo=photo20)
        bot.send_message(chat_id=call.message.chat.id,
                         text="Отныне Вы самый богатый человек Мира и вся выша жизнь прошла в роскоши и сытости\n\n\nНебольшой подарок за прохождение игры\nНабор стикеров ZhekaMatuxovbot в средеземье\n\n\nhttps://t.me/addstickers/ZhekaMatuxovbot")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Дракон одарил вас богатсвом")
    elif call.data == "DragonExitLove":
        photo21 = open('GameQvest/жекалюбовь.jpg', 'rb')
        bot.send_photo(chat_id=call.message.chat.id, photo=photo21)
        bot.send_message(chat_id=call.message.chat.id,
                         text="Дракон достает золотую фигурку девушки из своих скоровищ, и преврашает ее в живую девушку из ваших фантазий. Она влюбилась в Вас с первого взгляда. Вы возвращаетесь домой и живете долго и счастливо\n\n\nНебольшой подарок за прохождение игры\nНабор стикеров ZhekaMatuxovbot в средеземье\n\n\nhttps://t.me/addstickers/ZhekaMatuxovbot")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Дракон что-то достает")
    elif call.data == "DragonExitOver":
        photo22 = open('GameQvest/жекаумер.jpg', 'rb')
        bot.send_photo(chat_id=call.message.chat.id, photo=photo22)
        bot.send_message(chat_id=call.message.chat.id,
                         text="Дракон со словами: \"Да как ты смеешь!!!\". Накинулся на вас. От вас остались только доспехи")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Дракон полон ярости")
    elif call.data == "СhoosePathCastle":
        photo23 = open('GameQvest/скелетыжека.jpg', 'rb')
        bot.send_photo(chat_id=call.message.chat.id, photo=photo23)
        bot.send_message(chat_id=call.message.chat.id,
                         text="Вы приблизились к Замку, скелеты-рыцари увидели вас и двинулись в атаку")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы увидели группу скелетов")
        SkeletonsOfbBry(call.message)
    elif call.data == "SkeletonsOfbBry":
        photo24 = open('GameQvest/winskelet.jpg', 'rb')
        bot.send_photo(chat_id=call.message.chat.id, photo=photo24)
        bot.send_message(chat_id=call.message.chat.id,
                         text="Вы убили всех скелетов-рыцарей\nНа полу вы заметили свиток")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Начался трудный бой")
        Ingot(call.message)
    elif call.data == "IngotYes":
        photo24 = open('GameQvest/svitok.jpg', 'rb')
        bot.send_photo(chat_id=call.message.chat.id, photo=photo24)
        bot.send_message(chat_id=call.message.chat.id,
                         text="Вы подняли свиток, раскрыли его и это оказался свиток усиления\nНадеюсь, он поможет мне в дальнейшем пушествий по замку\nВы пошли дальше")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы подняли свиток ")
        Demon(call.message)
    elif call.data == "Demon":
        photo25 = open('GameQvest/vulgrim.jpg', 'rb')
        bot.send_photo(chat_id=call.message.chat.id, photo=photo25)
        bot.send_message(chat_id=call.message.chat.id,
                         text="Приблизившись к демону, он обратился к вам:\n-\"Здравствуй, смертный. Меня зовут Вульгрим. Не знаю зачем направляешься к хозяину этой башни темному рыцарю Листату, но следующий его прислужник тебе не по зубам. Однако, я могу оказать тебе услугу\"")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы подошли к демону")
        Demon2(call.message)
    elif call.data == "Demon2":
        photo26 = open('GameQvest/amulet.jpg', 'rb')
        bot.send_photo(chat_id=call.message.chat.id, photo=photo26)
        bot.send_message(chat_id=call.message.chat.id,
                         text="Демон протягивает некий амулет и говорит:\n-\"Этот артефакт позволит убить твоего следующего противника, его имя Сашаель. Я дам тебе амулет, но взамен ты принесешь мне сердце Сашаеля\"")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Демон продолжил разговор")
        Demon3(call.message)
    elif call.data == "DemonAmuletYes":
        photo27 = open('GameQvest/image15.jpg', 'rb')
        bot.send_message(chat_id=call.message.chat.id,
                         text="Демон улыбнулся и сказал:\n-\"Жду не дождусь когда ты принесешь его сердце мне. Не советую меня обманывать\"\n\n\nВы отправились дальше и встретили Сашаеля")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы взяли амулет")
        bot.send_photo(chat_id=call.message.chat.id, photo=photo27)
        Boss1(call.message)
    elif call.data == "DemonAmuletNo":
        photo28 = open('GameQvest/image15.jpg', 'rb')
        bot.send_message(chat_id=call.message.chat.id,
                         text="Демон оскалился и сказал:\n- \"Что ж, как знаешь, посмотрим как ты справишься с Сашаелем\"\n\n\nВы отправились дальше и встретили Сашаеля")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы отказались от амулета")
        bot.send_photo(chat_id=call.message.chat.id, photo=photo28)
        Boss2(call.message)
    elif call.data == "BossAmuletYes":
        photo29 = open('GameQvest/killsasha.jpg', 'rb')
        bot.send_photo(chat_id=call.message.chat.id, photo=photo29)
        bot.send_message(chat_id=call.message.chat.id,
                         text="При взмахе меча сила амулета перетекла в ваши руки. Вы нанесли сокрушительный удар такой силы, что броня противника разлетелась словно она была изготовлена из хрусталя. Сашаель упал на колени, вы просунули свою руку в отверствие в броне и достали едва бьющиеся сердце этой твари")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы Начали сражение с Сашаелем")
        Demon4(call.message)
    elif call.data == "BossAmuletNo":
        photo30 = open('GameQvest/killgeka.jpg', 'rb')
        bot.send_photo(chat_id=call.message.chat.id, photo=photo30)
        bot.send_message(chat_id=call.message.chat.id,
                         text="Вы нанесли удар по противнику, но вашей силы удара не хватило, чтобы нанести сильные повреждения. Противник размахнулся и своей косой разделил ваше тело на три части \n\n\nВЫ ПОГИБЛИ")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы Начали сражение с Сашаелем")
    elif call.data == "BossExit":
        photo31 = open('GameQvest/killsasha.jpg', 'rb')
        bot.send_photo(chat_id=call.message.chat.id, photo=photo31)
        bot.send_message(chat_id=call.message.chat.id,
                         text="Вы использовали свиток и ощутили прилив сил. Вы произвели серию быстрых атак словно берсерк,броня противника разлетелась словно она была изготовлена из хрусталя. Сашаель упал на колени, вы просунули свою руку в отверствие в броне и достали едва бьющиеся сердце этой твари")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы Начали сражение с Сашаелем")
        SashaelKill(call.message)
    elif call.data == "Demon4":
        photo32 = open('GameQvest/hearth.jpg', 'rb')
        bot.send_photo(chat_id=call.message.chat.id, photo=photo32)
        bot.send_message(chat_id=call.message.chat.id,
                         text="Вы поднимаетесь вверх по лестнице, перед Вами появляется силуэт Вашего знакомого демона Вульгрима.\n - \"Тебе все таки удалось победить в схватке смертный. Кажется, пришло время платить по долгам. Давай мое сердце\"")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы встретили демона")
        Demon5(call.message)
    elif call.data == "DemonHeartYes":
        photo33 = open('GameQvest/listat.jpg', 'rb')
        bot.send_photo(chat_id=call.message.chat.id, photo=photo33)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="\"C тобой приятно иметь дело, что ж, надеюсь еще увидимся\"\nВы поднимаетесь на самый верх башни")
        bot.send_message(chat_id=call.message.chat.id,
                         text="Вы Поднялись на вершину башни. Вы оказались в комнате с огромным количеством золота, у стены сидит связанная девушка. Вы замечаете два светящихся глаза. Видимо это владелец башни Листат, выглядит он устрашающе. После пары секунд молчания он говорит\n\n\"- Придти сюда было глупо. Сейчас ты умрешь")
        MainBoss(call.message)
    elif call.data == "DemonHeartNo":
        photo34 = open('GameQvest/listat.jpg', 'rb')
        bot.send_photo(chat_id=call.message.chat.id, photo=photo34)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вульгрим злится и говорит\n\"- Я это так не оставлю, зря ты решил со мной поссориться.\"\nДемон исчезает на ваших глазах.\nВы поднимаетесь на самый верх башни")
        bot.send_message(chat_id=call.message.chat.id,
                         text="Вы Поднялись на вершину башни. Вы оказались в комнате с огромным количеством золота, у стены сидит связанная девушка. Вы замечаете два светящихся глаза. Видимо это владелец башни Листат, выглядит он устрашающе. После пары секунд молчания он говорит\n\n\"- Придти сюда было глупо. Сейчас ты умрешь")
        MainBoss2(call.message)
    elif call.data == "MainBossExit":
        photo35 = open('GameQvest/ЖекаВин.jpg', 'rb')
        bot.send_photo(chat_id=call.message.chat.id, photo=photo35)
        bot.send_message(chat_id=call.message.chat.id,
                         text="Вы использовали свиток и ощутили прилив сил. Вы произвели серию быстрых атак словно берсерк и перед вами осталась лишь куча мяса противника, будто вы разделали свинью.")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы начали бой")
        VinBoss(call.message)
    elif call.data == "VinBoss":
        photo36 = open('GameQvest/finalgood.jpg', 'rb')
        bot.send_photo(chat_id=call.message.chat.id, photo=photo36)
        bot.send_message(chat_id=call.message.chat.id,
                         text="Вы освободили девушку и забрали золото. Вскоре, вы с ней поженились и купили огромный дом. Вы прожили долгую и счастливую жизнь.\n\n\nНебольшой подарок за прохождение игры\nНабор стикеров ZhekaMatuxovbot в средеземье\n\n\nhttps://t.me/addstickers/ZhekaMatuxovbot")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы освободили девушку и забрали золото")
    elif call.data == "MainBossNo":
        photo37 = open('GameQvest/жекуубилбос.jpg', 'rb')
        bot.send_photo(chat_id=call.message.chat.id, photo=photo37)
        bot.send_message(chat_id=call.message.chat.id,
                         text="Вы попытались нанести удар, но Листат оказался быстрее. Он увернулся от вашей атаки и ловким ударом снес с плечь вашу голов. Вы погибили, а он продолжил развлекаться со своей пленницей.")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы начали бой")
    elif call.data == "SashaelKill":
        photo38 = open('GameQvest/demonBlade.jpg', 'rb')
        bot.send_photo(chat_id=call.message.chat.id, photo=photo38)
        bot.send_message(chat_id=call.message.chat.id,
                         text="Вы встречаете демона. Он предлагает новую сделку:\n\"- Смотрю, тебе удалось победить Сашаэля и даже забрать его сердце, что ж, я тебя недооценил. Но с владельцем этой башни тебе не удастся справиться без артефактов. Предлагаю новую сделку. В обмен на сердце, я дам тебе Клинок Бездны. При должном мастерстве с ним ты без проблем справишься с Листатом\"")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы встретили демона")
        SashaelKill2(call.message)
    elif call.data == "SashaelKillYes":
        photo39 = open('GameQvest/listatwad.jpg', 'rb')
        bot.send_photo(chat_id=call.message.chat.id, photo=photo39)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="\"C тобой приятно иметь дело, что ж, надеюсь еще увидимся\"\nВы поднимаетесь на самый верх башни")
        bot.send_message(chat_id=call.message.chat.id,
                         text="Вы Поднялись на вершину башни. Вы оказались в комнате с огромным количеством золота, у стены сидит связанная девушка. Вы замечаете два светящихся глаза. Видимо это владелец башни Листат, выглядит он устрашающе. После пары секунд молчания он говорит\n\n\"- Придти сюда было глупо. Сейчас ты умрешь")
        MainBoss4(call.message)
    elif call.data == "SashaelKillNo":
        photo40 = open('GameQvest/listat.jpg', 'rb')
        bot.send_photo(chat_id=call.message.chat.id, photo=photo40)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вульгрим злится и говорит:\n\"- Я это так не оставлю, зря ты решил со мной поссорится. Демон исчезает на ваших глазах.\"\nВы поднимаетесь на самый верх башни")
        bot.send_message(chat_id=call.message.chat.id,
                         text="Вы Поднялись на вершину башни. Вы оказались в комнате с огромным количеством золота, у стены сидит связанная девушка. Вы замечаете два светящихся глаза. Видимо это владелец башни Листат, выглядит он устрашающе. После пары секунд молчания он говорит\n\n\"- Придти сюда было глупо. Сейчас ты умрешь")
        MainBoss3(call.message)
    elif call.data == "Died":
        photo41 = open('GameQvest/жекуубилбос.jpg', 'rb')
        bot.send_photo(chat_id=call.message.chat.id, photo=photo41)
        bot.send_message(chat_id=call.message.chat.id,
                         text="Вы попытались нанести удар, но Листат оказался быстрее. Он увернулся от нашей атаки и ловким ударом снес с плечь вашу голов. Вы погибили, а он продолжил развлекаться со своей пленницей.")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы начали бой")
    elif call.data == "ScrollAttack":
        photo42 = open('GameQvest/ЖекаВин.jpg', 'rb')
        bot.send_photo(chat_id=call.message.chat.id, photo=photo42)
        bot.send_message(chat_id=call.message.chat.id,
                         text="Вы использовали свиток и ощутили прилив сил. Вы произвели серию быстрых атак словно берсерк и перед вами осталась лишь куча мяса противника, будто вы разделали свинью.")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы начали бой")
        VinBoss2(call.message)
    elif call.data == "VinBoss2":
        photo43 = open('GameQvest/finalgood.jpg', 'rb')
        bot.send_photo(chat_id=call.message.chat.id, photo=photo43)
        bot.send_message(chat_id=call.message.chat.id,
                         text="Вы освободили девушку и забрали золото. Вскоре, вы с ней поженились и купили огромный дом. Вы жили счастливую и беззаботную жизнь\n\n\n Но ....")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы освободили девушку и забрали золото")
        TenYears(call.message)
    elif call.data == "TenYears":
        photo44 = open('GameQvest/Умерласемья.jpg', 'rb')
        bot.send_photo(chat_id=call.message.chat.id, photo=photo44)
        bot.send_message(chat_id=call.message.chat.id,
                         text="Прошло десять лет, в один из прекрасных солнечных дней, Вы возвращаетесь домой и видите ужасную картину. По дому разбросаны части тел всей вашей семьи и прислуги. А на стене написано кровью: Зря ты решил со мной поссориться, смертный.")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Однажды вы пришли домой")
    elif call.data == "HeartAttack":
        photo45 = open('GameQvest/gekaDemon.jpg', 'rb')
        bot.send_photo(chat_id=call.message.chat.id, photo=photo45)
        bot.send_message(chat_id=call.message.chat.id,
                         text="Вы почувствовали дикий прилив сил. От Вас начала распространяться аура тьмы. Вы никогда не чувствовали себя сильнее, чем сейчас. Ваш противник начал пятиться назад и что-то бормотать.")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы начали бой")
        JekaDemon(call.message)
    elif call.data == "JekaDemon":
        photo46 = open('GameQvest/gekaDemonBoi.jpg', 'rb')
        bot.send_photo(chat_id=call.message.chat.id, photo=photo46)
        bot.send_message(chat_id=call.message.chat.id,
                         text="Вы подошли к нему и одним уверенным движением вырвали ему сердце и затолкали в глотку, затем вырвали ноги и руки. Пленная девушка закричала и затряслась от страха. Вы подумали успокоить ее, но голос в вашей голове начал шептать\n\n\"- Сожри эту мразь... Сожри это аппетитное свежее мясо.\"\n\nВаш разум затуманился, вы набросились на девушку и начали терзать ее зубами и ногтями, вырывать из нее куски мяса, вы никогда в жизни не ели с таким аппетитом.")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы потеряли контроль над собой")
        JekaDemon2(call.message)
    elif call.data == "JekaDemon2":
        photo47 = open('GameQvest/gekaKing.jpg', 'rb')
        bot.send_photo(chat_id=call.message.chat.id, photo=photo47)
        bot.send_message(chat_id=call.message.chat.id,
                         text="Когда вы закончили, вы поняли, что отныне вы являетесь хозяином этой башни, а так же, вы больше никогда не сможете жить без пожирания этого вкуснейшего человеческого мяса.")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы стали владыкой тьмы")
    elif call.data == "Died2":
        photo48 = open('GameQvest/жекуубилбос.jpg', 'rb')
        bot.send_photo(chat_id=call.message.chat.id, photo=photo48)
        bot.send_message(chat_id=call.message.chat.id,
                         text="Вы попытались нанести удар, но Листат оказался быстрее. Он увернулся от нашей атаки и ловким ударом снес с плечь вашу голов. Вы погибили, а он продолжил развлекаться со своей пленницей.")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы начали бой")
    elif call.data == "HeartAttack2":
        photo49 = open('GameQvest/gekaDemon.jpg', 'rb')
        bot.send_photo(chat_id=call.message.chat.id, photo=photo49)
        bot.send_message(chat_id=call.message.chat.id,
                         text="Вы почувствовали дикий прилив сил. От Вас начала распространяться аура тьмы. Вы никогда не чувствовали себя сильнее, чем сейчас. Ваш противник начал пятиться назад и что-то бормотать.")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы начали бой")
        JekaDemon(call.message)
    elif call.data == "SwordAttack":
        photo49 = open('GameQvest/bladeOfSouls.jpg', 'rb')
        bot.send_photo(chat_id=call.message.chat.id, photo=photo49)
        bot.send_message(chat_id=call.message.chat.id,
                         text="Вы ощущаете как меч начал выбрировать, через мгновение из противника полилась жизненная энергия и начала подпитывать меч бездны. Вы решили не тратить времени и предприняли попытку атаковать. Судя по всему меч Бездны не оставил противнику сил даже попытаться отбить удар. С помощью своего нового оружия вы выпотрошили Листата как свинью")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы начали бой")
        VinBoss(call.message)
    elif call.data == "BossAmuletNo2":
        photo30 = open('GameQvest/killgeka.jpg', 'rb')
        bot.send_photo(chat_id=call.message.chat.id, photo=photo30)
        bot.send_message(chat_id=call.message.chat.id,
                         text="Вы нанесли удар по противнику, но вашей силы удара не хватило что бы нанести сильные повреждения. Противник размахнулся и своей косой разделил ваше тело на три части \n\n\nВЫ ПОГИБЛИ")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы Начали сражение с Сашаелем")
    elif call.data == "BossExit2":
        photo31 = open('GameQvest/killsasha.jpg', 'rb')
        bot.send_photo(chat_id=call.message.chat.id, photo=photo31)
        bot.send_message(chat_id=call.message.chat.id,
                         text="Вы использовали свиток и ощутили прилив сил. Вы произвели серию быстрых атак словно берсерк и перед вами осталась лишь куча мяса противника, будто вы разделали свинью.")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы Начали сражение с Сашаелем")
        SashaelKill(call.message)
    elif call.data == "audionext":
        audio_processing(call.message, False)
    elif call.data == "musicStart":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="А вот и музыка")
        audio_processing(call.message, True)
    elif call.data == "audioLike":
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                  text='Готово')
        LikePlayList(call.message)
    elif call.data == "musicList":
        PlayList(call.message)
    elif call.data == "love":
        perc = random.randint(18, 23)
        while (perc < 100):
            try:
                text = "😇 Поиск пары в процесе ..." + str(perc) + "%"
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
    elif call.data == "money":
        money_list = ['moneyOrel', 'moneyRechka', 'moneyBock']
        itog = random.choice(money_list)
        if itog == 'moneyRechka':
            itog = "CAACAgIAAxkBAAEExZhihz9nld8zDsx_xGIJe1UohKY1fQACGRUAAna_QEhmJTifqgABlUUkBA"
            bot.send_sticker(chat_id=call.message.chat.id, sticker=itog)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Выпала Решка")
        if itog == 'moneyOrel':
            itog = "CAACAgIAAxkBAAEExZpih0AP0h2kGOxA6im8S-JnV0TzGgACex0AAqIeOEhfUFiQUgr4EyQE"
            bot.send_sticker(chat_id=call.message.chat.id, sticker=itog)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Выпал Орел")
        if itog == 'moneyBock':
            itog = "CAACAgIAAxkBAAEExZxih0AlAr4WhBhh2ziJhpW6amwxQwACfRcAAvUgQEif-5XszcoaBCQE"
            bot.send_sticker(chat_id=call.message.chat.id, sticker=itog)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Ничия")
    elif call.data == "films":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Приятного просмотра")
        film(call.message)
    elif call.data == "mult":

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Приятного просмотра")
        mult(call.message)
    elif call.data == "anime":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Приятного просмотра")
        anime(call.message)
#Фильмы
@bot.message_handler(commands=["films", "фильмы"])
def films(message, res=False):
    keyfilms = types.InlineKeyboardMarkup()
    key_film = types.InlineKeyboardButton(text='Случайный Фильм', callback_data='films')
    keyfilms.add(key_film)
    key_mult = types.InlineKeyboardButton(text='Случайный Мультик', callback_data='mult')
    keyfilms.add(key_mult)
    key_anime = types.InlineKeyboardButton(text='Случайное Аниме', callback_data='anime')
    keyfilms.add(key_anime)
    bot.send_message(message.chat.id, 'Что хотите посмотреть ?',
                     reply_markup=keyfilms)

#Музыка
@bot.message_handler(commands=["music", "музыка"])
def music(message, res=False):
    keymusic = types.InlineKeyboardMarkup()
    key_musicStart = types.InlineKeyboardButton(text='Включить музыку', callback_data='musicStart')
    keymusic.add(key_musicStart)
    key_musicList = types.InlineKeyboardButton(text='Мой плейлист', callback_data='musicList')
    keymusic.add(key_musicList)
    bot.send_message(message.chat.id, 'Что хотите послушать ?',
                     reply_markup=keymusic)

# Добавление Аудио
@bot.message_handler(content_types=['audio'])
def audio_record(message):
    db = sqlite3.connect('db/JeckaBot.db')
    cur = db.cursor()
    track = str(message.audio.file_unique_id)
    Track_performer = message.audio.performer
    Track_title = message.audio.title
    isNew = True
    UniqueId_list = []
    for UniqueId in cur.execute('SELECT UniqueId FROM Music WHERE UniqueId LIKE ?', ('%' + track + '%',)):
        UniqueId_list.append(UniqueId[0])
        UniqueId_list1 = UniqueId_list[0]
        if str(UniqueId_list1) == str(message.audio.file_unique_id):
            isNew = False
            bot.send_message(message.chat.id, Track_performer + " - " + Track_title + " - Такой трек уже есть ")

    if isNew == True:
        Track_id = message.audio.file_id
        Track_Unique = message.audio.file_unique_id
        Track_Name = message.audio.file_name
        db.execute("INSERT INTO Music (Name, Performer, Title, UniqueId, FileId) VALUES (?, ?, ?, ?, ?);", (Track_Name, Track_performer, Track_title, Track_Unique, Track_id))
        db.commit()
        db.close()
        bot.send_message(message.chat.id, Track_performer + " - " + Track_title + " - Трек сохранен ")

#Игра "Путешествие жеки"
@bot.message_handler(commands=["qvest"])
def GameQvest(message, res=False):
    keygameqvest = types.InlineKeyboardMarkup()
    key_startqvest = types.InlineKeyboardButton(text='Да давай погрузимся в мир фантастики', callback_data='startqvest')
    keygameqvest.add(key_startqvest)
    key_exitqvest = types.InlineKeyboardButton(text='Нет, вернуться назад', callback_data='exitqvest')
    keygameqvest.add(key_exitqvest)
    bot.send_message(message.chat.id, 'Привет хочешь сыграть в игру про путешествия Жеки по волшебному миру ?',
                     reply_markup=keygameqvest)

# Команда "Игра"
@bot.message_handler(commands=["game", "игра"])
def game(message, res=False):
    keygame = types.InlineKeyboardMarkup();
    key_Game1 = types.InlineKeyboardButton(text='Камень,Ножницы,Бумага', callback_data='GameSSP')
    keygame.add(key_Game1)
    key_Game2 = types.InlineKeyboardButton(text='Слот-машина', callback_data='SlotMachine')
    keygame.add(key_Game2)
    key_Game3 = types.InlineKeyboardButton(text='Блекджек', callback_data='BlackJack')
    keygame.add(key_Game3)
    key_qvest = types.InlineKeyboardButton(text='Путешествие Жеки', callback_data='qvest')
    keygame.add(key_qvest)
    key_StatGame = types.InlineKeyboardButton(text='Статистика', callback_data='StatGame')
    keygame.add(key_StatGame)
    bot.send_message(message.chat.id, 'Во что сыграем ?\nВаш Баланс: ' + getBalance(message), reply_markup=keygame)
    isAdmin = False
    for x in admin:
        if message.chat.id == x:
            isAdmin = True
    if (isAdmin == False):
        bot.send_message(UseridMas[0], message.from_user.first_name + " - Пошел Играть")
        bot.send_message(UseridMas[1], message.from_user.first_name + " - Пошел Играть")

# Получить баланс пользователя
def getBalance(message):
    count = 0
    numberMas = -1
    for s in UseridMas:
        if str(s) == str(message.chat.id):
            numberMas = count
        count = count + 1
    Balance = str(masScore[numberMas])
    return Balance

def GameSSP(message, itog, res=False):
    keygame1 = types.InlineKeyboardMarkup();
    key_Stone = types.InlineKeyboardButton(text='Камень🤜', callback_data='Stone')
    keygame1.add(key_Stone)
    key_Scissors = types.InlineKeyboardButton(text='Ножницы✌️', callback_data='Scissors')
    keygame1.add(key_Scissors)
    key_Paper = types.InlineKeyboardButton(text='Бумага✋', callback_data='Paper')
    keygame1.add(key_Paper)
    key_gameexit = types.InlineKeyboardButton(text='Вдругой раз', callback_data='gameexit')
    keygame1.add(key_gameexit)
    if itog == "first":
        bot.send_message(message.chat.id, "играем ? ", reply_markup=keygame1)
    else:
        bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id,
                              text=itog, reply_markup=keygame1)

def randomCard(poolCard, playerScore, itog):
    randomCard = random.choice(poolCard)
    if randomCard == "a":
        if playerScore < 11:
            playerScore = playerScore + 11
            itog = itog + "🃏"
        else:
            playerScore = playerScore + 1
            itog = itog + "🃏"
    if randomCard == 10:
        playerScore = playerScore + randomCard
        itog = itog + "🔟"
    if randomCard == 9:
        playerScore = playerScore + randomCard
        itog = itog + "9️⃣"
    if randomCard == 8:
        playerScore = playerScore + randomCard
        itog = itog + "8️⃣"
    if randomCard == 7:
        playerScore = playerScore + randomCard
        itog = itog + "7️⃣"
    if randomCard == 6:
        playerScore = playerScore + randomCard
        itog = itog + "6️⃣"
    if randomCard == 5:
        playerScore = playerScore + randomCard
        itog = itog + "5️⃣"
    if randomCard == 4:
        playerScore = playerScore + randomCard
        itog = itog + "4️⃣"
    if randomCard == 3:
        playerScore = playerScore + randomCard
        itog = itog + "3️⃣"
    if randomCard == 2:
        playerScore = playerScore + randomCard
        itog = itog + "2️⃣"
    return playerScore, itog

def BJBet(message, itog, res=False):
    keyBJ = types.InlineKeyboardMarkup()
    key_BJbet50 = types.InlineKeyboardButton(text='Ставка 50', callback_data='BlackJack50')
    keyBJ.add(key_BJbet50)
    key_BJbet100 = types.InlineKeyboardButton(text='Ставка 100', callback_data='BlackJack100')
    keyBJ.add(key_BJbet100)
    key_BJbet200 = types.InlineKeyboardButton(text='Ставка 200', callback_data='BlackJack200')
    keyBJ.add(key_BJbet200)
    key_BJexit = types.InlineKeyboardButton(text='Вдругой раз', callback_data='krutkonec')
    keyBJ.add(key_BJexit)
    if itog == "first":
        bot.send_message(message.chat.id, 'Сыграем ?', reply_markup=keyBJ)
    else:
        bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id,
                              text=itog, reply_markup=keyBJ)

def BJGetCard(message, sum, itog, res=False):
    keyBJGetCard = types.InlineKeyboardMarkup()
    key_BJGetCardYes = types.InlineKeyboardButton(text='Еще карту', callback_data='GetCardYes')
    keyBJGetCard.add(key_BJGetCardYes)
    key_BJGetCardNo = types.InlineKeyboardButton(text='Хватит', callback_data='GetCardNo')
    keyBJGetCard.add(key_BJGetCardNo)
    bot.send_message(message.chat.id, 'Сумма: ' + str(sum) + '\n' + itog + '\nЕще карту?', reply_markup=keyBJGetCard)

def BlackJackFirst(message, bet):
    isBankrot, numberMas = updateScore(bet, -bet, message)
    playerScore = 0
    itog = ""
    if isBankrot == False:
        poolCard = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, "a"]
        playerScore, itog = randomCard(poolCard, playerScore, itog)
        playerScore, itog = randomCard(poolCard, playerScore, itog)
        if playerScore == 21:
            isBankrot, numberMas = updateScore(bet, 2 * bet, message)
            x = open('bjSaves//player' + str(message.chat.id) + '.txt', 'w', encoding='UTF-8')
            x.write(str(bet) + '\n' + "0" + '\n' + "0")
            x.close()
            BJBet(message,
                  'Ты выиграл, набрав ' + str(playerScore) + ' \n{}'.format(itog) + "\n" + "Баланс: " + str(
                      masScore[numberMas]) + "(+" + str(bet) + ")")
        else:
            x = open('bjSaves//player' + str(message.chat.id) + '.txt', 'w', encoding='UTF-8')
            x.write(str(bet) + '\n' + str(playerScore) + '\n' + itog)
            x.close()
            BJGetCard(message, playerScore, itog)
    else:
        BJBet(message, "К сожалению, Ваших средств недостаточно, чтобы сделать ставку")

def BlackJackNext(message, getCard):
    poolCard = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, "a"]
    bjmas = []
    ff = open('bjSaves//player' + str(message.chat.id) + '.txt', 'r', encoding='UTF-8')
    for s in ff:
        bjmas.append(s.strip().lower())
    ff.close()
    bet = int(bjmas[0])
    playerScore = int(bjmas[1])
    itog = bjmas[2]
    if getCard == True:
        playerScore, itog = randomCard(poolCard, playerScore, itog)
        if playerScore == 21:
            isBankrot, numberMas = updateScore(bet, 2 * bet, message)
            x = open('bjSaves//player' + str(message.chat.id) + '.txt', 'w', encoding='UTF-8')
            x.write(str(bet) + '\n' + "0" + '\n' + "0")
            x.close()
            BJBet(message, 'Ты выиграл, набрав ' + str(playerScore) + ' \n{}'.format(itog) + "\n" + "Баланс: " + str(
                masScore[numberMas]) + "(+" + str(bet) + ")")
        if playerScore > 21:
            isBankrot, numberMas = updateScore(bet, 0, message)
            x = open('bjSaves//player' + str(message.chat.id) + '.txt', 'w', encoding='UTF-8')
            x.write(str(bet) + '\n' + "0" + '\n' + "0")
            x.close()
            BJBet(message, 'Ты проиграл, набрав ' + str(playerScore) + ' \n{}'.format(itog) + "\n" + "Баланс: " + str(
                masScore[numberMas]) + "(" + str(-bet) + ")")
        if playerScore < 21:
            x = open('bjSaves//player' + str(message.chat.id) + '.txt', 'w', encoding='UTF-8')
            x.write(str(bet) + '\n' + str(playerScore) + '\n' + itog)
            x.close()
            BJGetCard(message, playerScore, itog)
    if getCard == False:
        botItog = ""
        botScore = 0
        botScore, botItog = randomCard(poolCard, botScore, botItog)
        botScore, botItog = randomCard(poolCard, botScore, botItog)
        while botScore <= playerScore:
            botScore, botItog = randomCard(poolCard, botScore, botItog)
        if botScore > 21:
            isBankrot, numberMas = updateScore(bet, 2 * bet, message)
            x = open('bjSaves//player' + str(message.chat.id) + '.txt', 'w', encoding='UTF-8')
            x.write(str(bet) + '\n' + "0" + '\n' + "0")
            x.close()
            BJBet(message, 'Ты выиграл, Жека-крупье набрал ' + str(botScore) + ' \n{}'.format(
                botItog) + "\n" + "Твой Баланс: " + str(
                masScore[numberMas]) + "(+" + str(bet) + ")")
        if botScore == playerScore:
            isBankrot, numberMas = updateScore(bet, bet, message)
            x = open('bjSaves//player' + str(message.chat.id) + '.txt', 'w', encoding='UTF-8')
            x.write(str(bet) + '\n' + "0" + '\n' + "0")
            x.close()
            BJBet(message, 'Ничья, Жека-крупье набрал ' + str(botScore) + ' \n{}'.format(
                botItog) + "\n" + "Твой Баланс: " + str(
                masScore[numberMas]) + "(+" + str(0) + ")")
        if botScore > playerScore:
            if botScore <= 21:
                isBankrot, numberMas = updateScore(bet, 0, message)
                x = open('bjSaves//player' + str(message.chat.id) + '.txt', 'w', encoding='UTF-8')
                x.write(str(bet) + '\n' + "0" + '\n' + "0")
                x.close()
                BJBet(message, 'Ты проиграл, Жека-крупье набрал ' + str(botScore) + ' \n{}'.format(
                    botItog) + "\n" + "Твой Баланс: " + str(
                    masScore[numberMas]) + "(-" + str(bet) + ")")

def slotMachine(message, betValue):
    bet = betValue
    slot1 = ""
    slot2 = ""
    slot3 = ""
    point = 0
    randSlot = random.randint(0, 100)
    if randSlot <= 20:
        slot1 = "💰"
    elif randSlot <= 43:
        slot1 = "🍌"
    elif randSlot <= 71:
        slot1 = "🍋"
    elif randSlot > 71:
        slot1 = "🍒"
    randSlot = random.randint(0, 100)
    if randSlot <= 20:
        slot2 = "💰"
    elif randSlot <= 43:
        slot2 = "🍌"
    elif randSlot <= 71:
        slot2 = "🍋"
    elif randSlot > 71:
        slot2 = "🍒"
    randSlot = random.randint(0, 100)
    if randSlot <= 20:
        slot3 = "💰"
    elif randSlot <= 43:
        slot3 = "🍌"
    elif randSlot <= 71:
        slot3 = "🍋"
    elif randSlot > 71:
        slot3 = "🍒"
    itog = slot1 + slot2 + slot3
    if slot1 == slot2 == slot3:
        if slot1 == "💰":
            point = bet * 100
        if slot1 == "🍌":
            point = bet * 10
        if slot1 == "🍋":
            point = bet * 5
        if slot1 == "🍒":
            point = bet * 3
        isBankrot, numberMas = updateScore(bet, point, message)
        if isBankrot == False:
            itog = "Ты выиграл \n{}".format(itog) + "\n" + "Баланс: " + str(masScore[numberMas]) + "(+" + str(
                point) + ")"
        else:
            itog = "bankrot"
    else:
        point = bet * (-1)
        isBankrot, numberMas = updateScore(bet, point, message)
        if isBankrot == False:
            itog = "Увы, но ты проиграл \n{}".format(itog) + "\n" + "Баланс: " + str(masScore[numberMas]) + "(" + str(
                point) + ")"
        else:
            itog = "bankrot"
    return itog

def updateScore(bet, point, message):
    count = 0
    numberMas = -1
    isBankrot = False
    for s in UseridMas:
        if s == str(message.chat.id):
            numberMas = count
        count = count + 1
    if numberMas >= 0:
        if masScore[numberMas] >= bet:
            masScore[numberMas] = masScore[numberMas] + point
            x = open('data//balls.txt', 'w', encoding='UTF-8')
            for s in masScore:
                x.write(str(s).strip() + '\n')
            x.close()
        else:
            isBankrot = True
        return isBankrot, numberMas
    else:
        isBankrot = False
        return isBankrot, numberMas

# Функция "Ставка в слот-машине"
def SlotBet(message, itog, res=False):
    keykazino = types.InlineKeyboardMarkup()
    key_bet10 = types.InlineKeyboardButton(text='Ставка 10', callback_data='SlotBet10')
    keykazino.add(key_bet10)
    key_bet50 = types.InlineKeyboardButton(text='Ставка 50', callback_data='SlotBet50')
    keykazino.add(key_bet50)
    key_krutexit = types.InlineKeyboardButton(text='Вдругой раз', callback_data='krutkonec')
    keykazino.add(key_krutexit)
    if itog == "first":
        bot.send_message(message.chat.id, 'Сыграем ?', reply_markup=keykazino)
    elif itog == "bankrot":
        bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id,
                              text="К сожалению, твой баланс не позволяет сделать ставку")
    else:
        bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id,
                              text=itog)
        time.sleep(0.5)
        bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id,
                              text=itog, reply_markup=keykazino)


# Команда «Старт»
@bot.message_handler(commands=["start", "старт"])
def start(message, res=False):
    fz = open('data/UseridMas.txt', 'a', encoding='UTF-8')
    fk = open('data/balls.txt', 'a', encoding='UTF-8')
    pl = open('usersPlayLists/music' + str(message.chat.id) + '.txt', 'a', encoding='UTF-8')
    sz = str(message.chat.id)
    countUserId = 0
    for x5 in UseridMas:
        if (sz.lower().strip() == x5.lower().strip()):
            countUserId = countUserId + 1
    if (countUserId == 0):
        global standatPoint
        fz.write(sz.strip() + '\n')
        fk.write(str(standatPoint).strip() + '\n')
        masScore.append(standatPoint)
        UseridMas.append(sz.strip())
        weatherStatus.append(0)
    fz.close()
    fk.close()
    pl.close()
    bot.send_message(message.chat.id,
                     '{} Привет, меня зовут ЖекаБот. Напиши мне Привет :)\nОбязательно введи /help что бы увидеть что я умею'.format(
                         message.from_user.first_name))

# Команда "ХЕЛП"
@bot.message_handler(commands=["help"])
def help(message, res=False):
    bot.send_message(message.chat.id, '{} Привет, вот что я умею'.format(
        message.from_user.first_name) + '\n❕ Список Команд ❕\n/weather - Погода в вашем городе\n/course - Курс различных валют\n/music - Послушать музыку\n/game - Поиграть в игры\n/menu - Вызвать меню\nЧтобы узнать гороскоп на сегодня, напиши мне, например "гороскоп весы"\nА так же, я могу отвечать на твои сообщения, картинки, стикеры.\nИ каждый день учусь новому.')

# Команда "Бот меню"
@bot.message_handler(commands=["menu"])
def menu(message, res=False):
    keyboardgame = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('/погода')
    btn2 = types.KeyboardButton('/курс')
    btn3 = types.KeyboardButton('/фильмы')
    btn4 = types.KeyboardButton('/музыка')
    btn5 = types.KeyboardButton('/игра')
    btn6 = types.KeyboardButton('/admin')
    keyboardgame.add(btn1, btn2, btn3, btn4, btn5, btn6)
    bot.send_message(message.chat.id, 'Что нужно ? ', reply_markup=keyboardgame)

# Команда "Погода"
@bot.message_handler(commands=["погода", "weather"])
def weather(message, res=False):
    count = 0
    for x in UseridMas:
        if str(x) == str(message.chat.id):
            weatherStatus[count] = 1
        count = count + 1
    bot.send_message(chat_id=message.chat.id, text='В Каком городе тебя интересует погода ?')

def textCity(message):
    bot.send_message(chat_id=message.chat.id, text=get_weather(message.text, open_weather_token))

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
        text2 = ('я не знаю такого города')
        return text2

# Команда "Гороскоп"
def handle_Aries(message):
    isGoroscope = False
    indexCommand = message.text.find(" ")
    CommandString = message.text[:indexCommand]
    if (fuzz.token_sort_ratio(CommandString, "гороскоп") > 90):
        isGoroscope = True
        Similary = [0] * 12
        index = message.text.find(" ")
        sign = message.text[index + 1:]
        Similary[0] = (fuzz.token_sort_ratio(sign, "овен"))
        Similary[1] = (fuzz.token_sort_ratio(sign, "телец"))
        Similary[2] = (fuzz.token_sort_ratio(sign, "близнецы"))
        Similary[3] = (fuzz.token_sort_ratio(sign, "лев"))
        Similary[4] = (fuzz.token_sort_ratio(sign, "дева"))
        Similary[5] = (fuzz.token_sort_ratio(sign, "весы"))
        Similary[6] = (fuzz.token_sort_ratio(sign, "скорпион"))
        Similary[7] = (fuzz.token_sort_ratio(sign, "стрелец"))
        Similary[8] = (fuzz.token_sort_ratio(sign, "козерог"))
        Similary[9] = (fuzz.token_sort_ratio(sign, "водолей"))
        Similary[10] = (fuzz.token_sort_ratio(sign, "рыбы"))
        Similary[11] = (fuzz.token_sort_ratio(sign, "рак"))
        maxSimilary = max(Similary)
        count = 0
        for x in Similary:
            if x == maxSimilary:
                ourSignNumber = count
            count = count + 1
        engSign = " "
        if (ourSignNumber == 0):
            engSign = "aries"
            sign = "Овен"
        if (ourSignNumber == 1):
            engSign = "taurus"
            sign = "Телец"
        if (ourSignNumber == 2):
            engSign = "gemini"
            sign = "Близнецы"
        if (ourSignNumber == 11):
            engSign = "cancer"
            sign = "Рак"
        if (ourSignNumber == 3):
            engSign = "leo"
            sign = "Лев"
        if (ourSignNumber == 4):
            engSign = "virgo"
            sign = "Дева"
        if (ourSignNumber == 5):
            engSign = "libra"
            sign = "Весы"
        if (ourSignNumber == 6):
            engSign = "scorpio"
            sign = "Скорпион"
        if (ourSignNumber == 7):
            engSign = "sagittarius"
            sign = "Стрелец"
        if (ourSignNumber == 8):
            engSign = "capricorn"
            sign = "Козерог"
        if (ourSignNumber == 9):
            engSign = "aquarius"
            sign = "Водолей"
        if (ourSignNumber == 10):
            engSign = "pisces"
            sign = "Рыбы"
        if maxSimilary<70:
            bot.send_message(message.chat.id, "Не знаю такого знака зодиака")
        else:
            file = urllib2.urlopen(
                'https://ignio.com/r/export/utf/xml/daily/com.xml')
            data = file.read()
            file.close()
            data = xmltodict.parse(data)
            Aries = sign + '\n' + data["horo"][engSign]["today"]
            bot.send_message(message.chat.id, Aries)

    return isGoroscope

# Команда "Пара дня"
def handle_Para(message):
    para = False
    if (fuzz.token_sort_ratio(message.text.lower().strip(), "Пара дня") > 70):
        hack(message)
        para = True
    return para

def hack(message):
    keylove = types.InlineKeyboardMarkup()
    key_love = types.InlineKeyboardButton(text='Поиск пары дня', callback_data='love')
    keylove.add(key_love)
    bot.send_message(message.chat.id, 'Ну что найдем для тебя пару дня ?', reply_markup=keylove)

# Команда "Орел  Решка"
def handle_Brocok(message):
    Brocok = False
    if (fuzz.token_sort_ratio(message.text.lower().strip(), "Орел или Решка") > 70):
        money(message)
        Brocok = True
    return Brocok

def money(message):
    keymoney = types.InlineKeyboardMarkup()
    key_money = types.InlineKeyboardButton(text='Бросить монету', callback_data='money')
    keymoney.add(key_money)
    bot.send_message(message.chat.id, 'Подбросим монету ?', reply_markup=keymoney)

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
        bot.send_message(message.chat.id, ' {}, У Вас нет прав администратора'.format(message.from_user.first_name))

def cancelButton(message):
    keyCancel = types.InlineKeyboardMarkup();  # наша клавиатура
    key_cancel = types.InlineKeyboardButton(text='Отменить операцию', callback_data='cancel');  # кнопка «Да»
    keyCancel.add(key_cancel);  # добавляем кнопку в клавиатуру
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
        if ('u: ' in q):
            degreeOfSimilarity = (fuzz.token_sort_ratio(q.replace('u: ', ''), questionString))
            if (degreeOfSimilarity > maximumSimilarity):
                maximumSimilarity = degreeOfSimilarity
                questionNumberToAdd = elementNumber
        elementNumber = elementNumber + 1
    if (maximumSimilarity > 70):
        questionOfSimilary = "В базе есть похожий вопрос:\n" + mas[questionNumberToAdd].replace('u: ',
                                                                                                '') + "\n" + "ты уверен, что хочешь добавить новый?"
        keyboard = types.InlineKeyboardMarkup()  # наша клавиатура
        key_yes = types.InlineKeyboardButton(text='Добавить', callback_data='yes')  # кнопка «Да»
        keyboard.add(key_yes);  # добавляем кнопку в клавиатуру
        key_no = types.InlineKeyboardButton(text='Добавить ответ к существующему', callback_data='no')
        keyboard.add(key_no);
        bot.send_message(message.chat.id, questionOfSimilary, reply_markup=keyboard)
    else:
        update(questionString, answerString)

def handle_UserId(message):
    # Запись userId
    fz = open('data/UseridMas.txt', 'a', encoding='UTF-8')
    fk = open('data/balls.txt', 'a', encoding='UTF-8')
    fi = open('data/UserName.txt', 'a', encoding='UTF-8')
    pl = open('usersPlayLists/music' + str(message.chat.id) + '.txt', 'a', encoding='UTF-8')
    si = str(message.from_user.first_name)
    sz = str(message.chat.id)
    fi.write(si.strip() + ' ID: ' + sz.strip() + '\n')
    countUserId = 0
    for x5 in UseridMas:
        if (sz.lower().strip() == str(x5).lower().strip()):
            countUserId = countUserId + 1
    if (countUserId == 0):
        global standatPoint
        fz.write(sz.strip() + '\n')
        fk.write(str(standatPoint).strip() + '\n')
        masScore.append(standatPoint)
        UseridMas.append(sz.strip())
        weatherStatus.append(0)
    fz.close()
    fk.close()
    fi.close()
    pl.close()

def handle_Time(message):
    if (fuzz.token_sort_ratio(message.lower().strip(), "сколько времени?") > 70):
        tz = pytz.timezone('Asia/Krasnoyarsk')
        nvk_current_datetime = datetime.now(tz).strftime("%y.%m.%d %H:%M:%S")
        c_date, c_time = nvk_current_datetime.split()
        Time = f"У тебя че, телефона нет? \nНу на {c_time}"
        return Time

@bot.message_handler(content_types=["text"])
def handle_text(message):
    realAnswer = ""
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
    handle_UserId(message)
    para = handle_Para(message)
    Brocok = handle_Brocok(message)
    isGoroscope = handle_Aries(message)
    isStandarnAnswer = True
    timeAnswer = handle_Time(message.text)
    numberUser = 0
    count = 0
    for x in UseridMas:
        if x == str(message.chat.id):
            numberUser = count
        count = count + 1
    if weatherStatus[numberUser] == 1:
        textCity(message)
        weatherStatus[numberUser] = 0
        isStandarnAnswer = False
        realAnswer = "*Был дан ответ о погоде*"
    if (isAddQuestion == True):
        if (isAdmin == True):
            if (addAdmin == str(message.chat.id)):
                addQuestion(message)
                isStandarnAnswer = False
                isAddQuestion = False
                addAdmin = "0"
                realAnswer = "*Был добавлен вопрос*"
    if (isPush == True):
        if (isAdmin == True):
            if (pushAdmin == str(message.chat.id)):
                push(message.text)
                pushAdmin = "0"
                realAnswer = "*Был отправлен пуш*"
                isStandarnAnswer = False
                isPush = False
    if (para == True):
        isStandarnAnswer = False
        realAnswer = "*Была подобрана пара*"
    if (isGoroscope == True):
        isStandarnAnswer = False
        realAnswer = "*Был отправлен гороскоп*"
    if (Brocok == True):
        isStandarnAnswer = False
        realAnswer = "*Была подкинута монетка*"
    if (timeAnswer != None):
        bot.send_message(message.chat.id, timeAnswer)
        isStandarnAnswer = False
        realAnswer = timeAnswer
    if (isStandarnAnswer == True):
        realAnswer = answer(message.text)
        bot.send_message(message.chat.id, realAnswer)
    f = open('data/logi/' + str(message.chat.id) + '_' + str(message.from_user.username) + '_log.txt', 'a',
             encoding='UTF-8')
    f.write('u: ' + message.text + '\n' + realAnswer + '\n')
    f.close()
    if (isAdmin == False):
        if (ignoreListParameter == False):
            bot.send_message(UseridMas[0], message.from_user.first_name + "\n" + message.text + "\n" + realAnswer)
            bot.send_message(UseridMas[1], message.from_user.first_name + "\n" + message.text + "\n" + realAnswer)

# Запускаем бота
bot.polling(none_stop=True, interval=0)
